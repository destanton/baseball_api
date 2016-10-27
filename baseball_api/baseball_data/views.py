from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
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
    queryset = Pitching.objects.all()
    serializer_class = PitchingSerializer


class MasterDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class BattingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Batting.objects.all()
    serializer_class = BattingSerializer


class FieldingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pitching.objects.all()
    serializer_class = FieldingSerializer


class PitchingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pitching.objects.all()
    serializer_class = PitchingSerializer
