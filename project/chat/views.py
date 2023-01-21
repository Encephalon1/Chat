from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from rest_framework import viewsets
from .serializers import *
from .models import *
from .forms import Avatar


class IndexView(LoginRequiredMixin, TemplateView):
    model = MyUser
    template_name = 'index.html'


class GroupChatViewSet(viewsets.ModelViewSet):
    serializer_class = GroupChatSerializer
    queryset = GroupChat.objects.all()


class LoadAvatar(UpdateView):
    form_class = Avatar
    model = MyUser
    template_name = 'load_avatar.html'

    def home(self, request):
        images = MyUser.objects.all()
        context = {
            'images': images
        }
        return render(request, 'load_avatar.html', context)

    def file_upload(self, request):
        if request.method == 'POST':
            my_files = request.FILES.get('file')
            MyUser.objects.create(content=my_files)
            return HttpResponse('img/')
        return JsonResponse({'post': 'fasle'})


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})
