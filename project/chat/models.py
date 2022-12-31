from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse


class MyUser(AbstractUser):
    picture = models.ImageField(upload_to='images/', default=None)

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])


class GroupChat(models.Model):
    name = models.CharField(max_length=255)
    participant = models.ManyToManyField(MyUser, through='UserGroup', related_name='participant')

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='author')
    date_and_time = models.DateTimeField(auto_now_add=True)
    message_text = models.TextField()


# Сообщения в групповой чат
class GroupMessage(Message):
    group = models.ForeignKey(GroupChat, on_delete=models.CASCADE, related_name='group')


class PrivateMessage(Message):
    recipient = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='recipient')


class UserGroup(models.Model):
    groupThrough = models.ForeignKey(GroupChat, on_delete=models.CASCADE, related_name='allgroups')
    userThrough = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='allparticipants')
