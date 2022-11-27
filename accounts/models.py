from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

def content_file_name(instance, filename):
	return '/'.join(['users', 'avatars', instance.first_name + ' ' + instance.last_name  ,  filename])


class User(AbstractUser):
	ROLE_STATUS = (
		('1','مدیر'),
		('2','فروشنده'),
		('3','نویسنده'),
		('4','امور مالی'),
		('5','مسئول سفارشات'),
		('6','کارمند'),
		('7','سئو'),
		('8','مشترک'),
	)

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	phone = PhoneNumberField(region="IR",null=False, blank=False, unique=True)
	role = models.CharField(max_length=1,null=True,blank=False,choices=ROLE_STATUS)
	avatar = models.ImageField(upload_to=content_file_name,default='users/avatar/default/user-img.png')
	about = models.TextField(max_length=250, blank=True, null=True)







