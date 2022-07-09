from django.shortcuts import render
from django.http import HttpResponse

from django_tables2 import Table
from . import tables
from . import models

# Create your views here.

from .models import AnnualPopulation


def index(request):
    render_context = {}
    return render(
        request, template_name="countries/css_main_page.html", context=render_context
    )

from . import tables

class NonceTable1(Table):
    class Meta:
        model = AnnualPopulation
        field = ("year", "population", "country_id")


def simple_table_without_explicit_style(request):
    generic_table = NonceTable1(AnnualPopulation.objects.all()[:45])
    render_context = {"table": generic_table}
    return render(
        request,
        template_name="countries/bootstrap4-shell.html",
        context=render_context,
    )

from django_tables2 import RequestConfig

def no_template_in_table_class(request):
    table = tables.Bootstrap4CountryCodesTable(data=models.Country.objects.all())
    configurer = RequestConfig(request, paginate={'per_page': 5})
    configurer.configure(table)
    return render(request,
                  template_name="countries/bootstrap4-shell.html",
                  context = {'table': table})

def extends_built_in(request):
    # this is same as "no_template_in_table_class", except for the template
    table = tables.Bootstrap4CountryCodesTable(data=models.Country.objects.all())
    configurer = RequestConfig(request, paginate={'per_page': 5})
    configurer.configure(table)
    return render(request,
                  template_name="countries/bootstrap4-shell.html",
                  context={'table': table,
                           'bootstrap4_before_content': 'before content'})



