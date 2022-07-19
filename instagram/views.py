from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


# class PublicPostListAPIView(generics.ListCreateAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer


# class PublicPostListAPIView(APIView):  # generics을 사용하지 않고 APIView로 구현
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
#
# public_post_list = PublicPostListAPIView.as_view()

# public_post_list를 함수 기반 뷰로
@api_view(["GET"])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()  # data 범위 지정(all, filter, ...)
    serializer_class = PostSerializer

    @action(detail=False, methods=["GET"])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["PATCH"])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=["is_public"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # Class 기반 view에서 요청이 될 때마다 호출되는 함수
    # def dispatch(self, request, *args, **kwargs):
    #     print("request body :", request.body)  # 실제 서비스라면 logger(장고 기본 지원)을 사용 추천
    #     print("request POST :", request.POST)
    #     return super().dispatch(request, *args, **kwargs)


# def post_list(request):
#     # request.method => 2개 분기
#     pass
#
#
# def post_detail(request, pk):
#     # request.method => 3개 분기
#     pass


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "instagram/post_detail.html"

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(
            {
                "post": post,
            }
        )
