from django.contrib import admin

from .models import Customer, Service, Product


class CustomerList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'organization', 'role', 'email', 'bldgroom', 'address', 'account_number', 'city',
                     'state', 'zipcode', 'phone_number' )
    list_filter = ( 'cust_name', 'organization')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


class ServiceList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'service_category', 'description', 'location', 'setup_time',
                     'cleanup_time', 'service_charge')
    list_filter = ( 'cust_name', 'setup_time')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


class ProductList(admin.ModelAdmin):
    list_display = ( 'cust_name', 'product', 'p_description', 'quantity', 'pickup_time', 'charge')
    list_filter = ( 'cust_name', 'pickup_time')
    search_fields = ('cust_name', )
    ordering = ['cust_name']


admin.site.register(Customer, CustomerList)
admin.site.register(Service, ServiceList)
admin.site.register(Product, ProductList)
