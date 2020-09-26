"""Spoken_English_Point URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from Main.views import Homepage, Contact, Gallery, Blog, News_view, Add_News, Contacted_Mail, Delete_News, Delete_Mails, Delete_Demo_users
from Authentication.views import Login, Logout, Register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage, name='home'),
    path('contact/', Contact, name='contact'),
    path('contacted/', Contacted_Mail, name='contacted'),
    path('gallery/', Gallery, name='gallery'),
    path('blogs/', Blog, name='blog'),
    path('news/', News_view, name='news'),
    path('addnews/', Add_News, name='addnews'),
    path('deletenews/<int:id>', Delete_News, name='delete'),
    path('deletemails/<int:id>', Delete_Mails, name='deletemail'),
    path('deletedemousers/<int:id>', Delete_Demo_users, name='deletedemousers'),

    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', Logout, name='logout')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'Main.views.error_404_view'