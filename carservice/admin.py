from django.contrib import admin
from .models import CarModel, Automobile, Order, ServiceOrder, Service


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_model')


class OrderInstanceInline(admin.TabularInline):
    model = ServiceOrder
    search_fields = ('service_name',)
    extra = 1
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'car__car_plate', 'car__car_model__car_name', 'car__car_model__car_model', 'order_status')
    search_fields = ('order_date', 'order_status', 'car__car_plate', 'car__car_model__car_name', 'car__car_model__car_model')
    list_editable = ('order_status',)
    list_filter = ('order_status',)
    inlines = [OrderInstanceInline]

class AutomobileAdmin(admin.ModelAdmin):
    list_display = ('customer', 'car_model__car_name', 'car_model__car_model',
                    'car_plate', 'vin_code')
    list_filter = ('customer', 'car_model__car_name')
    search_fields = ('customer', 'car_model__car_name', 'car_model__car_model',
                     'car_plate', 'vin_code')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_price')
    search_fields = ('service_name',)
    search_help_text = 'Search by Service Name'


class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = (
    'order__order_date', 'service__service_name', 'qty', 'order__car__car_plate', 'order__car__car_model__car_name',
    'order__car__car_model__car_model', 'service_status')
    search_fields = (
    'order__order_date', 'qty', 'order__car__car_plate', 'service__service_name', 'order__car__car_model__car_name',
    'order__car__car_model__car_model', 'service_status')
    list_editable = ('service_status',)
    list_filter = ('service_status',)


admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Automobile, AutomobileAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ServiceOrder, ServiceOrderAdmin)
admin.site.register(Service, ServiceAdmin)
