#from django.db import models
from django.contrib import admin
from django.urls import path
from . import views
# Create your models here.

# Create your models here.
# class ModelsTemps(models.Model):
# 	date_creation = models.DateTimeField(auto_now_add=True)
# 	date_mise_a_jour = models.DateTimeField(auto_now=True)

# 	class Meta:
# 		abstract = True 

# class Articles(ModelsTemps):
# 	titre =  models.CharField(max_length=50)
# 	commentaire =  models.TextField(max_length=255)


# 	def __str__(self):
# 		return self.titre
		
# class Profile(models.Model):
#    name = models.CharField(max_length = 50)
#    picture = models.ImageField(upload_to = 'pictures')

#    class Meta:
#       db_table = "profile"





urlpatterns = [
    path('',views.redir),
    path('home',views.home, name="home"),
    path('nam\'ser/register',views.Register,name="register"),
    path('nam\'ser/login',views.Login,name="login"),
    path('logout', views.logout, name="logout"),
    path('users', views.PartUser, name="PartUser"),
    path('nam\'ser/live',views.live,name="live"),
    path('nam\'ser/matchs/resultat-foot-hier',views.football, name="football"),
    path('nam\'ser/matchs/matchs-demain',views.football_2, name="football_2"),
    path('nam\'ser/matchs/matchs-aujourd\hui',views.football_1, name="football_1"),
    path('nam\'ser/parie-match-en-direct',views.parie, name="parie")
]
