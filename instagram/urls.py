from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("post", views.PostViewSet)  # 2개의 URL을 만들어 줌(패턴)
# -> router.urls에 리스트 형태로 존재(url patter list)

urlpatterns = [
    # path("public/", views.PublicPostListAPIView.as_view()),
    path("public/", views.public_post_list),
    path("", include(router.urls)),
]
