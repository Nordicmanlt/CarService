# Create your models here.
from django.db import models


class CarModel(models.Model):
    car_name = models.CharField(verbose_name='Car Manufacturer', max_length=50, help_text='Įveskite automobilio gamintojo pavadinimą',
                                null=False)
    car_model = models.CharField(verbose_name='Model', max_length=50, help_text='Įveskite automobilio modelio pavadinimą',
                                 null=False)

    def __str__(self):
        return f'{self.car_name}, {self.car_model}'

    class Meta:
        verbose_name = 'Car model'
        verbose_name_plural = 'Car models'


class Automobile(models.Model):
    car_plate = models.CharField(verbose_name="Plate number",  max_length=10, unique=True, null=False)
    car_model = models.ForeignKey('CarModel', on_delete=models.DO_NOTHING)  # kaip čia su True daryti?
    vin_code = models.CharField(verbose_name='VIN number', max_length=17, help_text='Automobile VIN code', unique=True, null=False)
    customer = models.CharField(verbose_name='Customer', max_length=30, help_text='Customer Name Surname (or Company Name)')

    def __str__(self):
        return f'{self.car_plate}, {self.car_model}, {self.vin_code}, {self.customer}'

    class Meta:
        verbose_name = 'Automobile'
        verbose_name_plural = 'Automobiles'


class Order(models.Model):
    order_date = models.DateField('Order date', null=False)
    car = models.ForeignKey('Automobile', on_delete=models.DO_NOTHING)

    LOAN_STATUS = (
        ('n', 'New'),
        ('i', 'In progress'),
        ('d', 'Works Done'),
        ('c', 'Closed'),
    )

    order_status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='n',
        help_text='Order Status',
    )

    class Meta:
        ordering = ['-order_status', "order_date"]
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.order_date}, {self.order_status}, {self.car}'



class ServiceOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.DO_NOTHING)
    service = models.ForeignKey('Service', on_delete=models.DO_NOTHING)
    qty = models.DecimalField('Qty.', max_digits=12, decimal_places=1, null=False)

    LOAN_STATUS = (
        ('1', 'Not Started'),
        ('2', 'Planned'),
        ('3', 'In progress'),
        ('4', 'Blocked'),
        ('5', 'Done'),
    )

    service_status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='1',
        help_text='Service Status',
    )


    def __str__(self):
        return f'{self.order}, {self.service}, {self.qty}, {self.service_status}'

    class Meta:
        ordering = ['order__order_date', 'service_status']
        verbose_name = 'Service order'
        verbose_name_plural = 'Service orders'


class Service(models.Model):
    service_name = models.CharField('Service name', max_length=200, null=False)
    service_price = models.DecimalField('Service price', max_digits=12, decimal_places=2, null=False)

    def __str__(self):
        return f'{self.service_name}, {self.service_price}'

    class Meta:
        ordering = ['service_name']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
