import imp
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django_tables2 import Table
from .models import  Detail
#from .templates.table import PersonTable,InfoTable
from django_tables2 import SingleTableView
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .management.commands.simulate import simulation 
from math import floor


def home(request):
    return HttpResponse("hello .html")



##############################

def HomePage(request):
    data=Detail.objects.all()
    return render(request,"homepage.html",{"data":data})


@csrf_exempt
def insert(request):
    #request.session['Columns_name'] = ['name'].append([f"car {i}" for i in range(5)])
    data=request.POST.get("data")
    dict_data=json.loads(str(data))
    print("insertion start ...")
    s = 0
    Detail.objects.all().delete()
    try:
        
        for dic_single in dict_data:
            print(dic_single)
            
            details=Detail()
            name = dic_single['name']
            BPL = float(dic_single['BPL'])
            MgO = float(dic_single['MgO'])
            MO = float(dic_single['MO'])
            SiO2 = float(dic_single['SiO2'])
            CO2 = float(dic_single['CO2'])
            distance = float(dic_single['distance'])
           
            details.name = name
            details.BPL= BPL
            details.MgO=MgO
            details.MO=MO
            details.SiO2=SiO2
            details.CO2=CO2
            details.distance=distance
            
            
            if( BPL+MgO+MO+SiO2+CO2 == 0):
                details.Mix = 0
            else:
                
                details.Mix = simulation(BPL,MgO,MO,SiO2,CO2,name)
                s += details.Mix
        for dic_single in dict_data:
            print(dic_single)
            details=Detail()
            
            name = dic_single['name']
            BPL = float(dic_single['BPL'])
            MgO = float(dic_single['MgO'])
            MO = float(dic_single['MO'])
            SiO2 = float(dic_single['SiO2'])
            CO2 = float(dic_single['CO2'])
            distance = float(dic_single['distance'])
           
            details.name = name
            details.BPL= BPL
            details.MgO=MgO
            details.MO=MO
            details.SiO2=SiO2
            details.CO2=CO2
            details.distance=distance
            
            
            if( BPL+MgO+MO+SiO2+CO2 == 0):
                tempMix = 0
            else:
                
                tempMix = simulation(BPL,MgO,MO,SiO2,CO2,name)
            details.Mix = tempMix*100/s
            temps=distance/667
            NV=floor((details.Mix/100)*38)
            CD=temps*2+2.5+1.82
            R=floor((CD*NV)/60)
            details.distance=R
            details.save()
    
        print(" begin")

        response_data={"error":False,"errorMessage":"Updated Successfully"}
        return JsonResponse(response_data,safe=False)
    
    except:
        response_data={"error":True,"errorMessage":"Failed to insert Data"}
        return JsonResponse(response_data,safe=False)
    

@csrf_exempt
def update_details(request):
    data=request.POST.get("data")
    dict_data=json.loads(data)
    try:
        for dic_single in dict_data:
            details=Detail.objects.get(id=dic_single['id'])
            details.name=dic_single['Layer name']
            details.BPL=dic_single['BPL']
            details.MgO=dic_single['MgO']
            details.MO=dic_single['MO']
            details.SiO2=dic_single['SiO2']
            details.CO2=dic_single['CO2']
            details.distance=dic_single['distance']
            
            details.save()
        response_data={"error":False,"errorMessage":"Updated Successfully"}
        return JsonResponse(response_data,safe=False)
    except:
        response_data={"error":True,"errorMessage":"Failed to Update Data"}
        return JsonResponse(response_data,safe=False)

@csrf_exempt
def delete_details(request):
    id=request.POST.get("id")
    try:
        details=Detail.objects.get(id=id)
        details.delete()
        response_data={"error":False,"errorMessage":"Deleted Successfully"}
        return JsonResponse(response_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Failed to Delete Data"}
        return JsonResponse(response_data,safe=False)

        
def insert_table(request):
    return render(request,"table.html")



@csrf_exempt
def simulate(request):
    #request.session['Columns_name'] = ['name'].append([f"car {i}" for i in range(5)])
    data=request.POST.get("data")
    dict_data=json.loads(str(data))
    print("simulation begin")
    try:
        for dic_single in dict_data:
            
            name = dic_single['name']
            BPL = dic_single['BPL']
            MgO = dic_single['MgO']
            MO = dic_single['MO']
            SiO2 = dic_single['SiO2']
            CO2 = dic_single['CO2']
            distance = dic_single['distance']
            if(BPL,MgO,MO,SiO2,CO2==0,0,0,0,0):
                prediction =0
            
            else:
                prediction = simulation(BPL,MgO,MO,SiO2,CO2,name)
        res = f"predicted value for    ''  {name}  ''    layer is :    {prediction}"
        response_data={"error":False,"errorMessage":res}
        return JsonResponse(response_data,safe=False)
        
    except:
        response_data={"error":True,"errorMessage":"Failed to Simulate"}
        return JsonResponse(response_data,safe=False)

@csrf_exempt   
def dashboard(request):
    data=request.POST.get("data")
    dict_data=json.loads(str(data))
    
    try:
        for dic_single in dict_data:
            details=Detail()
            name = dic_single['name']
            BPL = dic_single['BPL']
            MgO = dic_single['MgO']
            MO = dic_single['MO']
            SiO2 = dic_single['SiO2']
            CO2 = dic_single['CO2']
            distance = dic_single['distance']
            details.name = name
            details.BPL = BPL
            details.MgO = MgO
            details.MO = MO
            details.SiO2 = SiO2
            details.CO2 = CO2
            details.distance = distance
            if([BPL,MgO,MO,SiO2,CO2]==[0,0,0,0,0]):
                details.Mix = 0
            else:
                details.Mix = simulation(BPL,MgO,MO,SiO2,CO2,name)
            details.save()
            print("  mix %  >>>>>>" + str(details.Mix))
        
        response_data={"error":False,"errorMessage":"Updated Successfully !!"}
        #return JsonResponse(response_data,safe=False)
        
    except:
        response_data={"error":True,"errorMessage":"Failed to Update Data"}
        #return JsonResponse(response_data,safe=False)
    #return render(request,"dashboard.html")
    data=Detail.objects.all()
    print("start " + str(dict_data))
    return render(request,"dashboard.html",{"data":data})



