from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import *
from .utlis import send_notification
from django.utils.translation import activate

# Create your views here.
class test(TemplateView):
    template_name = 'dashboard/index.html'


def testnotif(request):
    send_notification(
        user=request.user, 
        title='عنوان ازمایش2ی',
        text='این 2متن ازمایشی نوتیف هست',
    )
    return redirect('text')

def Change_lang(request):
	activate(request.GET.get('lang'))
	return redirect('/')