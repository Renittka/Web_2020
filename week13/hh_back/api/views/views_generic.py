from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from api.models import Company, Vacancy
from api.serializers import CompanySerializer2, VacancySerializer, CompanyWithVacanciesSerializer


class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2
    # permission_classes = (IsAuthenticated, )


class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2


class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class CompanyWithVacanciesListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyWithVacanciesSerializer


class CompanyVacanciesListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    lookup_url_kwarg = 'company_id'

    # def get_queryset(self):
    #     company = self.request.Company
    #     return company.vacancies.all()
    
    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = VacancySerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def get_object(self, company_id=):
    #     queryset = self.get_queryset()
    #     filter = {}
    #     for field in self.multiple_lookup_fields:
    #         filter[company_id] = self.kwargs[field]
    #
    #     obj = get_object_or_404(queryset, **filter)
    #     self.check_object_permissions(self.request, obj)
    #     return obj


class TopVacanciesListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.order_by('-salary')[:10]
    serializer_class = VacancySerializer
