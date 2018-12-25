from django.shortcuts import render, reverse
import emails.views
from textblob.classifiers import NaiveBayesClassifier


def analysis(request):
    id = request.session['empid2']
    rev = reverse('crm:dashboard', kwargs={'id': id})
    rev1 = reverse('g_customers', kwargs={'id': id})
    train = [
        ('I loved this product', 'pos'),
        ('this product is not working properly !', 'neg'),
        ('thankyou for your support', 'pos'),
        ('this is my best product.', 'pos'),
        ('i did not like the product', 'neg'),
        ('I did not expect this from the product for this price', 'neg'),
        ('I am tired of this stuff', 'neg'),
        ("I can't deal with this", 'neg'),
        ('Customer care is not supportive', 'neg'),
        ("very happy with customer support", 'pos'),
    ]
    cl = NaiveBayesClassifier(train)
    val_pos=[]
    val_neg=[]
    message_body = emails.views.getAllMessages()
    message_list=[]

    for message in message_body:

        for m in message:
            message_list.append(m)

    for message in message_list:
        if (cl.classify(message)=='pos'):
            prob_dist_p = cl.prob_classify(message)
            temp=round(prob_dist_p.prob("pos"),2)
            val_pos.append(temp*100)


        else:
            prob_dist_n = cl.prob_classify(message)
            temp1 = round(prob_dist_n.prob("neg"), 2)
            val_neg.append(temp1*100)
    tot_pos=len(val_pos)
    tot_neg = len(val_neg)
    tot=tot_pos+tot_neg
    tot_pos=(tot_pos/tot)*100
    tot_neg = (tot_neg / tot) * 100

    return render(request,'sentimental.html',{
        'senti_val_p':val_pos,
        'senti_val_n':val_neg,
        'tot_pos':tot_pos,
        'tot_neg':tot_neg,
        'rev': rev,
        'rev1': rev1
    })