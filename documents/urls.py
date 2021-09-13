from bridger.frontend import FrontendView
from bridger.routers import BridgerRouter
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import DocumentTypeViewSet, DocumentViewSet

router = BridgerRouter()
router.register(r"document", DocumentViewSet, basename="document")
router.register(r"type", DocumentTypeViewSet, basename="type")

urlpatterns = [
    path("", include(router.urls)),
    FrontendView.bundled_view("frontend/"),
    path("bridger/", include(("bridger.urls", "bridger"), namespace="bridger")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
