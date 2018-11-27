# coding = utf-8

from django.contrib import admin

from .models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    pass