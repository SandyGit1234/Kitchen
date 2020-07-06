
from django.shortcuts import render
from MessyKitchen.forms import PostOrder
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.


def index(request):
    if request.method=='POST':
        print('Post')
        form=PostOrder(request.POST or None)
        if form.is_valid():
            order=form.cleaned_data['OrderDetails']
            name=form.cleaned_data['FirstName'] +' ' + form.cleaned_data['LastName']
            email=form.cleaned_data['Email']
            spicy=form.cleaned_data['Spice_Choice']
            subject='Thanks for placing order at Messy Kitchen'
            message='Hello ' + name +',' + '\n' + \
                    'You have placed following order at Messy Kitchen: '+\
                    '\n' + order +'\n' + 'with ' + spicy + ' spice level.'
            sender='MessyKitchen.DesiFood@Gmail.com'
            send_mail(subject,message,sender,[email,sender])
            context={'form':form,'name':name}
            #configure Session variable to access in Thank You Page
            request.session['message']=message
            return HttpResponseRedirect('ThankYou')
    else:

        form=PostOrder()
        context={'form':form}

    return render(request,'index.html',context)

def thanks(request):
    if request.method=='POST':
        return HttpResponseRedirect('/')
    else:
        try:
            message=request.session['message']
            #delete the session variable for next use
            del request.session['message']
        except:
            message='You have not placed any order.Go to Messy Kitchen to place order.'
        context={'message':message}
        return render(request,'ThankYou.html',context=context)
