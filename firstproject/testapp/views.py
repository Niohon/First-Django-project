from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from testapp.models import Worker


def index_page(request):
    # new_worker = Worker(name="Виктория", second_name="Шевцвоа", salary=12000)
    # new_worker.save()

    # worker_to_change = Worker.objects.get(id=2)
    # worker_to_change.salary = 21000
    # worker_to_change.save()
    # worker_to_change.delete()

    all_workers = Worker.objects.all()
    workers_info = []
    for i in all_workers:
        print(f"Имя: {i.name} Фамилия: {i.second_name} Зарплата: {i.salary} ID: {i.id}")
        workers_info.append(f"Имя: {i.name} Фамилия: {i.second_name} Зарплата: {i.salary} ID: {i.id} ")

    if request.GET:
        print(request.GET)

    return render(request, 'index.html', context={'data': workers_info})


def numbers(request, testid):
    return HttpResponse(f"<h1>Год рождения: </h1><p>{testid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
