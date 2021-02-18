from django.shortcuts import render, HttpResponse, redirect
from .models import User, Book, Borrower
from datetime import date
from dateutil.relativedelta import relativedelta
# dict_var = {}
# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        try:
            name = request.POST['name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            return HttpResponse('Error 404')
        obj = User.objects.all()
        for i in obj:
            if i.username == username:
                return HttpResponse('Username taken')
        obj1 = User()
        obj1.username = username
        obj1.name = name
        obj1.email = email
        obj1.password = password
        obj1.save()
        return redirect('/libmanage/login')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return HttpResponse('Error 404')
        obj = User.objects.all()
        for i in obj:
            if i.username == username and i.password == password:
                request.session['flag'] = 1
                request.session['user_id'] = i.id
                return redirect('/')
        return HttpResponse('Invalid username/password')


def book(request):
    list_var = []
    obj = Book.objects.all()
    for i in obj:
        # flag3 = dict_var[i.id]
        list_var.append([i.id, i.bname, i.author, i.yop, i.status])
    if len(list_var) == 0:
        flag1 = 1
    else:
        flag1 = 0
    return render(request, 'book.html', {'l1': list_var, 'flag1' : flag1})




def bupdate(request, book_id):
    if request.method == 'GET':
        return render(request, 'bupdate.html', {'book_id' : book_id})
    elif request.method == 'POST':
        obj = Book.objects.get(id=book_id)
        obj.bname = request.POST['bname']
        obj.author = request.POST['author']
        obj.yop = request.POST['yop']
        # obj.status = request.POST['status']
        obj.save()
        return redirect('/')

def bdelete(request, book_id):
    obj = Book.objects.get(id=book_id)
    obj.delete()
    return redirect('/')

def badd(request):
    # global dict_var
    if request.method == 'GET':
        return render(request, 'badd.html')
    elif request.method == 'POST':
        obj = Book()
        obj.bname = request.POST['bname']
        obj.author = request.POST['author']
        obj.yop = request.POST['yop']
        # obj.status = request.POST['status']
        obj.save()
        # dict_var[obj.id] = 0
        return redirect('/')


def borrower(request):
    list_var = []
    obj = Borrower.objects.all()
    for i in obj:
        if i.due >= date.today():
            fine = 0
        else:
            fine = (i.due - date.today()).days * 5
        list_var.append([i.bu_id, i.b_id, i.b_name, i.due, fine])
    if len(list_var) == 0:
        flag2 = 1
    else:
        flag2 = 0
    return render(request, 'borrower.html', {'l1': list_var, 'flag2': flag2})

def borroweradd(request, book_id):
    # global dict_var
    if request.session.get('flag', 0) == 1:
        obj = Borrower()
        obj.bu_id = request.session['user_id']
        obj.b_id = book_id
        obj1 = User.objects.get(id=int(request.session['user_id']))
        obj.b_name = obj1.name
        due = date.today() + relativedelta(months=1)
        obj.due = due
        obj.save()
        obj1 = Book.objects.get(id=book_id)
        obj1.status = 'Issued'
        # dict_var[book_id] = 1
        return redirect('/')
    else:
        return render(request, 'signup.html')


def borrowerdel(request, book_id):
    # global dict_var
    obj = Borrower.objects.get(bu_id=int(request.session['user_id']))
    # dict_var[book_id] = 0
    obj.delete()
    obj1 = Book.objects.get(id=book_id)
    obj1.status = 'Available'
    return redirect('/')


def logout(request):
    if request.session.get("flag", 0) == 1:
        del request.session["flag"]
        del request.session["user_id"]
    return redirect('/')




