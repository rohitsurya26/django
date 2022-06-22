# from django.shortcuts import render

# from django.http import HttpResponse



# def homePageView(request):

#     return HttpResponse('Hello, World!')
from django.views.generic import TemplateView
class homePageView(TemplateView):
    template_name = 'manga/home.html'
