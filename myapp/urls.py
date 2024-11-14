from django.urls import path
from .views import hello, task_list, task_details
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TaskViewSet,AuthorViewSet,BookViewSet



# Basic URL patterns
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', hello, name='world'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/<int:pk>/', task_details, name='task_details'),  # Function-based views for tasks
]

# Set up the router for ViewSets
router = DefaultRouter()
router.register('author', AuthorViewSet, basename='author')
router.register('books', BookViewSet, basename='books')
router.register('task', TaskViewSet, basename='task')  # ModelViewSet for tasks

# Combine router urls with urlpatterns
urlpatterns += router.urls


