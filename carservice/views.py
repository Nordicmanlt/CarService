# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import CarModel, Automobile, Order, ServiceOrder, Service


def index(request):
    # Suskaičiuokime keletą pagrindinių objektų
    num_car_models = CarModel.objects.all().count()
    num_automobiles = Automobile.objects.all().count()
    num_orders = Order.objects.all().count()
    num_service_orders = ServiceOrder.objects.all().count()
    num_services = Service.objects.all().count()

    # Orders by status
    num_order_1 = Order.objects.filter(order_status__exact='n').count()
    num_order_2 = Order.objects.filter(order_status__exact='i').count()
    num_order_3 = Order.objects.filter(order_status__exact='d').count()
    num_order_4 = Order.objects.filter(order_status__exact='c').count()

    # Services by status
    num_service_status_1 = ServiceOrder.objects.filter(service_status__exact='1').count()
    num_service_status_2 = ServiceOrder.objects.filter(service_status__exact='2').count()
    num_service_status_3 = ServiceOrder.objects.filter(service_status__exact='3').count()
    num_service_status_4 = ServiceOrder.objects.filter(service_status__exact='4').count()
    num_service_status_5 = ServiceOrder.objects.filter(service_status__exact='5').count()


    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_car_models': num_car_models,
        'num_automobiles': num_automobiles,
        'num_orders': num_orders,
        'num_services': num_services,
        'num_service_orders': num_service_orders,
        'num_order_1': num_order_1,
        'num_order_2': num_order_2,
        'num_order_3': num_order_3,
        'num_order_4': num_order_4,
        'num_service_status_1': num_service_status_1,
        'num_service_status_2': num_service_status_2,
        'num_service_status_3': num_service_status_3,
        'num_service_status_4': num_service_status_4,
        'num_service_status_5': num_service_status_5,

    }

    # renderiname base.html, su duomenimis kintamąjame context
    return render(request, 'base.html', context=context)



# def services(request):
#     return render(request, 'services.html')