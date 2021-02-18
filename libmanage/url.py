from django.urls import path
from . import views
urlpatterns = [
path('', views.index),
path('home/', views.index),
path('signup/', views.register),
path('login/', views.login),
path('logout/', views.logout),
path('book/', views.book),
path('badd/', views.badd),
path('bupdate/<int:book_id>/', views.bupdate),
path('bdelete/<int:book_id>/', views.bdelete),
path('borrower/', views.borrower),
path('borroweradd/<int:book_id>/', views.borroweradd),
path('borrowerdel/<int:book_id>/', views.borrowerdel),
]