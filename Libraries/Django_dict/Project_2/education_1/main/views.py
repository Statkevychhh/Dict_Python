from django.shortcuts import render
# from django.http import HttpResponse



def index(request):
    data = {
        'title': 'Головна сторінка',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 19,
            'hobby': 'footbal'
        }
        
    }
    return render(request, "main/index.html", data)

# def about(request):
#     return HttpResponse("<h4>Сторінка про нас<h4>")

def about(request):
    return render(request, "main/about.html")