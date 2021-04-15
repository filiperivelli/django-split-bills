from django.contrib import admin
from split_bills_app.models import Bills, BillType, House, Invoices, Residents, Split

# Register your models here.
admin.site.register(Bills)
admin.site.register(BillType)
admin.site.register(House)
admin.site.register(Invoices)
admin.site.register(Residents)
admin.site.register(Split)
