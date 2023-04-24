from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from testapp.models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index_page(request):
    # new_worker = Worker(name="Виктория", second_name="Шевцвоа", salary=12000)
    # new_worker.save()

    # worker_to_change = Worker.objects.get(id=2)
    # worker_to_change.salary = 21000
    # worker_to_change.save()
    # worker_to_change.delete()

    posts = Women.objects.all()

    if request.GET:
        print(request.GET)

    return render(request, 'testapp/index.html', context={'title': 'Главнвя страница',
                                                          'menu': menu,
                                                          'posts': posts})


def numbers(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Год рождения: </h1><p>{year}</p>")


def delete_all_workers(request):
    all_workers = Worker.objects.all()
    deleted_workers = []
    for i in all_workers:
        print(f"Имя: {i.name} Фамилия: {i.second_name} Зарплата: {i.salary} ID: {i.id} был удалён")
        deleted_workers.append(f"{i.id}. {i.name} {i.second_name}")
        i.delete()
        # worker_to_delete.delete()

    return render(request, 'testapp/deleted.html', context={'title': 'Удалить всех работников', 'data': deleted_workers})

def about(request):
    return render(request, 'testapp/about.html', context={'title': 'about'})

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

