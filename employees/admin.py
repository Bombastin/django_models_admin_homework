from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from workplaces.models import Workplace

from .models import Employee, EmployeeSkill, Skill


class EmployeeSkillInline(admin.TabularInline):
    model = EmployeeSkill
    extra = 1


class WorkplaceInline(admin.StackedInline):
    model = Workplace
    extra = 0
    max_num = 1


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    model = Employee

    list_display = (
        "username",
        "last_name",
        "first_name",
        "patronymic",
        "gender",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "gender",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "patronymic",
        "description",
    )
    ordering = (
        "last_name",
        "first_name",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Дополнительная информация о сотруднике",
            {
                "fields": (
                    "gender",
                    "patronymic",
                    "description",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Дополнительная информация о сотруднике",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "patronymic",
                    "gender",
                    "description",
                )
            },
        ),
    )

    inlines = (
        EmployeeSkillInline,
        WorkplaceInline,
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(EmployeeSkill)
class EmployeeSkillAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "skill",
        "level",
    )
    list_filter = ("skill",)
    search_fields = (
        "employee__username",
        "employee__first_name",
        "employee__last_name",
        "skill__name",
    )
