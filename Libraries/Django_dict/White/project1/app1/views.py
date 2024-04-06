from django.shortcuts import render
from app1.models import SalesOrder
from rest_framework.viewsets import ModelViewSet
from app1.serializers import OrderSerializer

# Create your views here.
def order_page(request):
    return render( request, 'index.html', {'orders': SalesOrder.objects.all()} )


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer
    
    
def order(request):
    return render( request, 'main.html')
