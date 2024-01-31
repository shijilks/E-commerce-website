from django.urls import path 
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from.forms import LoginForm
from.forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordResetForm


urlpatterns = [
    
path('', views.home),
path('about/', views.about,name="about"),
path('contact/', views.contact,name="contact"),
path('category/<slug:val>', views.CategoryView.as_view(),name="category"),
path('category-title/<val>', views.CategoryTitle.as_view(),name="category-title"),
path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
path('profile/', views.ProfileView.as_view(),name="profile"),
path('address/', views.address,name="address"),
path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),

#add to cart
path('add-to-cart/', views.add_to_cart,name="add_to_cart"),
path('cart/', views.show_cart,name="showcart"),
path('checkout/', views.checkout.as_view(),name="checkout"),
path('paymentdone/', views.payment_done,name="paymentdone"),
path('orders/', views.Orders, name="orders"),



path('pluscart/', views.plus_cart),
path('minuscart/', views.minus_cart),
path('removecart/', views.remove_cart),
path('pluswishlist/', views.plus_wishlist),
path('minuswishlist/', views.minus_wishlist),

path('search/', views.search,name='search'),
path('wishlist/', views.show_wishlist,name='showwishlist'),



path('registration/', views.CustomerRegistrationView.as_view(),name="customerregistration"),
path('accounts/login/', auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm) ,name="login"),
path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone') ,name="passwordchange"),
path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html') ,name="passwordchangedone"),
path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm) ,name="password_reset"),

path('password-reset/done/', auth_view.PasswordResetView.as_view(template_name='password_reset_done.html',form_class=MyPasswordResetForm) ,name="password_reset_done"),

path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordResetForm) ,name="password_reset_confirm"),

path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html') ,name="password_reset_complete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header='MILMA DAIRY'
admin.site.site_title='MILMA DAIRY'
admin.site.site_index_title='Welcome to MILMA DAIRY Shop'