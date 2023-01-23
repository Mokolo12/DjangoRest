from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from notes.views import NoteModelViewSet, ProjectModelViewSet
from users.views import UserModelViewSet

router = DefaultRouter()  # Create a router
router.register('users', UserModelViewSet)  # Register User model view set with the router
router.register('notes', NoteModelViewSet)  # Register Note model view set with the router
router.register('projects', ProjectModelViewSet)  # Register Project model view set with the router

urlpatterns = [
    path('admin/', admin.site.urls),