from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from products.views import  products, basket_add, basket_del

app_name = 'products'

urlpatterns = [
    path('',products,name = 'index'),
    path('<int:category_id>', products, name='category'),
    path('page/<int:page>', products, name='page'),
    path('basket-add/<int:product_id>/',basket_add,name = 'basket-add'),
    path('basket-del/<int:id>/',basket_del,name = 'basket-del'),
]

#if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)