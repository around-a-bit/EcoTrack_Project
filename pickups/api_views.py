from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import PickupRequest
from .serializers import PickupRequestSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_pickups_api(request):
    qs = PickupRequest.objects.filter(user=request.user).order_by("-created_at")
    serializer = PickupRequestSerializer(qs, many=True)
    return Response(serializer.data)
