from django.urls import path
from . import views

urlpatterns = [
    path('lost/<int:pk>', views.LostRetrieveAPIView.as_view()),
    path('lost/', views.LostListCreateAPIView.as_view()),
    path('lost/<int:pk>/update', views.LostUpdateAPIView.as_view(), name='lost-edit'),
    path('lost/<int:pk>/destroy', views.LostDestroyAPIView.as_view()),
    path('found/<int:pk>', views.FoundRetrieveAPIView.as_view()),
    path('found/', views.FoundListCreateAPIView.as_view()),
    path('found/<int:pk>/update', views.FoundUpdateAPIView.as_view(), name='found-edit'),
    path('found/<int:pk>/destroy', views.FoundDestroyAPIView.as_view()),
]