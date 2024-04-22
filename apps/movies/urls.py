from django.urls import path, include
from apps.movies import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'movies'

movies_patterns = [
    path('inicio/', views.movie_list, name='home'),
    path('<int:pk>/', views.movie_detail, name='movies-detail'),
    path('crear/', views.movie_create, name='movies-create'),
    path('crear-categoria/', views.category_create, name='category-create'),
    path('<int:pk>/editar/', views.movie_update, name='movies-edit'),
    path('<int:pk>/eliminar/', views.movie_delete, name='movies-delete')
]

categories_patterns = [
    path('<int:pk>/editar/', views.category_update, name='category-edit'),
    path('<int:pk>/eliminar/', views.category_delete, name='category-delete')
]

urlpatterns = [
    path('', views.log_in, name='log-in'),
    path('log-out/', views.log_out, name='log-out'),
    path('categorias/', views.category_list, name='category-list'),
    path('categorias/', include(categories_patterns)),
    path('peliculas/', include(movies_patterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
