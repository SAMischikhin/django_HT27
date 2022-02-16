from django.urls import path

from ads import views



urlpatterns = [
    path("", views.Index.as_view()),
    path("test/", views.Test.as_view()),
    path('cat/',  views.ViewCat.as_view()),
    path('ad/',  views.ViewAd.as_view()),
    path('cat/<int:pk>/',  views.CatDetailView.as_view()),
    path('ad/<int:pk>/',  views.AdDetailView.as_view()),
    ]