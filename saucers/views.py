from rest_framework.response import Response
from rest_framework.views import APIView

from saucers.models import Saucer


# Create your views here.

class ListSaucers(APIView):
    """
    View to get all Saucers.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = SaucerSerializer

    def get(self, request, format=None):
        """
        Return a list of all Saucers.
        """
        queryset = Saucer.objects.all()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
