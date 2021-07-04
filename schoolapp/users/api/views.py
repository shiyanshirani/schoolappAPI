from rest_framework import viewsets
from rest_framework.response import Response

from users.models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = UserProfile.objects.all()
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = UserProfile.objects.all()
        # user = get_object_or_404(queryset, pk=pk)
        try:
            user = UserProfile.objects.get(pk=pk)
            serializer = UserProfileSerializer(user)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response({"Error": "No data"})

        
        
