from rest_framework import serializers

from apps.students.models import Student
from apps.groups.models import Group


class StudentSerializer(serializers.ModelSerializer):
    """ Студент Сериализатор """
    class Meta:
        model = Student
        fields = [
            'id',
            'group',
            'username',
            'email',
            'full_name',
            'phone_number',
        ]


class StudentCreateSerializer(serializers.ModelSerializer):
    """ Создание Студента Сериализатор """
    password = serializers.CharField(
        write_only=True
    )
    class Meta:
        model = Student
        fields = [
            'username',
            'full_name',
            'group',
            'phone_number',
            'email',
            'password',
        ]

    def create(self, validated_data):
        password = validated_data['password']

        if not password:
            raise ValueError("Ошибка. Нет пароля")
        
        student = Student(**validated_data)
        student.set_password(password)
        student.save()

        return student


class GroupSerializer(serializers.ModelSerializer):
    """ Группа Сериализатор """
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = [
            'id',
            'title',
            'created_at',
            'students',
        ]
