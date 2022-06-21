from company.serializers import JopPostingSerializer
from rest_framework import serializers

from user.models import ApplyPosting, Position, UserInfo


class ApplyPostingSerializer(serializers.ModelSerializer):
    posting = JopPostingSerializer()

    class Meta:
        model = ApplyPosting
        exclude = ("updated_at", "created_at", "user", "id")


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ("id", "username", "email")


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ("username", "email", "position")


class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ("position",)


class UserDetailSerializer(serializers.ModelSerializer):
    aplly_posting = ApplyPostingSerializer(source="apply_posting", many=True)

    class Meta:
        model = UserInfo
        exclude = ("updated_at", "created_at")
