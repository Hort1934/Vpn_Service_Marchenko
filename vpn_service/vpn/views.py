from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserSite
from .serializers import UserSiteSerializer
from users.models import UserProfile
from .serializers import UserProfileSerializer
from django.http import HttpResponse
import requests

class UserSiteViewSet(viewsets.ModelViewSet):
    queryset = UserSite.objects.all()
    serializer_class = UserSiteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

def proxy_view(request, site_name, *args):
    user_site = UserSite.objects.get(user=request.user, name=site_name)
    external_url = user_site.url + request.path
    response = requests.get(external_url)

    modified_content = response.content.replace(external_url.encode(), f"/{site_name}".encode())
    return HttpResponse(modified_content, content_type=response.headers['Content-Type'])
