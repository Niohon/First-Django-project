# import sys
# from sys import path
# import pprint

# sys.path.remove('D:\\Python\\First django project\\venv\\lib\\site-packages')
# sys.path.append('D:\\Python\\First django project\\firstproject')
# pprint.pprint(sys.path)

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

    return render(request, 'index.html', context={'data': workers_info})
