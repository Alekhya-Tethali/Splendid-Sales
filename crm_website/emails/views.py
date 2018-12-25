from django.shortcuts import render
import os
from django.contrib import messages
from general_customers import send_email_from_api
from django.core.paginator import Paginator
from apiclient.discovery import build
from oauth2client.file import Storage
from httplib2 import Http
from django.http import HttpResponseRedirect
from .forms import EmailForm
import base64
import email


'''Initialising variables for usage of Gmail API'''
cwd_dir = os.getcwd()
credential_dir = os.path.join(cwd_dir, '.credentials')
credential_path = os.path.join(credential_dir, 'python-gmail-api.json')
store = Storage(credential_path)
credentials = store.get()
service = build('gmail', 'v1', http=credentials.authorize(Http()))
inboxmessages=0

''' Retuns the UI for composing an email'''
def emailcompose(request):
    inboxmessagenumber()
    return render(request, 'emailcompose.html',{'inboxmessages':inboxmessages})


'''Sends email and returns back to the email composing UI'''
def sendmail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            to = form.cleaned_data['to']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            try:
                sendInst = send_email_from_api.send_email(service)
                message = sendInst.create_message('crmwebsite2018@gmail.com', to, subject, content)
                sendInst.send_message('me', message)
                messages.success(request, 'Mail sent successfully')
                return HttpResponseRedirect('/email/')
            except:
                messages.success(request, 'Error in sending mail.Please Check the email id.')
                return HttpResponseRedirect('/email/')
        else:
            messages.success(request, 'Error in sending mail.Please Check the mail format.')
            return HttpResponseRedirect('/email/')
    else:
        messages.success(request, 'There was an internal error.Please contact the administrator.')
        return HttpResponseRedirect('/email/')


'''Renders the  messages labelled as inbox on the UI in the form of pages'''
def readmail(request):
    no_mail_per_page=10
    messagefull=inboxmessagenumber()
    paginator = Paginator(messagefull, no_mail_per_page)
    page = request.GET.get('page')
    messagefullpage = paginator.get_page(page)
    return render(request, 'readmail.html',{'messagefull':messagefullpage,'inboxmessages':inboxmessages})


'''Renders email with the given message id '''
def emailread(request):
    inboxmessagenumber()
    message_id=request.GET['message_id']
    message_body=GetMessageString(service, 'me', message_id)
    messagefull=GetMessage(service, 'me', message_id)
    return render(request, 'emailread.html',{'message_body':message_body,'messagefull':messagefull,'inboxmessages':inboxmessages})


'''Reads a specific email with the given email message id without the detailed content'''
def GetMessage(service, user_id, msg_id):
     message = service.users().messages().get(userId=user_id, id=msg_id).execute()
     return message


'''Reads the content of the given email message id'''
def GetMessageString(service,user_id,msg_id):

    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()

    MessageBody = []
    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII')).decode('utf-8')
    mime_msg = email.message_from_string(msg_str)
    for parts in mime_msg.walk():
        mime_msg.get_payload()
        print(parts.get_content_type())
        if parts.get_content_type() == 'text/plain':
            myMSG =(parts.get_payload())
            MSG = myMSG.replace( '\r\n', '\n')
            MessageBody.append(MSG)
    return MessageBody


'''initialises number of messages in inbox by reading the entire mailbox'''
def inboxmessagenumber():
    response = service.users().messages().list(userId='me',
                                               labelIds=['INBOX']).execute()
    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])

    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId='me',
                                                   labelIds=['INBOX'],
                                                   pageToken=page_token).execute()
        messages.extend(response['messages'])
    messagefull = []
    for message in messages:
        messagefull.append(GetMessage(service,'me',message['id']))
    global inboxmessages
    inboxmessages=len(messagefull)
    return messagefull

def getAllMessages():
    response = service.users().messages().list(userId='me',
                                               labelIds=['INBOX']).execute()
    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])
    messagefull = []
    for message in messages:
        messagefull.append(GetMessageString(service, 'me', message['id']))
    return messagefull