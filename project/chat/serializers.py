from rest_framework import serializers
from .models import *


class GroupChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = ('id', 'name') #'participant__userThrough')
