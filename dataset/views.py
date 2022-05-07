import csv
from django.shortcuts import render
from django.http import HttpResponse
from .models import dataset
from django.http import JsonResponse
from .serializers import *
from rest_framework.request import Request
import json
from rest_framework.decorators import api_view


from django.core.files.storage import FileSystemStorage

# Create your views here.

def export_dataset(request):
    response=HttpResponse(content_type='text/csv')
    writer=csv.writer(response)
    writer.writerow(['video_path','age','gender','diagnosedWithADHD','responseTime','correctTimingResponses','correctAttentionResponses','hyperactivityTarget','hyperactivityNonTarget','hyperactivityRandom','impulsiveResponses','omissionErrors','totalResponses'])
    for data in dataset.objects.all().values_list('video_path','age','gender','diagnosedWithADHD','responseTime','correctTimingResponses','correctAttentionResponses','hyperactivityTarget','hyperactivityNonTarget','hyperactivityRandom','impulsiveResponses','omissionErrors','totalResponses'):
        writer.writerow(data)
    response['Content-Disposition']='attachment; filename="dataset.csv"'
    return response

@api_view(["POST"])
def insert_dataset_record(request):
    print(request)
    videofile = request.FILES['videoData']
    fs = FileSystemStorage(location="videos")
    #body_unicode = request.data.decode('utf-8')
    print(request.data)
    #body = json.loads(request.data)
    #print(videofile.name)
    filename = fs.save(videofile.name, videofile)
    print("request",request.data)
    request.data['video_path']=filename
    if request.method == 'POST':
        serializer = DatasetSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Your order went well"
            return JsonResponse({"data":data})
        return JsonResponse({"error":serializer.errors})
    return JsonResponse({"error":"error"})

def hello(request):
    return "hello"
def download(request):
    file_path="videos/OpenGL Application 2021-01-24 19-46-54.mp4"
    with open(file_path) as f:
        response= HttpResponse(f.read(),content_type="application/adminupload")
        response['Content-Disposition'] = "inline:filename"+os.path.basename(file_path)
        return response




