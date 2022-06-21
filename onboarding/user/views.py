from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView, status

from .models import UserInfo
from .serializers import UserCreateSerializer, UserDetailSerializer, UserListSerializer, UserPutSerializer


# Create your views here.
class UserListView(APIView):
    def get(self, request):
        users = UserInfo.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request):
        serializer = UserListSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "success, create user"}, status.HTTP_200_OK)


class UserDetailListView(APIView):
    def get(self, request, user_id):
        user = UserInfo.objects.filter(id=user_id).first()
        serializer = UserDetailSerializer(user, many=False)

        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=UserPutSerializer,
    )
    def put(self, request, user_id):
        user = UserInfo.objects.filter(id=user_id).first()
        serializer = UserPutSerializer(user, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        serializer = UserDetailSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, user_id):
        user = get_object_or_404(UserInfo, pk=user_id)
        user.delete()
        return Response({"detail": "success, delete user"}, status.HTTP_200_OK)
