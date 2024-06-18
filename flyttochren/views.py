from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
import datetime

from .models import Storstadning, Hemstadning, Flyttstadning, Fonsterputs, ContactForm, Kontorsstadning, Trappstadning, Flytt
from .serializers import StorstadningSerializer, HemstadningSerializer, FlyttstadningSerializer, FonsterputsSerializer, ContactFormSerializer, KontorsstadningSerializer, TrappstadningSerializer, FlyttSerializer



@api_view(['GET'])
def available_times_storstadning(request):
    date = request.query_params.get('date')

    if not date:
        return Response({'error': 'Tarih belirtilmelidir.'}, status=400)

    try:
        # Tarih formatını kontrol etmek ve parse etmek
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return Response({'error': 'Geçersiz tarih formatı.'}, status=400)

    # Tam saatleri belirleyelim
    all_hours = [datetime.time(hour=h) for h in range(7,19)]

    # O gün dolu olan saatleri alalım
    booked_hours = Storstadning.objects.filter(selectedDate=date).values_list('selectedTime', flat=True)

    # Müsait saatleri hesaplayalım
    available_hours = [hour for hour in all_hours if hour not in booked_hours]

    # Saatleri string formatına dönüştürelim
    available_hours_str = [hour.strftime('%H:%M') for hour in available_hours]

    return Response({'available_hours': available_hours_str})


@api_view(['GET'])
def available_times_flytthjalp(request):
    date = request.query_params.get('date')

    if not date:
        return Response({'error': 'Tarih belirtilmelidir.'}, status=400)

    try:
        # Tarih formatını kontrol etmek ve parse etmek
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return Response({'error': 'Geçersiz tarih formatı.'}, status=400)

    # Tam saatleri belirleyelim
    all_hours = [datetime.time(hour=h) for h in range(8,9)]

    # O gün dolu olan saatleri alalım
    booked_hours = Flytt.objects.filter(selectedDate=date).values_list('selectedTime', flat=True)

    # Müsait saatleri hesaplayalım
    available_hours = [hour for hour in all_hours if hour not in booked_hours]

    # Saatleri string formatına dönüştürelim
    available_hours_str = [hour.strftime('%H:%M') for hour in available_hours]

    return Response({'available_hours': available_hours_str})


@api_view(['GET'])
def available_times_flyttstadning(request):
    date = request.query_params.get('date')

    if not date:
        return Response({'error': 'Tarih belirtilmelidir.'}, status=400)

    try:
        # Tarih formatını kontrol etmek ve parse etmek
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return Response({'error': 'Geçersiz tarih formatı.'}, status=400)

    # Tam saatleri belirleyelim
    all_hours = [datetime.time(hour=h) for h in range(7,19)]

    # O gün dolu olan saatleri alalım
    booked_hours = Flyttstadning.objects.filter(selectedDate=date).values_list('selectedTime', flat=True)

    # Müsait saatleri hesaplayalım
    available_hours = [hour for hour in all_hours if hour not in booked_hours]

    # Saatleri string formatına dönüştürelim
    available_hours_str = [hour.strftime('%H:%M') for hour in available_hours]

    return Response({'available_hours': available_hours_str})


@api_view(['GET'])
def available_times_hemstadning(request):
    date = request.query_params.get('date')

    if not date:
        return Response({'error': 'Tarih belirtilmelidir.'}, status=400)

    try:
        # Tarih formatını kontrol etmek ve parse etmek
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return Response({'error': 'Geçersiz tarih formatı.'}, status=400)

    # Tam saatleri belirleyelim
    all_hours = [datetime.time(hour=h) for h in range(7, 19)]

    # O gün dolu olan saatleri alalım
    booked_hours = Hemstadning.objects.filter(selectedDate=date).values_list('selectedTime', flat=True)

    # Müsait saatleri hesaplayalım
    available_hours = [hour for hour in all_hours if hour not in booked_hours]

    # Saatleri string formatına dönüştürelim
    available_hours_str = [hour.strftime('%H:%M') for hour in available_hours]

    return Response({'available_hours': available_hours_str})


@api_view(['GET'])
def available_times_fonsterputs(request):
    date = request.query_params.get('date')

    if not date:
        return Response({'error': 'Tarih belirtilmelidir.'}, status=400)

    try:
        # Tarih formatını kontrol etmek ve parse etmek
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return Response({'error': 'Geçersiz tarih formatı.'}, status=400)

    # Tam saatleri belirleyelim
    all_hours = [datetime.time(hour=h) for h in range(7, 19)]

    # O gün dolu olan saatleri alalım
    booked_hours = Fonsterputs.objects.filter(selectedDate=date).values_list('selectedTime', flat=True)

    # Müsait saatleri hesaplayalım
    available_hours = [hour for hour in all_hours if hour not in booked_hours]

    # Saatleri string formatına dönüştürelim
    available_hours_str = [hour.strftime('%H:%M') for hour in available_hours]

    return Response({'available_hours': available_hours_str})


class ContactFormMVS(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer


class StorstadningMVS(viewsets.ModelViewSet):
    queryset = Storstadning.objects.all()
    serializer_class = StorstadningSerializer


class FlyttMVS(viewsets.ModelViewSet):
    queryset = Flytt.objects.all()
    serializer_class = FlyttSerializer


class HemstadningMVS(viewsets.ModelViewSet):
    queryset = Hemstadning.objects.all()
    serializer_class = HemstadningSerializer


class FlyttstadningMVS(viewsets.ModelViewSet):
    queryset = Flyttstadning.objects.all()
    serializer_class = FlyttstadningSerializer


class FonsterputsMVS(viewsets.ModelViewSet):
    queryset = Fonsterputs.objects.all()
    serializer_class = FonsterputsSerializer


class KontorsstadningMVS(viewsets.ModelViewSet):
    queryset = Kontorsstadning.objects.all()
    serializer_class = KontorsstadningSerializer


class TrappstadningMVS(viewsets.ModelViewSet):
    queryset = Trappstadning.objects.all()
    serializer_class = TrappstadningSerializer
