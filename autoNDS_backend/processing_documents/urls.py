from django.urls import path
from .views import DocumentListView

urlpatterns = [
    path('api/documents/', DocumentListView.as_view(), name='document-list')
]