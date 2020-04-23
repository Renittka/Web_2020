
from django_filters import rest_framework as filters

from api.models import Vacancy


class VacancyFilter(filters.FilterSet):
    # Product.objects.filter(name__contains=name)
    company_id = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Vacancy
        fields = ('name', 'salary', 'company_id')