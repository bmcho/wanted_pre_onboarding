from django.urls import path
from . import views


urlpatterns = [
    path("/companies", views.CompanyListView.as_view()),
    path("/companies/<int:company_id>", views.CompanyDetailListView.as_view()),
]
