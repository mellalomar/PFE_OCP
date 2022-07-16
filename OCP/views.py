import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django_tables2 import Table
from .models import Info, Person, Details, Detail
from .templates.table import PersonTable,InfoTable
from django_tables2 import SingleTableView
from django.views.decorators.csrf import csrf_exempt
# Create your views here.




def home(request):
    return HttpResponse("hello .html")


class PersonListView(ListView):
    model = Person
    template_name = 'people.html'

class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'people.html'

class InfoListView(SingleTableView):
    model = Info
    table_class = InfoTable
    template_name = 'people.html'


##############################

def HomePage(request):
    data=Detail.objects.all()
    return render(request,"homepage.html",{"data":data})


@csrf_exempt
def insert(request):
    request.session['Columns_name'] = ['name'].append([f"car {i}" for i in range(5)])
    data=request.POST.get("data")
    dict_data=json.loads(str(data))
    try:
        for dic_single in dict_data:
            details=Detail()
            details.First_Name=dic_single['First_Name']
            details.Last_Name=dic_single['Last_Name']
            details.City=dic_single['City']
            details.save()
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
            details.First_Name=dic_single['First_Name']
            details.Last_name=dic_single['Last_Name']
            details.City=dic_single['City']
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
