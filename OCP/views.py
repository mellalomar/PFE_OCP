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
    try:
        for dic_single in dict_data:
            details=Detail()
            details.name=dic_single['name']
            details.BPL=dic_single['BPL']
            details.MgO=dic_single['MgO']
            details.MO=dic_single['MO']
            details.SiO2=dic_single['SiO2']
            details.CO2=dic_single['CO2']
            details.save()
        if(request.method == 'POST' and 'run_script' in request.POST):
            print("simulation begin")
        print(" begin")
        response_data={"error":False,"errorMessage":"Updated Successfully"}
        return JsonResponse(response_data,safe=False)
        
    except:
        response_data={"error":True,"errorMessage":"Failed to Update Data"}
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
    #try:
    for dic_single in dict_data:
        
        name = dic_single['name']
        BPL = dic_single['BPL']
        MgO = dic_single['MgO']
        MO = dic_single['MO']
        SiO2 = dic_single['SiO2']
        CO2 = dic_single['CO2']
        prediction = simulation(BPL,MgO,MO,SiO2,CO2,name)
    res = f"predicted value of {name} is {prediction}"
    response_data={"error":False,"errorMessage":res}
    return JsonResponse(response_data,safe=False)
        
    #except:
    #    response_data={"error":True,"errorMessage":"Failed to Simulate"}
    #    return JsonResponse(response_data,safe=False)
    
