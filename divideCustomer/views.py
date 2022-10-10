from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'divideCustomer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'divideCustomer/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'divideCustomer/order.html')

class Dining(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'divideCustomer/dining.html')