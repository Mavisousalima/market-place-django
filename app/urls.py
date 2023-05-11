from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Marketplace",
        description="A marketplace for all products",
        default_version="1.0.0"
    )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',
        include([
            path('swagger/schema', schema_view.with_ui('swagger'), name="Swagger Schema"),
            path('products/', include(('product.urls', 'product'), namespace="product")),
            path('checkout/', include(('cart.urls', 'checkout'), namespace="checkout"))
        ])
    )
]
