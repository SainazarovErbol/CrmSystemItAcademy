from django.contrib import admin

from apps.schedules.models import Schedule, Lesson


admin.site.register(Schedule)
admin.site.register(Lesson)
