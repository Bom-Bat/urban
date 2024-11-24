from django.shortcuts import render
from django.views.generic import TemplateView


def func_template(request):
    return render(request, 'func_template.html')


class class_template(TemplateView):
    template_name = 'class_template.html'


# Create your views here.
