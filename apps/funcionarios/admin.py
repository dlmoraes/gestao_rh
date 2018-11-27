# coding = utf-8

from django.contrib import admin

from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass