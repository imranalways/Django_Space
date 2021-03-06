from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from PostApp.models import Post
from PostApp.serializers import PostSerializer
# Create your views here.

@csrf_exempt
def postgetbyid(request,id):
    if request.method=='GET':
        post= Post.objects.get(PostId=id)
        post_serializer= PostSerializer(post,many=False)
        return JsonResponse(post_serializer.data,safe=False)

@csrf_exempt
def PostApi(request,id=0):
    if request.method=='GET':
        post= Post.objects.all()
        post_serializer= PostSerializer(post,many=True)
        return JsonResponse(post_serializer.data,safe=False)

    elif request.method=='POST':
        post_data=JSONParser().parse(request)
        post_serializer=PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Added Successfully!!!",safe=False)
        return JsonResponse(post_data,safe=False)

    elif request.method=='PUT':
        post_data=JSONParser().parse(request)
        post=Post.objects.get(PostId=post_data['id'])
        post_serializer=PostSerializer(post,data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Updated Successfully!!!",safe=False)
        return JsonResponse(post_data,safe=False)
    
    elif request.method=='DELETE':
        post_data=JSONParser().parse(request)
        post=Post.objects.get(PostId=post_data['PostId'])
        post.delete()
        return JsonResponse("Deleted Successfully",safe=False)
        
