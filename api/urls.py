from django.urls import path, include
from product.views import ProductViewSet, CategoryViewSet, ReviewViewSet,ProductImageViewSet
from rest_framework_nested import routers
from order.views import CartViewSet,CartItemViewSet,OrderViewset

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet)
router.register('carts',CartViewSet, basename='cart')
router.register('orders',OrderViewset, basename='order')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product-review')
product_router.register('images', ProductImageViewSet,
                        basename='product-images')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]