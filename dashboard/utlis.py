from .models import *


def send_notification(user, title, text):
    Notification.objects.get_or_create(user=user, title=title, text=text)