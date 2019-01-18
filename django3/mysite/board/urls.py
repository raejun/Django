from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/board/
    path('', views.index),
    path('writeform', views.writeform),
    path('write', views.write),
    path('list', views.list),
    path('read/<int:post_id>', views.read),
    # path('updateform/<int:post_id>', views.updateform),
    # path('update', views.update),
    # path('deleteform/<int:post_id>', views.deleteform),
    # path('delete', views.delete),
]
