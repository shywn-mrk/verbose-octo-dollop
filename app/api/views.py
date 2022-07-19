from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import URLSerializer
from api.utils import generate_code

from .models import URL

class URLCreateView(APIView):
    def post(self, request):
        url = request.data["original-url"]
        code = generate_code(url)

        new_url = {
            "original_url": url,
            "shorten_code": code
        }

        url = URL.objects.create(**new_url)

        serializer = URLSerializer(url)

        return Response(serializer.data)

class URLRetrieveView(APIView):
    def get(self, request, code):
        url = URL.objects.get(shorten_code=code)
        serializer = URLSerializer(url)
        return Response(serializer.data)
