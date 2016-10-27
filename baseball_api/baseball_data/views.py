from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from baseball_data.models import Master, Batting, Fielding, Pitching
from baseball_data.serializers import MasterSerializer, BattingSerializer, FieldingSerializer, PitchingSerializer


class MasterListCreateAPIView(ListCreateAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class BattingListCreateAPIView(ListCreateAPIView):
    queryset = Batting.objects.all()
    serializer_class = BattingSerializer


class FieldingListCreateAPIView(ListCreateAPIView):
    queryset = Fielding.objects.all()
    serializer_class = FieldingSerializer


class PitchingListCreateAPIView(ListCreateAPIView):
    quesryset = Pitching.objects.all()
    serializer_class = PitchingSerializer
