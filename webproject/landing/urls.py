from django.urls import path
from .views import homeview, about, blog, contact_view, horaires


app_name = 'landing'

urlpatterns = [
    path('', homeview,  name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', contact_view, name="contact"),
    path('horaires', horaires, name="horaires")

]
