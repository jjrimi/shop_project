from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, FileResponse
from .models import Product
from django.conf import settings
from django.db import connection
from io import BytesIO
import base64
from django.http import JsonResponse

def index(request):
    products = Product.objects.all()
    for product in products:
        product.image_base64 = product.get_image_base64()
    return render(request, 'index.html', {'products': products})

def get_products_by_category(request):
    category_param = request.GET.get('category', '')
    if category_param and category_param != 'All Products':
        products = Product.objects.filter(category=category_param)
    else:
        products = Product.objects.all()

    product_list = []
    for product in products:
        product_dict = {
            'id': product.id,
            'category': product.category,
            'name': product.name,
            'price': product.price,
            'image_base64': product.get_image_base64(),
        }
        product_list.append(product_dict)

    return JsonResponse(product_list, safe=False)

def category(request):
    category_param = request.GET.get('category')
    if category_param:
        # 해당 카테고리에 속하는 상품들을 가져옴
        products = Product.objects.filter(category=category_param)
    else:
        # 모든 상품들을 가져옴
        products = Product.objects.all()

    for product in products:
        product.image_base64 = product.get_image_base64()

    return render(request, 'category.html', {'products': products, 'category': category_param})

def read(request, id):
    return HttpResponse('Read!'+id)

def create_product(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        if category and name and price and image:
            # 모델을 사용하여 데이터 생성
            Product.objects.create(
                category=category,
                name=name,
                price=price,
                image=image.read()  # 이미지를 바이너리 형태로 저장
            )
            return HttpResponse('Success')
        else:
            return HttpResponse('내용을 빠짐없이 입력하세요!')
    else:
        return render(request, 'create_product.html')

