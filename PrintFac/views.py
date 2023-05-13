from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import PyPDF2 
import page_counter
from .models import Document
from .forms import DocumentForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Document
from .forms import DocumentForm
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.conf import settings

def FileUploadView(request):
    context={}
    if request.method == 'POST':
        file = request.FILES['file']
        name=request.POST['name']
        description=request.POST['description']
        color=request.POST['print_color']
        reader = PyPDF2.PdfReader(file)
        NumPages= len(reader.pages) 
        if color=="color":
            amount=1.5*NumPages
        else:
            amount=5*NumPages

        # Creating Payment uisng Razorpay
        client=razorpay.Client(auth=(settings.KEY,settings.SECRET))
        payment=client.order.create({'amount':100*amount,'currency':'INR','payment_capture':1})
        docs=Document.objects.create(
            name=name,
            document=file,
            description=description,
            print_color=color,
            amount=amount,
            razorpay_order_id=payment['id']
        )
        docs.save()
        context={
            'payment':payment,
        }
    return render(request, 'templates/UploadFile.html',context)

@csrf_exempt
def HandleSuccess(request):
    context={}
    order_id=request.GET.get('order_id')
    docs=Document.objects.get(razorpay_order_id=order_id)
    response=request.POST
    print(response['razorpay_order_id'])
    param_dict={
        'razorpay_payment_id':order_id
    #     'razorpay_order_id':response['razorpay_order_id'],
    #     'razorpay_signature':response['razorpay_signature'],
    }
    print(param_dict)
    client=razorpay.Client(auth=(settings.KEY,settings.SECRET))
    # try:
    #     status=client.utility.verify_payment_signature(param_dict)
    #     docs=Document.objects.get(razorpay_order_id=response['razorpay_order_id'])
    #     docs.razorpay_payment_id=response['razorpay_payment_id']
    #     docs.is_paid=True
    #     docs.save()
    context={
        'name':docs.name,
        'paid':docs.is_paid,
        'amount':docs.amount,
        'transaction_id':docs.razorpay_order_id,
        'description':docs.description,
        'print_color':docs.print_color,
        # 'status':status
        }
    return render(request,"templates/success.html",context)
    # except:
    #     return render(request,"templates/success.html",context)


# class DocumentCreateView(CreateView):
#     model = Document
#     form_class = DocumentForm
#     template_name = 'UploadFile.html'
#     success_url = reverse_lazy('document')
    
#     def post(self, request,*args,**kwargs):
#         docs=Document.objects.all()
#         form=self.get_form()
#         if form.is_valid():
#             file=request.FILES['document']
#             reader = PyPDF2.PdfReader(file)
#             # NumPages = page_counter.page_count(file)
#             NumPages= len(reader.pages) 
#             print(NumPages)
#             form.save()
#         client=razorpay.Client(auth=(settings.KEY,settings.SECRET))
#         payment=client.order.create({'amount':1000,'currency':'INR','payment_capture':1})
#         print(payment)
#         rpay=Document.objects.create(
#             razorpay_order_id=payment['id'],
#             razorpay_payment_id="smple",
#             razorpay_payment_signature="sample"
#             )
#         rpay.save()
#         context={'items':docs,'payment':payment}
#         return render(request, "templates/UploadFile.html",context=context)
