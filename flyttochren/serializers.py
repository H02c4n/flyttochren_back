from rest_framework import serializers
from .models import Storstadning, Hemstadning, Flyttstadning, Fonsterputs, Windows, WindowsFonsterputs, UserInfo, UserInfoHemstadning, UserInfoFonsterputs, UserInfoFlyttstadning, ContactForm, Kontorsstadning, Trappstadning, Flytt, UserInfoFlytt


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = [
            'id',
            'name',
            'email',
            'tel',
            'message'
        ]


class WindowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Windows
        fields = [
            'utanSprojs_count',
            'utanSprojs_sides',
            'medSprojs_count',
            'medSprojs_sides',
            'overhangda_count',
            'overhangda_sides',
            'balkong_count',
            'balkong_sides'
        ]


class WindowsFonsterputsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowsFonsterputs
        fields = [
            'utanSprojs_count',
            'utanSprojs_sides',
            'medSprojs_count',
            'medSprojs_sides',
            'overhangda_count',
            'overhangda_sides',
            'balkong_count',
            'balkong_sides'
        ]


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [
            'firstName',
            'lastName',
            'phoneNumber',
            'email',
            'gatuAdress',
            'postNummer',
            'postOrt'
        ]


class UserInfoHemstadningSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfoHemstadning
        fields = [
            'firstName',
            'lastName',
            'phoneNumber',
            'email',
            'gatuAdress',
            'postNummer',
            'postOrt'
        ]


class UserInfoFlyttstadningSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfoFlyttstadning
        fields = [
            'firstName',
            'lastName',
            'phoneNumber',
            'email',
            'gatuAdress',
            'postNummer',
            'postOrt'
        ]


class UserInfoFonsterputsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfoFonsterputs
        fields = [
            'firstName',
            'lastName',
            'phoneNumber',
            'email',
            'gatuAdress',
            'postNummer',
            'postOrt'
        ]


class UserInfoFlyttSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [
            'firstName',
            'lastName',
            'phoneNumber',
            'email'
        ]


class StorstadningSerializer(serializers.ModelSerializer):
    windows = WindowsSerializer()
    user_info = UserInfoSerializer()
    total_pris = serializers.SerializerMethodField()

    class Meta:
        model = Storstadning
        fields = [
            'id',
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
            'total_pris'
        ]

    def create(self, validated_data):
        windows_data = validated_data.pop('windows')
        user_info_data = validated_data.pop('user_info')
        service_request = Storstadning.objects.create(**validated_data)
        Windows.objects.create(service_request=service_request, **windows_data)
        UserInfo.objects.create(service_request=service_request, **user_info_data)
        return service_request

    def update(self, instance, validated_data):
        windows_data = validated_data.pop('windows')
        user_info_data = validated_data.pop('user_info')

        instance.bostadsyta = validated_data.get('bostadsyta', instance.bostadsyta)
        instance.husdjur = validated_data.get('husdjur', instance.husdjur)
        instance.hasKatt = validated_data.get('hasKatt', instance.hasKatt)
        instance.hasHund = validated_data.get('hasHund', instance.hasHund)
        instance.hasAnnat = validated_data.get('hasAnnat', instance.hasAnnat)
        instance.fonsterputs = validated_data.get('fonsterputs', instance.fonsterputs)
        instance.hasKarmtvatt = validated_data.get('hasKarmtvatt', instance.hasKarmtvatt)
        instance.hasStegeBehovs = validated_data.get('hasStegeBehovs', instance.hasStegeBehovs)
        instance.hasStadutrustning = validated_data.get('hasStadutrustning', instance.hasStadutrustning)
        instance.ovenCount = validated_data.get('ovenCount', instance.ovenCount)
        instance.fridgeCount = validated_data.get('fridgeCount', instance.fridgeCount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.commentFonster = validated_data.get('commentFonster', instance.commentFonster)
        instance.keyStatus = validated_data.get('keyStatus', instance.keyStatus)
        instance.utrustningAvgift = validated_data.get('utrustningAvgift', instance.utrustningAvgift)
        instance.serviceAvgift = validated_data.get('serviceAvgift', instance.serviceAvgift)
        instance.stegeAvgift = validated_data.get('stegeAvgift', instance.stegeAvgift)
        instance.totalAmount = validated_data.get('totalAmount', instance.totalAmount)
        instance.selectedDate = validated_data.get('selectedDate', instance.selectedDate)
        instance.selectedTime = validated_data.get('selectedTime', instance.selectedTime)
        instance.save()

        windows = instance.windows
        windows.utanSprojs_count = windows_data.get('utanSprojs_count', windows.utanSprojs_count)
        windows.utanSprojs_sides = windows_data.get('utanSprojs_sides', windows.utanSprojs_sides)
        windows.medSprojs_count = windows_data.get('medSprojs_count', windows.medSprojs_count)
        windows.medSprojs_sides = windows_data.get('medSprojs_sides', windows.medSprojs_sides)
        windows.overhangda_count = windows_data.get('overhangda_count', windows.overhangda_count)
        windows.overhangda_sides = windows_data.get('overhangda_sides', windows.overhangda_sides)
        windows.balkong_count = windows_data.get('balkong_count', windows.balkong_count)
        windows.balkong_sides = windows_data.get('balkong_sides', windows.balkong_sides)
        windows.save()

        user_info = instance.user_info
        user_info.firstName = user_info_data.get('firstName', user_info.firstName)
        user_info.lastName = user_info_data.get('lastName', user_info.lastName)
        user_info.phoneNumber = user_info_data.get('phoneNumber', user_info.phoneNumber)
        user_info.email = user_info_data.get('email', user_info.email)
        user_info.gatuAdress = user_info_data.get('gatuAdress', user_info.gatuAdress)
        user_info.postNummer = user_info_data.get('postNummer', user_info.postNummer)
        user_info.postOrt = user_info_data.get('postOrt', user_info.postOrt)
        user_info.save()

        return instance

    def get_total_pris(self, obj):
        #start with the base amount
        total_pris = obj.serviceAvgift + obj.totalAmount

        # conditionally add stegeAvgift
        if obj.hasStegeBehovs:
            total_pris += obj.stegeAvgift
        
        #conditionally add utrustningAvgift
        if obj.hasStadutrustning:
            total_pris += obj.utrustningAvgift
        
        return total_pris
    

class FlyttSerializer(serializers.ModelSerializer):

    user_info = UserInfoFlyttSerializer()

    class Meta:
        model = Flytt
        fields = [
            'id',
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
        ]

    def create(self, validated_data):
        user_info_data = validated_data.pop('user_info')
        service_request = Flytt.objects.create(**validated_data)
        UserInfoFlytt.objects.create(service_request=service_request, **user_info_data)
        return service_request

    def update(self, instance, validated_data):
        user_info_data = validated_data.pop('user_info')

        instance.postnummerFrom = validated_data.get('postnummerFrom', instance.postnummerFrom)
        instance.cityFrom = validated_data.get('cityFrom', instance.cityFrom)
        instance.gatuAdressFrom = validated_data.get('gatuAdressFrom', instance.gatuAdressFrom)
        instance.boendeTypFrom = validated_data.get('boendeTypFrom', instance.boendeTypFrom)
        instance.bostadsytaFrom = validated_data.get('bostadsytaFrom', instance.bostadsytaFrom)
        instance.biutrymmenFrom = validated_data.get('biutrymmenFrom', instance.biutrymmenFrom)
        instance.vaningFrom = validated_data.get('vaningFrom', instance.vaningFrom)
        instance.hissFrom = validated_data.get('hissFrom', instance.hissFrom)
        instance.postnummerTo = validated_data.get('postnummerTo', instance.postnummerTo)
        instance.cityTo = validated_data.get('cityTo', instance.cityTo)
        instance.gatuAdressTo = validated_data.get('gatuAdressTo', instance.gatuAdressTo)
        instance.boendeTypTo = validated_data.get('boendeTypTo', instance.boendeTypTo)
        instance.bostadsytaTo = validated_data.get('bostadsytaTo', instance.bostadsytaTo)
        instance.biutrymmenTo = validated_data.get('biutrymmenTo', instance.biutrymmenTo)
        instance.vaningTo = validated_data.get('vaningTo', instance.vaningTo)
        instance.hissTo = validated_data.get('hissTo', instance.hissTo)

        instance.kommentar = validated_data.get('kommentar', instance.kommentar)
        instance.hasNedpacking = validated_data.get('hasNedpacking', instance.hasNedpacking)
        instance.hasUppacking = validated_data.get('hasUppacking', instance.hasUppacking)
        instance.hasMagasinering = validated_data.get('hasMagasinering', instance.hasMagasinering)
        instance.hasFlyttstad = validated_data.get('hasFlyttstad', instance.hasFlyttstad)
        instance.hasAtervinning = validated_data.get('hasAtervinning', instance.hasAtervinning)

        instance.selectedDate = validated_data.get('selectedDate', instance.selectedDate)
        instance.selectedTime = validated_data.get('selectedTime', instance.selectedTime)
        instance.save()

        user_info = instance.user_info
        user_info.firstName = user_info_data.get('firstName', user_info.firstName)
        user_info.lastName = user_info_data.get('lastName', user_info.lastName)
        user_info.phoneNumber = user_info_data.get('phoneNumber', user_info.phoneNumber)
        user_info.email = user_info_data.get('email', user_info.email)
        user_info.save()

        return instance
    

class HemstadningSerializer(serializers.ModelSerializer):
    user_info = UserInfoHemstadningSerializer()
    total_pris = serializers.SerializerMethodField()

    class Meta:
        model = Hemstadning
        fields = [
            'id',
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
        ]

    def create(self, validated_data):
        user_info_data = validated_data.pop('user_info')
        service_request = Hemstadning.objects.create(**validated_data)

        UserInfoHemstadning.objects.create(service_request=service_request, **user_info_data)
        return service_request

    def update(self, instance, validated_data):
        user_info_data = validated_data.pop('user_info')

        instance.bostadsyta = validated_data.get('bostadsyta', instance.bostadsyta)
        instance.husdjur = validated_data.get('husdjur', instance.husdjur)
        instance.hasKatt = validated_data.get('hasKatt', instance.hasKatt)
        instance.hasHund = validated_data.get('hasHund', instance.hasHund)
        instance.hasAnnat = validated_data.get('hasAnnat', instance.hasAnnat)
        instance.frekvens = validated_data.get('frekvens', instance.frekvens)
        instance.totalAmount = validated_data.get('totalAmount', instance.totalAmount)
        instance.selectedDate = validated_data.get('selectedDate', instance.selectedDate)
        instance.selectedTime = validated_data.get('selectedTime', instance.selectedTime)
        instance.save()

        user_info = instance.user_info
        user_info.firstName = user_info_data.get('firstName', user_info.firstName)
        user_info.lastName = user_info_data.get('lastName', user_info.lastName)
        user_info.phoneNumber = user_info_data.get('phoneNumber', user_info.phoneNumber)
        user_info.email = user_info_data.get('email', user_info.email)
        user_info.gatuAdress = user_info_data.get('gatuAdress', user_info.gatuAdress)
        user_info.postNummer = user_info_data.get('postNummer', user_info.postNummer)
        user_info.postOrt = user_info_data.get('postOrt', user_info.postOrt)
        user_info.save()

        return instance

    def get_total_pris(self, obj):
        #start with the base amount
        total_pris = obj.totalAmount
        
        return total_pris


class FlyttstadningSerializer(serializers.ModelSerializer):
    user_info = UserInfoFlyttstadningSerializer()
    total_pris = serializers.SerializerMethodField()

    class Meta:
        model = Flyttstadning
        fields = [
            'id',
            'user_info',
            'bostadsyta',
            'keyStatus',
            'serviceAvgift',
            'totalAmount',
            'selectedDate',
            'selectedTime',
            'total_pris'
        ]

    def create(self, validated_data):
        user_info_data = validated_data.pop('user_info')
        service_request = Flyttstadning.objects.create(**validated_data)

        UserInfoFlyttstadning.objects.create(service_request=service_request, **user_info_data)
        return service_request

    def update(self, instance, validated_data):
        user_info_data = validated_data.pop('user_info')

        instance.bostadsyta = validated_data.get('bostadsyta', instance.bostadsyta)
        instance.keyStatus = validated_data.get('keyStatus', instance.keyStatus)
        instance.serviceAvgift = validated_data.get('serviceAvgift', instance.serviceAvgift)
        instance.totalAmount = validated_data.get('totalAmount', instance.totalAmount)
        instance.selectedDate = validated_data.get('selectedDate', instance.selectedDate)
        instance.selectedTime = validated_data.get('selectedTime', instance.selectedTime)
        instance.save()

        user_info = instance.user_info
        user_info.firstName = user_info_data.get('firstName', user_info.firstName)
        user_info.lastName = user_info_data.get('lastName', user_info.lastName)
        user_info.phoneNumber = user_info_data.get('phoneNumber', user_info.phoneNumber)
        user_info.email = user_info_data.get('email', user_info.email)
        user_info.gatuAdress = user_info_data.get('gatuAdress', user_info.gatuAdress)
        user_info.postNummer = user_info_data.get('postNummer', user_info.postNummer)
        user_info.postOrt = user_info_data.get('postOrt', user_info.postOrt)
        user_info.save()

        return instance

    def get_total_pris(self, obj):
        #start with the base amount
        total_pris = obj.totalAmount + obj.serviceAvgift
        
        return total_pris


class FonsterputsSerializer(serializers.ModelSerializer):
    windows = WindowsFonsterputsSerializer()
    user_info = UserInfoFonsterputsSerializer()
    total_pris = serializers.SerializerMethodField()

    class Meta:
        model = Fonsterputs
        fields = [
            'id',
            'user_info',
            'hasKarmtvatt',
            'hasStegeBehovs',
            'commentFonster',
            'stegeAvgift',
            'totalAmount',
            'selectedDate',
            'selectedTime',
            'windows',
            'total_pris'
        ]

    def create(self, validated_data):
        windows_data = validated_data.pop('windows')
        user_info_data = validated_data.pop('user_info')
        service_request = Fonsterputs.objects.create(**validated_data)
        WindowsFonsterputs.objects.create(service_request=service_request, **windows_data)
        UserInfoFonsterputs.objects.create(service_request=service_request, **user_info_data)
        return service_request

    def update(self, instance, validated_data):
        windows_data = validated_data.pop('windows')
        user_info_data = validated_data.pop('user_info')

        
        instance.hasKarmtvatt = validated_data.get('hasKarmtvatt', instance.hasKarmtvatt)
        instance.hasStegeBehovs = validated_data.get('hasStegeBehovs', instance.hasStegeBehovs)
        instance.commentFonster = validated_data.get('commentFonster', instance.commentFonster)
        instance.stegeAvgift = validated_data.get('stegeAvgift', instance.stegeAvgift)
        instance.totalAmount = validated_data.get('totalAmount', instance.totalAmount)
        instance.selectedDate = validated_data.get('selectedDate', instance.selectedDate)
        instance.selectedTime = validated_data.get('selectedTime', instance.selectedTime)
        instance.save()

        windows = instance.windows
        windows.utanSprojs_count = windows_data.get('utanSprojs_count', windows.utanSprojs_count)
        windows.utanSprojs_sides = windows_data.get('utanSprojs_sides', windows.utanSprojs_sides)
        windows.medSprojs_count = windows_data.get('medSprojs_count', windows.medSprojs_count)
        windows.medSprojs_sides = windows_data.get('medSprojs_sides', windows.medSprojs_sides)
        windows.overhangda_count = windows_data.get('overhangda_count', windows.overhangda_count)
        windows.overhangda_sides = windows_data.get('overhangda_sides', windows.overhangda_sides)
        windows.balkong_count = windows_data.get('balkong_count', windows.balkong_count)
        windows.balkong_sides = windows_data.get('balkong_sides', windows.balkong_sides)
        windows.save()

        user_info = instance.user_info
        user_info.firstName = user_info_data.get('firstName', user_info.firstName)
        user_info.lastName = user_info_data.get('lastName', user_info.lastName)
        user_info.phoneNumber = user_info_data.get('phoneNumber', user_info.phoneNumber)
        user_info.email = user_info_data.get('email', user_info.email)
        user_info.gatuAdress = user_info_data.get('gatuAdress', user_info.gatuAdress)
        user_info.postNummer = user_info_data.get('postNummer', user_info.postNummer)
        user_info.postOrt = user_info_data.get('postOrt', user_info.postOrt)
        user_info.save()

        return instance

    def get_total_pris(self, obj):
        #start with the base amount
        total_pris = obj.totalAmount

        # conditionally add stegeAvgift
        if obj.hasStegeBehovs:
            total_pris += obj.stegeAvgift
        
        
        return total_pris
    

class KontorsstadningSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Kontorsstadning
        fields = [
            'id',
            'foretagsNamn',
            'orgNum',
            'firstName',
            'lastName',
            'phoneNumber',
            'email',
            'gatuAdress',
            'postNummer',
            'postOrt',
            'kommentar'
        ]


class TrappstadningSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trappstadning
        fields = [
            'id',
            'foretagsNamn',
            'orgNum',
            'firstName',
            'lastName',
            'phoneNumber',
            'email',
            'gatuAdress',
            'postNummer',
            'postOrt',
            'kommentar'
        ]