from django.urls import path, re_path
from schedulerCrud import views
from django.contrib import admin

urlpatterns = [
    path('schedule', views.ScheduleEventsApi),
    re_path(r'^schedule/([0-9]+)$', views.ScheduleEventsApi),
    path('admin/', admin.site.urls),
]