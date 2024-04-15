from rest_framework import serializers

from apps.schedules.models import Lesson


class LessonSerializerForStudent(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'id',
            'date',
            'time',
        ]
