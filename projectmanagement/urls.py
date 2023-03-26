from django.urls import path
from . import views
from .views import HomeView, ProjectDetailView, AddProjectView, UpdateProjectView, DeleteProjectView,  LikeView, AddCommentView

urlpatterns = [
    path('about/', views.about, name="about"),
    path('', HomeView.as_view(), name="home"),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
    path('add_project/', AddProjectView.as_view(), name='add_project'),
    # path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('project/edit/<int:pk>', UpdateProjectView.as_view(), name='update_project'),
    path('project/<int:pk>/remove', DeleteProjectView.as_view(), name='delete_project'),
    # path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_project'),
    path('project/<int:pk>/comment/',
         AddCommentView.as_view(), name='add_comment'),
]
