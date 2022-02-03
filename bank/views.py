from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from datetime import datetime
# Create your views here.

def index(request):
    customers=CustomerDetails.objects.all()
    return render(request,'index.html',{'customers':customers})
def transaction(request):
    customers = CustomerDetails.objects.all()
    if request.method=='POST':
        print("yes1")
        semail=request.POST['semail']
        remail=request.POST['remail']
        amount_tobe=request.POST['amount']
        amount_tobe=int(amount_tobe)

        for recievers in customers:
            if recievers.email==remail:
                reciever=recievers
                rid=recievers.id
                print("yes2")
                break
        for sender in customers:
            # print(sender.email,sen)
            if sender.email==semail and sender.amount>amount_tobe and amount_tobe>0 and sender.email!=reciever.email:
                sid=sender.id
                newamount_sender = sender.amount - amount_tobe
                newamount_reciever = reciever.amount + amount_tobe
                print("yes3")

                try:
                    x = datetime.now()
                    x=str(x)
                    sql1= CustomerDetails(id=sid,email=sender.email,name=sender.name,amount=newamount_sender)
                    sql2= CustomerDetails(id=rid,email=reciever.email,name=reciever.name,amount=newamount_reciever)

                    sql3 = TransactionDetails(sender_data=sender.email, receiver_data=reciever.email,
                                              amount_data=amount_tobe,date=x)
                    sql2.save()
                    sql1.save()
                    sql3.save()
                    print("yes4")


                    return redirect('/')

                except:
                    print("yes5")
                    return HttpResponse("Transfer Failed!!")
        else:
            print("yes6")
            return HttpResponse("Invalid Input")
    print("yes7")
    return render(request,'index.html',{"customers":customers})
def transaction_details(request):
    transact= TransactionDetails.objects.all()
    return render(request,"transactiondetails.html",{'transact':transact})