from django.contrib import admin
from . models import Product,Customer,Cart,Wishlist,Payment,OrderPlaced
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category',' product_image']

admin.site.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','localiy','city','state','zipcode']

admin.site.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

admin.site.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

admin.site.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity',' ordered_data','stauts','payment']



admin.site.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']



admin.site.unregister(Group)

