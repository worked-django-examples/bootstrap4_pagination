from django_tables2 import tables


from countries import models as country_models

class Bootstrap4_example1_with_template_table(tables.Table):
    class Meta:
        model = country_models.Country
        attrs = {"class": "table table-hover"}
        template_name = "django_tables2/bootstrap4.html"

class Bootstrap4_example1_no_template_table(tables.Table):
    class Meta:
        model = country_models.Country
        attrs = {"class": "table table-hover"}





