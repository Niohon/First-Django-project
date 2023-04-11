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

    all_workers = Worker.objects.all()
    print(all_workers, "HI")

    return render(request, 'index.html')
