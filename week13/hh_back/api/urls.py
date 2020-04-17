from django.urls import path

# from api.views import companies_list, companies_detail, company_vacancies, vacancies_list, vacancies_detail,\
#     vacancies_top
from api.views.views_cbv import CompanyListAPIView, CompanyDetailAPIView, CompanyVacanciesListAPIView, \
    VacancyListAPIView, VacancyDetailAPIView, TopVacanciesListAPIView
from api.views.views_generic_v1 import CompanyListAPIView, CompanyDetailAPIView, CompanyVacanciesAPIView
from api.views.views_generic import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView, VacancyDetailAPIView,\
    CompanyWithVacanciesListAPIView, TopVacanciesListAPIView
# from api.views.views_generic CompanyVacanciesListAPIView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # path('companies/', companies_list),
    # path('companies/<int:company_id>/', companies_detail),
    # path('companies/<int:company_id>/vacancies/', company_vacancies),
    # path('vacancies/', vacancies_list),
    # path('vacancies/<int:vacancy_id>/', vacancies_detail),
    # path('vacancies/top_ten/', vacancies_top)
    path('login/', obtain_jwt_token),

    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),

    # path('companies/<int:pk>/vacancies/', CompanyVacanciesAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/', CompanyVacanciesListAPIView.as_view()),

    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten/', TopVacanciesListAPIView.as_view())
]