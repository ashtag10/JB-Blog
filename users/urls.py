#importation de la methode path
from django.urls import path
#importation le fichier views du module ou on se situe (users)
from . import views 



urlpatterns = [
  path("login/", views.login_view, name="login"),
  path ("logout", views.logout_view, name="logout"),
  path('signup/', views.signup_view, name='signup')
]