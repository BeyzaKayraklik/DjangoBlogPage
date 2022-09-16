

from django.urls import path

from blog.views import add_blog
from blog.views import view_blog
from blog.views import update_blog
from blog.views import delete_blog
from blog.views import overview_blog


urlpatterns = [

    path('', overview_blog, name='overview-blog'),
    path('create/', add_blog, name='add-blog'),
    path('all/', view_blog, name='view-blog'),
    path("update/<int:pk>/", update_blog, name="update-blog"),
    path('item/<int:pk>/delete/', delete_blog, name='delete-blog'),
    path('item/<int:pk>/delete/', delete_blog, name='delete-blog'),

]

