from django.contrib import admin
from .models import Users, Camera, Logs, Rtsp_server, Ftp
# Register your models here.


admin.site.register(Camera)
admin.site.register(Logs)
admin.site.register(Rtsp_server)
admin.site.register(Ftp)