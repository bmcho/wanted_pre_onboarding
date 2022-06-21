from rest_framework import serializers

from company.models import Company, JopPosting


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ("updated_at", "created_at")


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "companyname")


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("companyname", "country", "location")


class CompanyPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("country", "location")


class JopPostingListSerializer(serializers.Serializer):
    content = serializers.CharField()
    position = serializers.CharField()
    skill = serializers.CharField()

    class Meta:
        model = JopPosting


class CompanyDetailSerializer(serializers.ModelSerializer):
    posting = JopPostingListSerializer(many=True)

    class Meta:
        model = Company
        exclude = ("updated_at", "created_at")


class JopPostingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JopPosting
        fields = ("company", "position", "compensation", "content", "skill")


class JopPostingPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = JopPosting
        fields = ("position", "compensation", "content", "skill")


class JopPostingSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False)

    class Meta:
        model = JopPosting
        exclude = ("content", "updated_at", "created_at")


class JopPostingDetailSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False)

    class Meta:
        model = JopPosting
        exclude = ("updated_at", "created_at")
