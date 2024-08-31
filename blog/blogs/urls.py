from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    # Home page
    path('', views.index, name='home'),

    # Create new blog
    path('new_blog/', views.new_blog, name='new_blog'),
    
    # Edit blog
    path('edit_blog/<int:blog_id>', views.edit_blog, name='edit_blog')
]