

# restaurant_app/urls.py
from django.urls import path
from .views import login_view, signup_view, products_view
from .views import home_view, about_view, contact_view, feedback_view

urlpatterns = [ 
    path('', home_view, name='home'),
    #path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('products/', products_view, name='products'),
    path('contact/', contact_view, name='contact'),
    path('feedback/', feedback_view, name='feedback'),
]

