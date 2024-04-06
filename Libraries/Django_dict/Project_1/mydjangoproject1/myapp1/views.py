from django.shortcuts import render
from myapp1.models import Worker

# Create your views here.
def index_page(request):
    all_workers = Worker.objects.all()
    # print(all_workers)
    
    workers_filtered = Worker.objects.filter(salary=60000)
    # print(workers_filtered)
    
    # for i in all_workers:
    #     print(f'Name: {i.name}, Second_name: {i.second_name}, Salary: {i.salary}, ID: {i.id}')
    
    
    
    # new_worker = Worker(name='Alena', second_name='Kovrigina', salary='27000')
    # new_worker.save()
    # Worker.objects.create(name='Ruslan', second_name='Statkevych', salary='18000')
    
    # worker_to_change = Worker.objects.get(id='3')
    # worker_to_change.salary = 13000
    # worker_to_change.save()
    # Worker.objects.filter(id='3').update(salary=13000)
    
    # Worker.objects.get(id=5).delete()
    
    return render(request, 'index.html', context={'data': all_workers})
