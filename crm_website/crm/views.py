from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.urls import reverse
from crm.forms import UserForm
from general_customers.models import Resource, Employee, Customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import View
import math

@login_required
def dashboard(request, id):
    id = request.session['empid2']
    rev = reverse('crm:dashboard', kwargs={'id': id})
    rev1 = reverse('g_customers', kwargs={'id': id})
    count = Customer.objects.filter(eid=id).count()
    emp_list = Employee.objects.filter(eid=id)
    for emp in emp_list:
        sales = emp.sales

    product = Resource.objects.all().count()

    ec2 = Customer.objects.filter(rid='aws001').count()
    quick_sight = Customer.objects.filter(rid='aws002').count()
    lambd = Customer.objects.filter(rid='aws003').count()
    s3 = Customer.objects.filter(rid='aws004').count()
    rds = Customer.objects.filter(rid='aws005').count()

    tot = ec2 + quick_sight + lambd + s3 + rds
    try:
     ec2 = math.floor((ec2 / tot) * 100)
    except ZeroDivisionError:
        ec2=0
    try:
     quick_sight = math.floor((quick_sight / tot) * 100)
    except ZeroDivisionError:
        quick_sight=0
    try:
     lambd = math.floor((lambd / tot) * 100)
    except ZeroDivisionError:
        lambd=0
    try:
     s3 = math.floor((s3 / tot) * 100)
    except ZeroDivisionError:
        s3=0
    try:
     rds = math.floor((rds / tot) * 100)
    except ZeroDivisionError:
        rds=0

    list = Customer.objects.filter(eid=id)
    nameid = []
    rids = []
    status = []

    for cust in list:
        nameid.append(cust.cid.firstname)
        status.append(cust.status)

    return render(request, 'dashboard.html', {
        'count': count,
        'sales': sales,
        'product': product,
        'ec2': ec2,
        'quick_sight': quick_sight,
        'lambd': lambd,
        's3': s3,
        'rds': rds,
        'list': list,
        #'nameid0': nameid[0],
        #'status0': status[0],
        #'nameid1': nameid[1],
        #'status1': status[1],
        'id': id,
        'rev': rev,
        'rev1': rev1
    })


def privacy(request):
    id = request.session['empid2']

    rev = reverse('crm:dashboard', kwargs={'id': id})
    rev1 = reverse('g_customers', kwargs={'id': id})
    return render(request, 'privacy.html',{
        'rev' : rev,
        'rev1': rev1

    })

class UserFormView(View):
    form_class = UserForm
    template_name = 'login-main.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        empid=''
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    a= User.objects.filter(username=username)
                    empid = a[0].id
                    request.session['empid2'] = empid
                    url = reverse('crm:dashboard', kwargs={'id': empid})

                    return HttpResponseRedirect(url)


