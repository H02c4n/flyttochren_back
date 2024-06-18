from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import StorstadningMVS, HemstadningMVS, FlyttstadningMVS, FonsterputsMVS, ContactFormMVS, KontorsstadningMVS, TrappstadningMVS, FlyttMVS, available_times_storstadning, available_times_hemstadning, available_times_fonsterputs, available_times_flyttstadning, available_times_flytthjalp

router = DefaultRouter()


router.register('storstadning', StorstadningMVS)
router.register('hemstadning', HemstadningMVS)
router.register('flyttstadning', FlyttstadningMVS)
router.register('fonsterputs', FonsterputsMVS)
router.register('kontakt', ContactFormMVS)
router.register('kontorsstadning', KontorsstadningMVS)
router.register('trappstadning', TrappstadningMVS)
router.register('flytthjalp', FlyttMVS)


urlpatterns = [
 path('', include(router.urls)),
 path('available-times-storstadning/', available_times_storstadning, name='available_times_storstadning'),
 path('available-times-flyttstadning/', available_times_flyttstadning, name='available_times_flyttstadning'),
 path('available-times-hemstadning/', available_times_hemstadning, name='available_times_hemstadning'),
 path('available-times-fonsterputs/', available_times_fonsterputs, name='available_times_fonsterputs'),
 path('available-times-flytthjalp/', available_times_flytthjalp, name='available_times_flytthjalp'),
]
