from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","age","phone")
# Register your models here.
admin.site.register(Member,MemberAdmin)
