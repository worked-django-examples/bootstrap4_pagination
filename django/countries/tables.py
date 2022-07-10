# these classes are used almost entirely in in views, so you
# could define them in views.py.

# tables rely almost always on models.  Frequently, tables specify templates in
# their meta.

# temp

import django_tables2 as t2

from .models import Country

class Bootstrap4CountryCodesTable(t2.Table):
    # no fields, so the table will include all the columns in
    # the table.  There are only 2.
    class Meta:
        model = Country
        attrs = {"class": "table table-hover"}
        template_name = "django_tables2/bootstrap4.html"