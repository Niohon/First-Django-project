from django.shortcuts import render
from testapp.models import Worker

def index_page(request):

    all_workers = Worker.objects.all
    print(all_workers)

    return render(request, 'index.html')
