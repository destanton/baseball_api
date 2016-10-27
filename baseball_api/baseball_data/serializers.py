from rest_framework import serializers
from baseball_data.models import Master, Batting, Pitching, Fielding


class MasterSerializer(serializers.ModelSerializer):
    # player_code = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     view_name="master_detail_update_destroy_api_view",
    #     read_only=True,
    # )

    class Meta:
        model = Master
        fields = '__all__'


class BattingSerializer(serializers.ModelSerializer):

    on_base = serializers.FloatField()
    # on_base_percentage = serializers.SerializerMethodField()

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
