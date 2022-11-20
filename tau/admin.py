from django.contrib import admin
from .models import Student, Class

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ['student_id']

    def student_id(self, obj):
        return obj.id
    
class CLassAdmin(admin.ModelAdmin):
    readonly_fields = ['class_id']

    def class_id(self, obj):
        return obj.id


    
admin.site.register(Student, StudentAdmin)
admin.site.register(Class, CLassAdmin)