from django.urls import path

# /api/companies - List of all Companies
# /api/companies/<int:id>/ - Get one Company
# /api/companies/<int:id>/vacancies/ - List of Vacancies by Company
# /api/vacancies/ - List of all Vacancies
# /api/vacancies/<int:id>/ - Get one Vacancy
# /api/vacancies/top_ten/ - List of top 10 vacancies sorted by decreasing salary
from api.views import companies_list, companies_detail, company_vacancies, vacancies_list, vacancies_detail,\
    vacancies_top

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:id>/', companies_detail),
    path('companies/<int:id>/vacancies/', company_vacancies),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:id>/', vacancies_detail),
    path('companies/top_ten/', vacancies_top)
]