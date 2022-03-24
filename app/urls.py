from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('find-me/', views.FindMeView.as_view(), name='find-me'),
    path('find-me/<str:slug>/', views.FindMePet.as_view(), name='find-me-pet'),
    path('pet/<str:slug>/', views.PetCV.as_view(), name='pet_cv'),
    path('create-cv/', views.Create_CV_View.as_view(), name='create_cv'),
    path('cvs/', views.All_CVs.as_view(), name='cvs'),
    path('create-find-me/', views.Create_Find_Me_View.as_view(),
         name='create_find_me'),
    path('results/<str:section>/<str:slug>/',
         views.showResults.as_view(), name='results'),
    path('results/',
         views.SearchResult.as_view(), name='result'),
]
