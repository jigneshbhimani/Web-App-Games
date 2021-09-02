from app.models import *
from app.serializer import *
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import date, timedelta

# Create your views here.

# --------------------Register View--------------------


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if (serializer.is_valid()):
            user = serializer.save()
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User Created Successfully. Now perform Login and get access token",
            })
# --------------------Logout View--------------------


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
# --------------------Genres View--------------------


class GenresView(ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
# --------------------Tags View--------------------


class TagsView(ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
# --------------------Publishers View--------------------


class PublishersView(ListAPIView):
    queryset = Publishers.objects.all()
    serializer_class = PublishersSerializer
# --------------------Games View--------------------


class GamesView(ListAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    # Filteration
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('name', 'tags', 'genres')
# --------------------UpComing Games View--------------------


class UpComingView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

        def get_queryset(self):
            now = timezone.now() + timedelta(days=7)
            upcoming = Games.objects.filter(release_date=now).order_by('-release_date')
            return list(upcoming)


        serializer_class = GamesSerializer
        permission_classes = [IsAuthenticated]

        
        def get(self, request, id=None):
            if id:
                return self.retrieve(request)
            else:
                return self.list(request)

        def post(self, request):
            return self.create(request)

        def put(self, request, id=None):
            return self.update(request, id)

        def delete(self, request, id):
            return self.destroy(request, id)