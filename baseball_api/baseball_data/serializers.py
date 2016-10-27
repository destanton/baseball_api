from rest_framework import serializers
from baseball_data.models import Master, Batting, Pitching, Fielding


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'


class BattingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batting
        fields = '__all__'


class FieldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fielding
        fields = '__all__'


class PitchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitching
        fields = '__all__'
