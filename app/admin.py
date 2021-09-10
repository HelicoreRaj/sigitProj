from django.contrib import admin
from .models import CSVMaster

# Register your models here.

ModelField= lambda model: type('Subclass'+model.__name__,(admin.ModelAdmin,),{
	'list_display':[x.name for x in model._meta.fields],	
})

admin.site.register(CSVMaster,ModelField(CSVMaster))