from django.contrib import admin, messages
from .models import *


admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Department)
admin.site.register(Employee)
# admin.site.register(Courses)
admin.site.register(Students)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('crs_id', 'crs_name', 'crs_fee', 'isActive')
    list_display = ('id', 'name', 'fee', 'Active')

    def id(self, obj):
        return obj.crs_id

    def name(self, obj):
        return obj.crs_name

    def fee(self, obj):
        return obj.crs_fee

    def Active(self, obj):
        if obj.isActive:
            return 'Yes'
        else:
            return 'No'

    def make_active(self, req, q):
        q.update(isActive=True)
        messages.success(req, 'Course is Active..')

    def make_inactive(self, req, q):
        q.update(isActive=False)
        messages.success(req, 'Course is Inactive..')

    admin.site.add_action(make_active, 'Active the course')
    admin.site.add_action(make_inactive, 'Inactive the course')


admin.site.register(Courses, CoursesAdmin)
admin.site.site_header = 'My Admin'
admin.site.site_title = 'My Admin Panel'
admin.site.index_title = 'My Applications'
