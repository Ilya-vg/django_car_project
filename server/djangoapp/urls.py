from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for home page
    path('', views.get_dealerships, name='index'),

    # path for about view
    path('about/', TemplateView.as_view(template_name="djangoapp/about.html"), name='about'),

    # path for contact us view
    path('contact/', TemplateView.as_view(template_name="djangoapp/contact.html"), name='contact'),

    # path for registration
    path('signup/', views.registration_request, name='signup'),
    # path for login
    path('login/', views.login_request, name='login'),
    # path for logout
    path('logout_request/', views.logout_request, name='logout'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)