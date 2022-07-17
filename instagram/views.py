from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()  # data 범위 지정(all, filter, ...)
    serializer_class = PostSerializer

    # Class 기반 view에서 요청이 될 때마다 호출되는 함수
    def dispatch(self, request, *args, **kwargs):
        print("request body :", request.body)  # 실제 서비스라면 logger(장고 기본 지원)을 사용 추천
        print("request POST :", request.POST)
        return super().dispatch(request, *args, **kwargs)


def post_list(request):
    # request.method => 2개 분기
    pass


def post_detail(request, pk):
    # request.method => 3개 분기
    pass
