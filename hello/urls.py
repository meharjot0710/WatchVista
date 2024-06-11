from django.contrib import admin
from django.urls import path
from hello.views import *

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('about/',about, name="about"),
    path('contact/',contact, name="contact"),
    path('shop/',shop, name="shop"),
    path('review/',review, name="review"),
    path('login/',login, name="login"),
    path('signup/', signup, name='signup'),
    path('adlogin/',adlogin, name="adlogin"),
    path('adsignup/', adsignup, name='adsignup'),
    path('homelog/', homelog, name='homelog'),
    path('aboutlog/', aboutlog, name='aboutlog'),
    path('contactlog/', contactlog, name='contactlog'),
    path('reviewlog/', testimoniallog, name='testimoniallog'),
    path('shoplog/', shoplog, name='shoplog'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('update_quantity/<int:item_id>/', update_quantity, name='update_quantity'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('list/', product_list, name='product_list'),
    path('feed/', adfeedback, name='adfeedback'),
    path('delete_feedback/<int:feedback_id>/', delete_feedback, name='delete_feedback'),
    path('remove_product/<int:product_id>/', remove_product, name='remove_product'),
    path('order/', order, name='order'),
    path('complete_order/', complete_order, name='complete_order')
]