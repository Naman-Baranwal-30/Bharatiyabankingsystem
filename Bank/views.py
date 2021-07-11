from django.http import HttpResponse
from .models import details1,transcations
from django.template import loader
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

def showusers(request):
  objects1 = details1.objects.all()
  template = loader.get_template('banking1/selectuser.html')
  context = {
    'objects1': objects1
  }
  return HttpResponse(template.render(context, request))
def nameuser(request,name):
  objects2 = details1.objects.filter(name=name)
  objects3 = details1.objects.exclude(name=name)
  objects5 = details1.objects.values('bal').filter(name=name)
  template1 = loader.get_template('banking1/transaction.html')
  context1= {
    'objects3': objects3,
    'name': name,
    'objects2': objects2
  }
  return HttpResponse(template1.render(context1,request))
def insert1(request,name):
   objects5 = details1.objects.values('bal').filter(name=name)
   template12 = loader.get_template('banking1/transaction.html')
   context12 = {
       'objects5': objects5,
   }
   sender=request.POST["n"]
   receiver=request.POST.get("item_id",False)
   amt=(request.POST["number"])
   amount=int(amt);
   amt2=amount
   objects6 = details1.objects.values('bal').filter(name=receiver)
   initialbal2 = (objects6[0]['bal'])
  # initialbal2 = str(initialbal2)
   amt2=int(initialbal2)+amt2;
   initialbal1=(objects5[0]['bal'])
 #  initialbal1=str(initialbal1)
   amount=int(initialbal1)-amount;
   s1=details1.objects.filter(name=name).update(bal=amount);
  # s1.save();
   r1=details1.objects.filter(name=receiver).update(bal=amt2);
   a = transcations(sender=sender,receiver=receiver,amt=amt)
   a.save()
   messages.info(request, 'The Transaction was Completed Successfully from '+sender+' to '+receiver+' of the amount '+amt)
   template = loader.get_template('banking1/show.html')
   context = {
       'objects6': objects6
   }
   return HttpResponseRedirect('http://localhost:8000/transactions')


def showtransactions(request):
    objects4 = transcations.objects.all()
    template2 = loader.get_template('banking1/show.html')
    context2 = {
        'objects4': objects4
    }
    return HttpResponse(template2.render(context2, request))
