from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dogs/', views.dogs_index, name='index'),
  path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
  path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
  path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
  path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
  path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('dogs/<int:dog_id>/assoc_swag/<int:swag_id>/', views.assoc_swag, name='assoc_swag'),
  path('dogs/<int:dog_id>/unassoc_swag/<int:swag_id>/', views.unassoc_swag, name='unassoc_swag'),
  path('swags/', views.SwagsList.as_view(), name='swags_index'),
  path('swags/<int:pk>/', views.SwagsDetail.as_view(), name='swags_detail'),
  path('swags/create/', views.SwagsCreate.as_view(), name='swags_create'),
  path('swags/<int:pk>/update/', views.SwagsUpdate.as_view(), name='swags_update'),
  path('swags/<int:pk>/delete/', views.SwagsDelete.as_view(), name='swags_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]