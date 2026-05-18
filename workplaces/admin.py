from django.contrib import admin

from .models import Workplace


@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    list_display = (
        "desk_number",
        "employee",
        "additional_info",
    )
    search_fields = (
        "desk_number",
        "employee__username",
        "employee__first_name",
        "employee__last_name",
        "additional_info",
    )
    list_filter = ("employee__gender",)
