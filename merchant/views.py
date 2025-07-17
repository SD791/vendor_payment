from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Merchant
from .serializers import MerchantSerializer

@api_view(['POST'])
def create_merchant(request):
    serializer = MerchantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(using='merchant')  # Use merchant_db
        return Response(serializer.data)
    return Response(serializer.errors)
