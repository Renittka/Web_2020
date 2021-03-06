from django.db.models import Count
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from api.models import Company, Vacancy
from django.http import JsonResponse


@csrf_exempt
def companies_list(request):
    if request.method == 'GET':
        try:
            companies = Company.objects.all()
        except Vacancy.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'Company post request'})
    elif request.method == 'PUT':
        return JsonResponse({'data': 'Company put request'})
    elif request.method == 'DELETE':
        return JsonResponse({'data': 'Company delete request'})


@csrf_exempt
def companies_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'POST':
        return JsonResponse({'data': 'Company post request'})
    elif request.method == 'PUT':
        return JsonResponse({'data': 'Company put request'})
    elif request.method == 'DELETE':
        return JsonResponse({'data': 'Company delete request'})


@csrf_exempt
def company_vacancies(request, company_id):
    if request.method == 'GET':
        try:
            vacancies = Vacancy.objects.filter(company_id=company_id)
        except Vacancy.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'Vacancy post request'})
    elif request.method == 'PUT':
        return JsonResponse({'data': 'Vacancy put request'})
    elif request.method == 'DELETE':
        return JsonResponse({'data': 'Vacancy delete request'})


@csrf_exempt
def vacancies_list(request):
    if request.method == 'GET':
        try:
            vacancies = Vacancy.objects.all()
        except Vacancy.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'Vacancy post request'})
    elif request.method == 'PUT':
        return JsonResponse({'data': 'Vacancy put request'})
    elif request.method == 'DELETE':
        return JsonResponse({'data': 'Vacancy delete request'})


@csrf_exempt
def vacancies_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    elif request.method == 'POST':
        return JsonResponse({'data': 'Vacancy post request'})
    elif request.method == 'PUT':
        return JsonResponse({'data': 'Vacancy put request'})
    elif request.method == 'DELETE':
        return JsonResponse({'data': 'Vacancy delete request'})


@csrf_exempt
def vacancies_top(request):
    vac_top = Vacancy.objects.order_by('-salary')[:10]
    vac_json = [vacancy.to_json() for vacancy in vac_top]
    if request.method == 'GET':
        return JsonResponse(vac_json, safe=False)

