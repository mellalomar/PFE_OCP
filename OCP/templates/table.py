import django_tables2 as tables
from ..models  import Person,Info

class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "car1","car2","car3")

class InfoTable(tables.Table):
    class Meta:
        model = Info
        template_name = "django_tables2/bootstrap.html"
        fields = Info.Columns_name