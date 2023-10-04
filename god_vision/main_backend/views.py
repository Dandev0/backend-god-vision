import json
from .api_cameras.api_cameras_ import Rabbit_sender
from django.shortcuts import render
from django.http import JsonResponse
from .models import Camera, Logs, Rtsp_server, Ftp
from .serializer_ import SerializerCamera, SerializerLogs, SerializerRestreamingServer, Ftpserializer, SerializerCamerac
from rest_framework import generics
from datetime import timedelta
from django.utils import timezone


# Create your views here.
class HtmlPage:
    def __init__(self, html_file='main_backend/god_vision.html'):
        self.__html_file = html_file

    def page(self, request):
        data_list = []
        cameras_data = Camera.objects.all()
        for i in range(0, len(cameras_data)):
            data_serialize = SerializerCamerac(cameras_data[i]).data
            data_list.append(data_serialize)
        cam = {"Title": "Main page", 'cameras': data_list}
        return render(request, self.__html_file, context=cam)


class CameraBase(generics.ListAPIView):
    http_method_names = ['get', ]
    queryset = Camera.objects.all()
    serializer_class = SerializerCamera


class LogsBase(generics.ListAPIView):
    http_method_names = ['get', ]
    queryset = Camera.objects.all()
    serializer_class = SerializerLogs


class DateTimeRange:
    @staticmethod
    def get_range(start_datetime):
        now_date = timezone.now()
        start_date = now_date - timedelta(days=int(start_datetime))
        list_dates = [start_date, now_date]
        return list_dates


class Logs_services(LogsBase):
    def get_queryset(self):
        try:
            service = self.request.GET.get('service_name')
            print(service)
            range_date = self.request.GET.get('range')
            if range_date is not None:
                list_dates = DateTimeRange().get_range(range_date)
                queryset = Logs.objects.filter(name_service=service,
                                               date_time__date__range=(list_dates[0], list_dates[1]))
                serializer_class = SerializerLogs(queryset, many=True)
                return queryset
            elif service is None:
                if range_date is not None:
                    list_dates = DateTimeRange().get_range(range_date)
                    queryset = Logs.objects.filter(name_service=service,
                                                   date_time__date__range=(list_dates[0], list_dates[1]))
                    serializer_class = SerializerLogs(queryset, many=True)
                    return queryset
                else:
                    queryset = Logs.objects.all()
                    serializer_class = SerializerLogs(queryset, many=True)
                    return queryset
            else:
                queryset = Logs.objects.filter(name_service=service)
                serializer_class = SerializerLogs(queryset, many=True)
                return queryset
        except ValueError:
            pass


def validator_data(request):
    if request.method == 'POST':
        import ast
        ftp_list = []
        query = Ftp.objects.all()
        for i in range(0, len(query)):
            data_serialize = Ftpserializer(query[i]).data
            ftp_list.append(data_serialize)
        try:
            value_string = request.body.decode('utf-8')
            recep_data = json.loads(value_string)
            rtsp_name = recep_data['camera_name']
            object = Camera.objects.filter(name=rtsp_name)
            if object.exists():
                data_list = []
                need_keys = ['rtsp_url', 'type_camera', 'command', 'time_archive_write', 'camera_name', 'ftp_data']
                for i in recep_data.keys():
                    if i in need_keys:
                        continue
                    else:
                        data = {'data': 'Request body is not valid!'}
                        return JsonResponse(data)
                for i in range(0, len(object)):
                    data_serialize = SerializerCamera(object[i]).data
                    data_list.append(data_serialize)
                    data = {'data': data_list, 'command': recep_data['command']}
                message_to_rabbit = {
                    "ftp_data": ftp_list[-1],
                    "data": ast.literal_eval(request.body.decode('utf-8'))
                }
                message_to_rabbit = json.dumps(message_to_rabbit)
                Rabbit_sender(queue_='recognitions-service', message=message_to_rabbit).send_message()
            else:
                data = {'Message:': f'Camera {rtsp_name} is not exists!'}
            return JsonResponse(data)
        except KeyError:
            data = {'data': 'Request body is not valid!'}
            return JsonResponse(data)


def restream_service_api(request):
    if request.method == 'POST':
        value_string = request.body.decode('utf-8')
        recep_data = json.loads(value_string)
        server_name = recep_data['name']
        object = Rtsp_server.objects.filter(name_rtsp_server=server_name)
        if object.exists():
            data_list = []
            need_keys = ['command', 'rtsp_url', 'output_url', 'data', 'name']
            for i in recep_data.keys():
                if i in need_keys:
                    continue
                else:
                    data = {'data': 'Request body is not valid!'}
                    return JsonResponse(data)
            for i in range(0, len(object)):
                data_serialize = SerializerRestreamingServer(object[i]).data
                data_list.append(data_serialize)
                data = {'data': data_list, 'command': f'{recep_data["command"]}'}
            Rabbit_sender(queue_='runner_task_for_rtsp_server_queue', message=request.body).send_message()
        else:
            data = {'Message:': f'Rtsp server {server_name} is not exists!'}
        return JsonResponse(data)