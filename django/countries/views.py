from django.shortcuts import render
from django.http import HttpResponse

from django_tables2 import Table


# Create your views here.

from .models import AnnualPopulation


def index(request):
    render_context = {}
    return render(
        request, template_name="countries/css_main_page.html", context=render_context
    )


class NonceTable1(Table):
    class Meta:
        model = AnnualPopulation
        field = ("year", "population", "country_id")


def simple_table_without_explicit_style(request):
    generic_table = NonceTable1(AnnualPopulation.objects.all()[:45])
    render_context = {"table": generic_table}
    return render(
        request,
        template_name="countries/simple_table_without_explicit_style.html",
        context=render_context,
    )
