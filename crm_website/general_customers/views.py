from django.shortcuts import render, redirect, get_object_or_404
from general_customers.models import Visitors, Employee
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from general_customers.models import Registration, Customer, Resource

list=Visitors.objects.all()
name=[]
visitor=[]
time=[]

for v in list:
     name.append(v.product)
     visitor.append(v.visitors)
     time.append(v.avg_time)


@login_required
def g_customers(request,id):
    id = request.session['empid2']

    rev = reverse('crm:dashboard', kwargs={'id': id})
    rev1 = reverse('g_customers', kwargs={'id': id})

    a = Customer.objects.filter(eid=id)

    b = Registration.objects.all()
    oldc = []
    newc = []
    newcid=[]
    for old in a:
        oldc.append(old.cid.cid)

    for new in b:
        if new.cid not in oldc:
            newc.append(new.firstname)
            newcid.append(new.cid)

    b = len(newcid)
    for i in range(0, b):
        if newc[i] in request.GET:
            temp=Registration.objects.filter(cid=newcid[i])
            temp2 = Employee.objects.filter(eid=id)
            a = Customer(cid=temp[0], eid=temp2[0], status='pending')
            a.save()
    a = Customer.objects.filter(eid=id)
    b = Registration.objects.all()
    oldc = []
    newc = []
    newcid = []
    for old in a:
        oldc.append(old.cid.cid)

    for new in b:
        if new.cid not in oldc:
            newc.append(new.firstname)
            newcid.append(new.cid)
    list = Customer.objects.filter(eid=id)
    nameid = []
    for cust in list:
        nameid.append(cust.cid.firstname+" "+ cust.cid.lastname)
    tot_visitors=int(visitor[0])+int(visitor[1])+int(visitor[2])+int(visitor[3])+int(visitor[4])

    return render(request, 'general_customer.html', {
        'name0': name[0],
        'visitor0': visitor[0],
        'time0': time[0],
        'name1': name[1],
        'visitor1': visitor[1],
        'time1': time[1],
        'name2': name[2],
        'visitor2': visitor[2],
        'time2': time[2],
        'name3': name[3],
        'visitor3': visitor[3],
        'time3': time[3],
        'name4': name[4],
        'visitor4': visitor[4],
        'time4': time[4],
        'id': id,
        'rev1': rev1,
        'rev': rev,
        'tot_visitors':tot_visitors,
        'newc': newc,
        'nameid': nameid,
    })

def timeline(request):
    id = request.session['empid2']
    rev = reverse('crm:dashboard', kwargs={'id': id})
    rev1 = reverse('g_customers', kwargs={'id': id})
    a = User.objects.filter(pk=id)
    ename=a[0].username

    c = Customer.objects.all()
    for cust in c:
        n = cust.cid.firstname + " " + cust.cid.lastname
        if n in request.GET:
            name = request.GET[n]
            names=name.split(' ')
    details=Registration.objects.filter(firstname=names[0])
    mobile_no = details[0].phoneno
    email_id = details[0].cemailid
    location=details[0].loc
    cid=details[0].cid
    c=Customer.objects.filter(cid=cid,eid=id)
    rid=c[0].rid
    resource=rid.rname
    return render(request, 'timeline.html', {'name': name,
                                             'mobile_no':mobile_no,
                                            'email_id':email_id,
                                             'location':location,
                                             'rev': rev,
                                             'rev1': rev1,
                                             'ename': ename,
                                             'resource':resource
                                             })