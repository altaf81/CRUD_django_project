from re import search
from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='ermsapp/index.html'), name='home'),
    path('aboutus/', TemplateView.as_view(
        template_name='ermsapp/aboutus.html'), name='aboutus'),
    path('contactus/', TemplateView.as_view(
        template_name='ermsapp/contactus.html'), name='contactus'),
    path('addemp/', addemp, name='addemp'),
    path('emplist/', emplist, name='emplist'),
    path('deleteemp/<int:emp_id>', deleteemp, name='deleteemp'),
    path('deleteemp2', deleteemp2, name='deleteemp'),
    path('updateemp/<int:emp_id>', updateemp, name='updateemp'),
    path('sortasc', sortasc),
    path('sortdesc', sortdesc),
    path('searchemp', searchemp),

]
