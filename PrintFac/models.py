from django.db import models

COLOR_TYPE=(('clr','Color'),('blk','Black & White'))

class Document(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    description  = models.CharField(max_length = 255,blank=True)
    document  = models.FileField(upload_to='documents/')
    print_color=models.CharField(choices=COLOR_TYPE,default="Black & White",max_length=20)
    amount=models.IntegerField(null=True)
    razorpay_order_id=models.CharField(max_length=100,null=True,blank=True)
    razorpay_payment_id=models.CharField(max_length=100,null=True,blank=True)
    razorpay_payment_signature=models.CharField(max_length=100,null=True,blank=True)
    payment_date=models.DateTimeField(auto_now_add=True)
    is_paid=models.BooleanField(default=False)
    
 
    class Meta:
        ordering = ['payment_date']
     
    def __str__(self):
        return f"{self.name}"

