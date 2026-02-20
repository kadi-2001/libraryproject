from django.http import HttpResponse
from django.shortcuts import render

def index(request): 
    return HttpResponse("Hello, world!") 

def index(request):
    name = request.GET.get("name") or "world!"
    return HttpResponse("Hello, " + name)


# =========================
# Task 4 + 5 (Template + Context) ✅
# =========================
def home(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})


# =========================
# Task 6 (index2 رقم) ✅
# =========================
def index2(request, val1):
    return HttpResponse(f"value1 = {val1}")


# =========================
# Task 6 (index2 نص - Error) ✅
# =========================
def index2_text(request):
    return HttpResponse("error, expected val1 to be integer")


# =========================
# Task 7 (عرض كتاب) ✅
# =========================
def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    return render(request, 'bookmodule/show.html', {'book': targetBook})
