# coding = utf-8

from django.contrib import admin

from .models import Documento

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    pass