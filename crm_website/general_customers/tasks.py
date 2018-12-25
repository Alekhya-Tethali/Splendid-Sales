from __future__ import print_function
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.template.loader import get_template
from . import send_email_from_api

from apiclient.discovery import build
from httplib2 import Http

from oauth2client.file import Storage
from general_customers.models import Customer,Registration,Resource
import datetime
import os
@periodic_task(run_every=(crontab(minute='*/1')), name="send_email_api", ignore_result=True)
def send_email_api():
    cwd_dir = os.getcwd()
    credential_dir = os.path.join(cwd_dir, '.credentials')
    credential_path = os.path.join(credential_dir, 'python-gmail-api.json')
    store = Storage(credential_path)
    credentials=store.get()
    service = build('gmail', 'v1', http=credentials.authorize(Http()))
    sendInst=send_email_from_api.send_email(service)
    expdate = datetime.date.today()+datetime.timedelta(days=2)
    customer_object = Customer.objects.filter(cexpiry=expdate)
    for customers in customer_object:
        customer_id=customers.cid
        resource_id=customers.rid
        usernameobj=Registration.objects.filter(cid=customer_id.cid)
        username=''
        resource=''
        cmail=''
        for users in usernameobj:
            username=users.firstname
            cmail=users.cemailid
        resourceobj=Resource.objects.filter(rid=resource_id.rid)
        for resources in resourceobj:
            resource=resources.rname
        expiry_date=customers.cexpiry
        purchase_date=customers.dop
        message=sendInst.create_message('crmwebsite2018@gmail.com',cmail,'Testmail',
                                        get_template('subscript_renew_automail.html').render(dict({'username':username,
                                                                                                    'expiry_date':expiry_date,
                                                                                                   'purchase_date': purchase_date,
                                                                                                   'resource':resource})))
        sendInst.send_message('me',message)


