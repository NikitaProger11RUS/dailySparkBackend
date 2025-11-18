from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

# создаём router и регистрируем ViewSet
router = DefaultRouter() # автоматически создаёт маршруты для CRUD операций
router.register(r'notes', NoteViewSet, basename='note') #связывает ViewSet с маршрутом.

#берём все маршруты от Router для подключения к главному urls.py проекта.
urlpatterns = router.urls 