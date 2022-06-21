from django.db.models import Q
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView, status

from company.models import Company, JopPosting
from company.serializers import (
    CompanyCreateSerializer,
    CompanyDetailSerializer,
    CompanyListSerializer,
    CompanyPutSerializer,
    CompanySerializer,
    JopPostingCreateSerializer,
    JopPostingDetailSerializer,
    JopPostingPutSerializer,
    JopPostingSerializer,
)


# Create your views here.
class CompanyListView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanyListSerializer(companies, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CompanyCreateSerializer,
    )
    def post(self, request):
        serializer = CompanySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "success, create company"}, status.HTTP_201_CREATED)


class CompanyDetailListView(APIView):
    def get(self, request, company_id):
        company = Company.objects.filter(id=company_id).first()
        serializer = CompanyDetailSerializer(company, many=False)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CompanyPutSerializer,
    )
    def put(self, request, company_id):
        company = Company.objects.filter(id=company_id).first()
        serializer = CompanyPutSerializer(company, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        serializer = CompanyDetailSerializer(company, many=False)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        company.delete()
        return Response({"detail": "success, delete company"}, status.HTTP_200_OK)


class JopPostingListView(APIView):

    company = openapi.Parameter(
        "company",
        openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
    )

    postion = openapi.Parameter(
        "postion",
        openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
    )

    skill = openapi.Parameter(
        "skill",
        openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(
        manual_parameters=[company, postion, skill],
    )
    def get(self, reqeust):
        company = reqeust.GET.get("company", None)
        postion = reqeust.GET.get("postion", None)
        skill = reqeust.GET.get("skill", None)

        q = Q()
        if company:
            q &= Q(company__companyname__contains=company)
        if postion:
            q &= Q(position=postion)
        if skill:
            q &= Q(skill__contains=skill)

        posting = JopPosting.objects.filter(q).all()
        serializer = JopPostingSerializer(posting, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=JopPostingCreateSerializer,
    )
    def post(self, request):
        serializer = JopPostingCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "success, create jop-posting"}, status.HTTP_201_CREATED)


class JopPostingDetailListView(APIView):
    def get(self, reqeust, posting_id):

        posting = JopPosting.objects.filter(id=posting_id).first()
        serializer = JopPostingDetailSerializer(posting, many=False)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=JopPostingPutSerializer,
    )
    def put(self, reqeust, posting_id):
        posting = JopPosting.objects.filter(id=posting_id).first()
        serializer = JopPostingDetailSerializer(posting, data=reqeust.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        serializer = JopPostingDetailSerializer(posting, many=False)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, posting_id):
        company = get_object_or_404(JopPosting, pk=posting_id)
        company.delete()
        return Response({"detail": "success, delete jop-posting"}, status.HTTP_200_OK)
