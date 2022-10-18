from django.contrib import admin
from django.urls import path, include
from produtos.views import ProdutosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produtos', ProdutosViewSet, basename='Produtos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]