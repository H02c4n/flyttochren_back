from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import Storstadning, Hemstadning, Flyttstadning, Fonsterputs, Windows, WindowsFonsterputs, UserInfo, UserInfoHemstadning, UserInfoFlyttstadning, UserInfoFonsterputs, ContactForm, Kontorsstadning, Trappstadning, Flytt, UserInfoFlytt
# Register your models here.


class WindowsInline(admin.StackedInline):
    model = Windows

class WindowsFonsterputsInline(admin.StackedInline):
    model = WindowsFonsterputs

class UserInfoInline(admin.StackedInline):
    model = UserInfo

class UserInfoHemstadningInline(admin.StackedInline):
    model = UserInfoHemstadning

class UserInfoFlyttstadningInline(admin.StackedInline):
    model = UserInfoFlyttstadning

class UserInfoFonsterputsInline(admin.StackedInline):
    model = UserInfoFonsterputs

class UserInfoFlyttInline(admin.StackedInline):
    model = UserInfoFlytt

class StorstadningAdmin(admin.ModelAdmin):
    list_display = (
            'user_info',
            'bostadsyta',
            'husdjur',
            'hasKatt',
            'hasHund',
            'hasAnnat',
            'fonsterputs',
            'hasKarmtvatt',
            'hasStegeBehovs',
            'hasStadutrustning',
            'ovenCount',
            'fridgeCount',
            'comment',
            'commentFonster',
            'keyStatus',
            'utrustningAvgift',
            'serviceAvgift',
            'stegeAvgift',
            'totalAmount',
            'selectedDate',
            'selectedTime',
            'windows',
            'total_pris')
    search_fields = ('user_info__firstName', 'user_info__lastName', 'user_info__email', 'user_info__postOrt')
    list_filter = ('husdjur', 'fonsterputs', 'selectedDate')
    fieldsets = (
        ('Area', {
            'fields': ('bostadsyta',)
        }),
        ('Husdjur', {
            'fields': ('husdjur', 'hasKatt', 'hasHund', 'hasAnnat')
        }),
        ('Kommentar', {
            'fields': ('comment', 'commentFonster', 'keyStatus')
        }),
        ('Extra Services', {
            'fields': ('fonsterputs', 'hasKarmtvatt', 'hasStegeBehovs', 'hasStadutrustning', 'ovenCount', 'fridgeCount')
        }),
        ('Datum', {
            'fields': ('selectedDate', 'selectedTime')
        }),
        ('Avgift',  {
            'fields': ('serviceAvgift', 'stegeAvgift', 'utrustningAvgift', 'totalAmount')
        }),
    )
    inlines = [WindowsInline, UserInfoInline]

class FlyttAdmin(admin.ModelAdmin):
    list_display = (
            'user_info',
            'postnummerFrom',
            'cityFrom',
            'gatuAdressFrom',
            'boendeTypFrom',
            'bostadsytaFrom',
            'biutrymmenFrom',
            'vaningFrom',
            'hissFrom',
            'postnummerTo',
            'cityTo',
            'gatuAdressTo',
            'boendeTypTo',
            'bostadsytaTo',
            'biutrymmenTo',
            'vaningTo',
            'hissTo',
            'kommentar',
            'hasNedpacking',
            'hasUppacking',
            'hasMagasinering',
            'hasFlyttstad',
            'hasAtervinning',
            'selectedDate',
            'selectedTime'
        )
    search_fields = ('user_info__firstName', 'user_info__lastName', 'user_info__email')
    list_filter = ('cityFrom', 'cityTo', 'selectedDate')
    inlines = [UserInfoFlyttInline]

class HemstadningAdmin(admin.ModelAdmin):
    list_display = (
            'user_info',
            'bostadsyta',
            'husdjur',
            'hasKatt',
            'hasHund',
            'hasAnnat',
            'frekvens',
            'totalAmount',
            'selectedDate',
            'selectedTime',
            'total_pris'
            )
    inlines = [UserInfoHemstadningInline]

class FlyttstadningAdmin(admin.ModelAdmin):
    list_display = ('user_info',
            'bostadsyta',
            'keyStatus',
            'serviceAvgift',
            'totalAmount',
            'selectedDate',
            'selectedTime',
            'total_pris'
            )
    inlines = [UserInfoFlyttstadningInline]

class FonsterputsAdmin(admin.ModelAdmin):
    list_display = (
        'user_info',
        'windows',
        'commentFonster',
        'hasKarmtvatt',
        'hasStegeBehovs',
        'stegeAvgift',
        'selectedDate',
        'selectedTime',
        'totalAmount',
        'total_pris',
    )
    inlines = [WindowsFonsterputsInline, UserInfoFonsterputsInline]

admin.site.register(ContactForm)
admin.site.register(Kontorsstadning)
admin.site.register(Trappstadning)
admin.site.register(Storstadning, StorstadningAdmin)
admin.site.register(Hemstadning, HemstadningAdmin)
admin.site.register(Flyttstadning, FlyttstadningAdmin)
admin.site.register(Fonsterputs, FonsterputsAdmin)
admin.site.register(Flytt, FlyttAdmin)
admin.site.register(Windows)
admin.site.register(WindowsFonsterputs)
admin.site.register(UserInfo)
admin.site.register(UserInfoHemstadning)
admin.site.register(UserInfoFlyttstadning)
admin.site.register(UserInfoFonsterputs)
admin.site.register(UserInfoFlytt)


admin.site.site_title = _("Flytt Och Ren")
admin.site.site_header = _("Flytt Och Ren Admin Portal")
admin.site.index_title = _("Welcome to Flytt Och Ren Admin Portal")