from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(name='name', max_length=100)
    password = models.TextField(name='password', null=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Camera(models.Model):
    name = models.CharField(name='name', max_length=70)
    rtsp_url = models.CharField(name='rtsp_url', max_length=100)

    def __str__(self):
        return f"{self.name}, {self.rtsp_url}"

    class Meta:
        verbose_name = 'Камера'
        verbose_name_plural = 'Камеры'


class Logs(models.Model):
    name_service = models.CharField(name='name_service', max_length=50)
    message = models.TextField(name='message')
    date_time = models.DateTimeField(name='date_time')
    level_event = models.TextField(name='level_event', max_length=100)
    more_information = models.TextField(name='more_information')

    def __str__(self):
        return f"{self.name_service}, {self.message}, {self.date_time}, {self.level_event}, {self.more_information}"

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'


class Rtsp_server(models.Model):
    name_rtsp_server = models.CharField(name='name_rtsp_server', max_length=100)
    input_rtsp = models.TextField(name='input_rtsp')
    output_rtsp = models.TextField(name='output_rtsp')

    def __str__(self):
        return f"{self.name_rtsp_server}, {self.input_rtsp}, {self.output_rtsp}"

    class Meta:
        verbose_name = 'Rtsp сервер'
        verbose_name_plural = 'Rtsp сервер'


class Ftp(models.Model):
    host = models.CharField(name='host', max_length=100)
    ftp_login = models.TextField(name='ftp_login')
    ftp_password = models.TextField(name='ftp_password')

    def __str__(self):
        return f"{self.host}, {self.ftp_login}, {self.ftp_password}"

    class Meta:
        verbose_name = 'Фтп'
        verbose_name_plural = 'Фтп'
