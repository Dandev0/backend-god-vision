from rest_framework import serializers
from .models import Camera, Logs, Rtsp_server, Ftp


class SerializerCamera(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'

class SerializerCamerac(SerializerCamera):
    class Meta:
        model = Camera
        fields = ('name', 'rtsp_url')


class SerializerLogs(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'


class SerializerRestreamingServer(serializers.ModelSerializer):
    class Meta:
        model = Rtsp_server
        fields = '__all__'


class Ftpserializer(serializers.ModelSerializer):
    class Meta:
        model = Ftp
        fields = '__all__'
