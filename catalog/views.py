from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Book, Review
from .serializers import RegisterSerializer, ChangePasswordSerializer, BookSerializer, ReviewSerializer
from .permissions import IsReviewOwnerOrReadOnly
from django.shortcuts import get_object_or_404
# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["كلمة المرور القديمة غير صحيحة."]},
                                status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"message": "تم تحديث كلمة المرور بنجاح"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]



class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_id'])

    def perform_create(self, serializer):
        book = Book.objects.get(id=self.kwargs['book_id'])
        serializer.save(user=self.request.user, book=book)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsReviewOwnerOrReadOnly]