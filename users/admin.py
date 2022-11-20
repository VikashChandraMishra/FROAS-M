from django.contrib import admin
from .models import Teacher, Department


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ['teacher_id']

    def teacher_id(self, obj):
        return obj.id

    
class DepartmentAdmin(admin.ModelAdmin):
    readonly_fields = ['department_id']

    def department_id(self, obj):
        return obj.id

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Department, DepartmentAdmin)
