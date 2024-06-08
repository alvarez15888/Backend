from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.CalculoRetrieveAPIView.as_view()),
    path('', views.CalculoListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.CalculoUpdateAPIView.as_view()),
    path('<int:pk>/destroy/', views.CalculoDestroyAPIView.as_view())

]
