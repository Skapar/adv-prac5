from django.contrib import admin
from .models import Expense, Category

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):  
    list_display = ('description', 'amount', 'date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)