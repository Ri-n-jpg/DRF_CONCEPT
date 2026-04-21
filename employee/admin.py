from django.contrib import admin
from employee.models import Company, Employee


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'name', 'location', 'type', 'active')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'position', 'company')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)