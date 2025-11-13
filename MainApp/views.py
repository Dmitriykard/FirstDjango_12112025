from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]

def home(request)-> HttpResponse:
    context = {
        "name": "Иванов Иван Николаевич",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    author = {
        "name": "Николай",
        "middle_name": "Иванович",
        "last_name": "Сидоров",
        "phone": "8-914-800-20-30",
        "email": "kolya_sidr@mail.ru",
    } 
    context = {
        'author': author,
    }
    return render(request, "about.html", context)

def get_item(request, item_id: int):
    """По указанному id возвращает элемент из списка"""
    for item in items:
        if item["id"] == item_id:
            context = {
                "item": item
            }
            return render(request, "item_page.html", context)
    return render(request, "errors.html", {'errors': [f'Item with id={item_id} not found']})

def get_items(request):
    context = {"items": items}
    return render(request, "items_list.html", context)


        
    
    
