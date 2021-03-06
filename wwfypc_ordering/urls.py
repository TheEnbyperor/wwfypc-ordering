"""wwfypc_ordering URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django_keycloak_auth.views import Login, Logout

admin.autodiscover()
admin.site.login = Login.as_view()
admin.site.logout = Logout.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("django_keycloak_auth.urls")),
    path("unlocking/", include("unlocking.urls")),
    path("video_conversion/", include("video_conversion.urls")),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

if settings.DEBUG:
    urlpatterns += static("static/", document_root=settings.STATIC_ROOT)
    urlpatterns += static("media/", document_root=settings.MEDIA_ROOT)
