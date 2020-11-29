from django.contrib import admin
from . import models
admin.site.site_header='Hostel Management'

class form_ajaxAdmin(admin.ModelAdmin):
    list_display    = ['member_name']
    search_fields   = ['member_name']
    list_filter     = ['status',]

class advance_form_ajaxAdmin(admin.ModelAdmin):
    list_display    = ['member_name']
    search_fields   = ['member_name']
    list_filter     = ['status',]

class form_ajax_tableAdmin(admin.ModelAdmin):
    list_display    = ['member_name']
    search_fields   = ['member_name']
    list_filter     = ['status',]

class advance_form_ajax_tableAdmin(admin.ModelAdmin):
    list_display    = ['member_name']
    search_fields   = ['member_name']
    list_filter     = ['status',]
admin.site.register(models.form_ajax,form_ajaxAdmin)
admin.site.register(models.advance_form_ajax,advance_form_ajaxAdmin)
admin.site.register(models.form_ajax_table,form_ajax_tableAdmin)
admin.site.register(models.advance_form_ajax_table,advance_form_ajax_tableAdmin)























