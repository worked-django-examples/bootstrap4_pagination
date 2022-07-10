from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import HttpResponse
# Create your views here.

from countries.models import Country
from .tables import Bootstrap4_example1_no_template_table, Bootstrap4_example1_with_template_table

def index(request):
    return render(request, "demos/demos.html")

COUNTRIES_100 = Country.objects.all()[:100]

def example_1(request, table_class, page_title='Page Title'):
    table = table_class(data=COUNTRIES_100)
    configurer = RequestConfig(request, paginate={'per_page': 8})
    configurer.configure(table)
    return render(request=request,
                  template_name='demos/example_1.html',
                  context={'table': table,
                  'page_title': page_title})

def example_1_working_pagination(request):
    page_title = 'Example 1, template in table.Meta makes it work'
    return example_1(request, Bootstrap4_example1_with_template_table, page_title)

def example_1_broken_pagination(request):
    page_title = 'Example 1, no styling on pagination'
    return example_1(request, Bootstrap4_example1_no_template_table, page_title)

