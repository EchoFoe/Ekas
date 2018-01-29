from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class PrivacyPolicyAdmin(SummernoteModelAdmin):
    list_display = [field.name for field in PrivacyPolicy._meta.fields]
    class Meta:
        model = PrivacyPolicy
admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)

class BMKObjectsAdmin(SummernoteModelAdmin):
    list_display = [field.name for field in BMKObjects._meta.fields]
    class Meta:
        model = BMKObjects
admin.site.register(BMKObjects, BMKObjectsAdmin)

class EkspertizaObjectsAdmin(SummernoteModelAdmin):
    list_display = [field.name for field in EkspertizaObjects._meta.fields]
    class Meta:
        model = EkspertizaObjects
admin.site.register(EkspertizaObjects, EkspertizaObjectsAdmin)