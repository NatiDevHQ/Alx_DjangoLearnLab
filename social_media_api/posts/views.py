from rest_framework import generics, status, viewsets, filters, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification


# Post CRUD operations
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Comment CRUD operations
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Like a post
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # ✅ Explicit get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)

        # ✅ Explicit get_or_create
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification for post author
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,
            )

        return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)


# Unlike a post
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=pk)

        try:
            like = Like.objects.get(post=post, user=request.user)
            like.delete()
            return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"detail": "You haven’t liked this post."}, status=status.HTTP_400_BAD_REQUEST)
