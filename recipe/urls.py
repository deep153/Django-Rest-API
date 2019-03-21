from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #url('^$', views.index, name='index'),
    url('^api/recipes/$', views.RecipeList.as_view()),
    url('^api/recipes/(?P<pk>\d+)', views.RecipeDetail.as_view()),
    url('^api/recipes/users/(?P<uid>\d+)', views.UserRecipeView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
