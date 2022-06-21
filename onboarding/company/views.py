from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView, status
from company.models import Company, JopPosting
from company.serializers import (
    CompanyCreateSerializer,
    CompanyDetailSerializer,
    CompanyListSerializer,
    CompanyPutSerializer,
    CompanySerializer,
    JopPostingSerializer,
)

# Create your views here.
class CompanyListView(APIView):
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanyListSerializer(companies, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CompanyCreateSerializer,
    )
    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "success, create company"}, status.HTTP_200_OK)


class CompanyDetailListView(APIView):
    def get(self, request, company_id, format=None):
        company = Company.objects.filter(id=company_id).first()
        serializer = CompanyDetailSerializer(company, many=False)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CompanyPutSerializer,
    )
    def put(self, request, company_id, format=None):
        company = Company.objects.filter(id=company_id).first()
        serializer = CompanyPutSerializer(company, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "success, create company"}, status.HTTP_200_OK)

    def delete(self, request, company_id, format=None):
        company = get_object_or_404(Company, pk=company_id)
        company.delete()
        return Response({"detail": "success, delete company"}, status.HTTP_200_OK)
