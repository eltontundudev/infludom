from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.template.context_processors import csrf
from django.shortcuts import redirect, render
from .models import Talent, Project
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializer import TalentSerializer, ProjectSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

"""
Index function is for the home page of the website.
"""


class TalentViews(APIView):
    def post(self, request):
        serializer = TalentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    template = loader.get_template('index.html')
    # tasks = Task.objects.order_by("id")
    # more_tasks = Task.objects.filter()
    context = {'tasks': "welcome"}
    context.update(csrf(request))
    # return render('index.html', context)
    return HttpResponse(template.render(context, request))


class TalentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = TalentSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = ProjectSerializer

#
# def add(request):
#     item = Task(name=request.POST["name"])
#     item.save()
#     return redirect("/")
#
#
# def remove(request):
#     item = Task.objects.get(id=request.POST["id"])
#     if item:
#         item.delete()
#     return redirect("/")
#
#
# def post(request):
#     template = loader.get_template('index.html')
#     mabasa = Task.objects.all()
#     context = {'mabase': mabasa}
#     return HttpResponse(template.render(context, request))
