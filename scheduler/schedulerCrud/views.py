from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from schedulerCrud.serializers import ScheduleEventsSerializer
from schedulerCrud.models import ScheduleEvents

@csrf_exempt
def ScheduleEventsApi(request, id=None):
    if request.method=='GET':
        schedule_events = ScheduleEvents.objects.all()
        schedule_events_serializer=ScheduleEventsSerializer(schedule_events,many=True)
        return JsonResponse(schedule_events_serializer.data,safe=False)
    elif request.method=='POST':
        schedule_events_data=JSONParser().parse(request)
        schedule_events_serializer=ScheduleEventsSerializer(data=schedule_events_data)
        if schedule_events_serializer.is_valid():
            schedule_events_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        schedule_events_data=JSONParser().parse(request)
        schedule_event=ScheduleEvents.objects.get(Id=id)
        schedule_events_serializer=ScheduleEventsSerializer(schedule_event,data=schedule_events_data)
        if schedule_events_serializer.is_valid():
            schedule_events_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        schedule_event=ScheduleEvents.objects.get(Id=id)
        schedule_event.delete()
        return JsonResponse("Deleted Successfully",safe=False)