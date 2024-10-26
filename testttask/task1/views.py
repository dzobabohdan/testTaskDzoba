from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.utils import timezone
from .models import Plant
from .serializers import PlantSerializer


class PlantAPIView(APIView):
    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            plant = Plant.objects.get(pk=pk)
        except Plant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PlantSerializer(plant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Water a plant
    def post(self, request, pk):
        try:
            plant = Plant.objects.get(pk=pk)
        except Plant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        plant.watering_frequency_days = plant.last_watered_date.day - timezone.now().day
        plant.last_watered_date = timezone.now().date()
        plant.save()
        return Response({'status': 'plant watered', 'watering_frequency_days': plant.watering_frequency_days, 'last_watered_date': plant.last_watered_date})