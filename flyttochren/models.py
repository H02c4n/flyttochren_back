from django.db import models

# Create your models here.


class ContactForm(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    tel = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}'s message : {self.message}"
    
    class Meta:
        verbose_name = 'Kontakt Form'
        verbose_name_plural = 'Kontakt Form'


class Flytt(models.Model):
    postnummerFrom = models.CharField(max_length=10, blank=True, verbose_name='Postnummer från')
    cityFrom = models.CharField(max_length=100, blank=True, verbose_name='Stad från')
    gatuAdressFrom = models.CharField(max_length=255, blank=True, verbose_name='Gatu Adress från')
    boendeTypFrom = models.CharField(max_length=50, choices=[('villaRadhus', 'villaRadhus'), ('lagenhet', 'lagenhet'), ('forrad', 'forrad')], default='villaRadhus')
    bostadsytaFrom = models.CharField(max_length=255, blank=True, verbose_name='Yta från')
    biutrymmenFrom = models.CharField(max_length=255, blank=True, verbose_name='Biutrymmen från')
    vaningFrom = models.CharField(max_length=255, blank=True, verbose_name='Våning från')
    hissFrom = models.CharField(max_length=255, blank=True, verbose_name='Hiss från')

    postnummerTo = models.CharField(max_length=10, blank=True, verbose_name='Postnummer till')
    cityTo = models.CharField(max_length=100, blank=True, verbose_name='Stad till')
    gatuAdressTo = models.CharField(max_length=255, blank=True, verbose_name='Gatu Adress till')
    boendeTypTo = models.CharField(max_length=50, choices=[('villaRadhus2', 'villaRadhus2'), ('lagenhet2', 'lagenhet2'), ('forrad2', 'forrad2')], default='villaRadhus2')
    bostadsytaTo = models.CharField(max_length=255, blank=True, verbose_name='Yta till')
    biutrymmenTo = models.CharField(max_length=255, blank=True, verbose_name='Biutrymmen till')
    vaningTo = models.CharField(max_length=255, blank=True, verbose_name='Våning till')
    hissTo = models.CharField(max_length=255, blank=True, verbose_name='Hiss till')

    kommentar = models.TextField(blank=True, verbose_name='kommentar')

    hasNedpacking = models.BooleanField(default=False, verbose_name='Nedpacking')
    hasUppacking = models.BooleanField(default=False, verbose_name='Uppacking')
    hasMagasinering = models.BooleanField(default=False, verbose_name='Magasinering')
    hasFlyttstad = models.BooleanField(default=False, verbose_name='Flyttstäd')
    hasAtervinning = models.BooleanField(default=False, verbose_name='Återvinning')
    selectedDate = models.DateField(null=True, blank=True, verbose_name='Flyttdatum')
    selectedTime = models.TimeField(null=True, blank=True, verbose_name='Flytttid')


class Storstadning(models.Model):
    bostadsyta = models.CharField(max_length=255, blank=True)
    husdjur = models.CharField(max_length=50, choices=[('no', 'no'), ('yes', 'yes')], default='no')
    hasKatt = models.BooleanField(default=False, verbose_name='Katt')
    hasHund = models.BooleanField(default=False, verbose_name='Hund')
    hasAnnat = models.BooleanField(default=False, verbose_name='Annat')
    fonsterputs = models.CharField(max_length=50, choices=[('no','no'),('yes','yes')], default='no')
    hasKarmtvatt = models.BooleanField(default=False, verbose_name='Karmtvätt')
    hasStegeBehovs = models.BooleanField(default=False, verbose_name='Stege')
    hasStadutrustning = models.BooleanField(default=False, verbose_name='Städutrustning')
    ovenCount = models.IntegerField(default=0, verbose_name='Ugnsrengöring')
    fridgeCount = models.IntegerField(default=0, verbose_name='Kylskåpsrengöring')
    comment = models.TextField(blank=True, verbose_name='kommentar')
    commentFonster = models.TextField(blank=True, verbose_name='kommentar för fönster')
    keyStatus = models.CharField(max_length=50, choices=[('atHome', 'atHome'), ('willLeaveOneDayBefore', 'willLeaveOneDayBefore'),('alreadyLeftKey', 'alreadyLeftKey')], default='atHome')
    utrustningAvgift = models.IntegerField(default=350)
    serviceAvgift = models.IntegerField(default=70)
    stegeAvgift = models.IntegerField(default=350)
    totalAmount = models.IntegerField()
    selectedDate = models.DateField(null=True, blank=True, verbose_name='Date')
    selectedTime = models.TimeField(null=True, blank=True, verbose_name='Time')

    def __str__(self):
        # If UserInfo exists, return the first name; otherwise, return a default string.
        full_name = self.user_info.firstName +' '+self.user_info.lastName
        return f"Storstädningsförfrågan av {full_name if hasattr(self, 'user_info') and self.user_info.firstName else 'Unknown'}"
    
    def total_pris(self):
        total_pris = self.serviceAvgift
        if self.hasStegeBehovs:
            total_pris += self.stegeAvgift
        if self.hasStadutrustning:
            total_pris += self.utrustningAvgift
        total_pris += self.totalAmount
        return total_pris

    total_pris.short_description = 'Total Pris'


class Hemstadning(models.Model):
    bostadsyta = models.CharField(max_length=255, blank=True)
    husdjur = models.CharField(max_length=50, choices=[('no', 'no'), ('yes', 'yes')], default='no')
    hasKatt = models.BooleanField(default=False, verbose_name='Katt')
    hasHund = models.BooleanField(default=False, verbose_name='Hund')
    hasAnnat = models.BooleanField(default=False, verbose_name='Annat')
    frekvens = models.CharField(max_length=50, choices=[('biweekly', 'biweekly'), ('weekly', 'weekly'),('monthly', 'monthly')], default='biweekly')
    totalAmount = models.IntegerField()
    selectedDate = models.DateField(null=True, blank=True, verbose_name='Date')
    selectedTime = models.TimeField(null=True, blank=True, verbose_name='Time')

    def __str__(self):
        #if UserInfo exists, return the first name; otherwise, return a default string.
        full_name = self.user_info.firstName +' '+ self.user_info.lastName
        return f"Hemstädningförfrågan av {full_name if hasattr(self, 'user_info') and self.user_info.firstName else 'Unknown'}"
    
    def total_pris(self):
        total_pris = self.totalAmount
        return total_pris
    
    total_pris.short_description = 'Total Pris'


class Flyttstadning(models.Model):
    bostadsyta = models.CharField(max_length=255, blank=True)
    keyStatus = models.CharField(max_length=50, choices=[('atHome', 'atHome'), ('willLeaveOneDayBefore', 'willLeaveOneDayBefore'),('alreadyLeftKey', 'alreadyLeftKey')], default='atHome')
    serviceAvgift = models.IntegerField(default=70)
    totalAmount = models.IntegerField()
    selectedDate = models.DateField(null=True, blank=True, verbose_name='Date')
    selectedTime = models.TimeField(null=True, blank=True, verbose_name='Time')

    def __str__(self):
        #if UserInfo exists, return the first name; otherwise, return a default string.
        full_name = self.user_info.firstName +' '+ self.user_info.lastName
        return f"Flyttstädningförfrågan av {full_name if hasattr(self, 'user_info') and self.user_info.firstName else 'Unknown'}"
    
    def total_pris(self):
        total_pris = self.totalAmount + self.serviceAvgift
        return total_pris
    
    total_pris.short_description = 'Total Pris'


class Fonsterputs(models.Model):
    hasKarmtvatt = models.BooleanField(default=False, verbose_name='Karmtvätt')
    hasStegeBehovs = models.BooleanField(default=False, verbose_name='Stege')
    stegeAvgift = models.IntegerField(default=350)
    commentFonster = models.TextField(blank=True, verbose_name='kommentar för fönster')
    totalAmount = models.IntegerField()
    selectedDate = models.DateField(null=True, blank=True, verbose_name='Date')
    selectedTime = models.TimeField(null=True, blank=True, verbose_name='Time')

    def __str__(self):
        #if UserInfo exists, return the first name; otherwise, return a default string.
        full_name = self.user_info.firstName +' '+ self.user_info.lastName
        return f"Fonsterputsförfrågan av {full_name if hasattr(self, 'user_info') and self.user_info.firstName else 'Unknown'}"
    
    def total_pris(self):
        total_pris = self.totalAmount
        if self.hasStegeBehovs:
            total_pris += self.stegeAvgift
        
        return total_pris
    
    total_pris.short_description = 'Total Pris'


class Windows(models.Model):
    service_request = models.OneToOneField(Storstadning, on_delete=models.CASCADE, related_name='windows')
    utanSprojs_count = models.IntegerField(default=0)
    utanSprojs_sides = models.IntegerField(default=4)
    medSprojs_count = models.IntegerField(default=0)
    medSprojs_sides = models.IntegerField(default=4)
    overhangda_count = models.IntegerField(default=0)
    overhangda_sides = models.IntegerField(default=4)
    balkong_count = models.IntegerField(default=0)
    balkong_sides = models.IntegerField(default=4, verbose_name='Helt eller Endast glasräcke')

    def __str__(self):
        parts = []

        if self.utanSprojs_count > 0:
            sides_desc = "dubbelsidiga" if self.utanSprojs_sides > 2 else "enkelsidiga"
            parts.append(f"utan_spröjs:{self.utanSprojs_count}-st =>{sides_desc}")

        if self.medSprojs_count > 0:
            sides_desc = "dubbelsidiga" if self.medSprojs_sides > 2 else "enkelsidiga"
            parts.append(f"med_spröjs:{self.medSprojs_count}-st=>{sides_desc}")

        if self.overhangda_count > 0:
            sides_desc = "dubbelsidiga" if self.overhangda_sides > 2 else "enkelsidiga"
            parts.append(f"överhängda:{self.overhangda_count}-st=>{sides_desc}")

        if self.balkong_count > 0:
            sides_desc = "Helt inglasad" if self.balkong_sides > 2 else "endast glasräcke"
            parts.append(f"balkong:{self.balkong_count}-st =>{sides_desc}")

        if len(parts) < 1:
            return "Ingen Fönsterputsning"

        return ", ".join(parts)

    class Meta:
        verbose_name = "Windows För Storstädning"
        verbose_name_plural = "Windows För Storstädning"

    
class WindowsFonsterputs(models.Model):
    service_request = models.OneToOneField(Fonsterputs, on_delete=models.CASCADE, related_name='windows')
    utanSprojs_count = models.IntegerField(default=0)
    utanSprojs_sides = models.IntegerField(default=4)
    medSprojs_count = models.IntegerField(default=0)
    medSprojs_sides = models.IntegerField(default=4)
    overhangda_count = models.IntegerField(default=0)
    overhangda_sides = models.IntegerField(default=4)
    balkong_count = models.IntegerField(default=0)
    balkong_sides = models.IntegerField(default=4, verbose_name='Helt eller Endast glasräcke')

    def __str__(self):
        parts = []

        if self.utanSprojs_count > 0:
            sides_desc = "dubbelsidiga" if self.utanSprojs_sides > 2 else "enkelsidiga"
            parts.append(f"utan_spröjs:{self.utanSprojs_count}-st =>{sides_desc}")

        if self.medSprojs_count > 0:
            sides_desc = "dubbelsidiga" if self.medSprojs_sides > 2 else "enkelsidiga"
            parts.append(f"med_spröjs:{self.medSprojs_count}-st=>{sides_desc}")

        if self.overhangda_count > 0:
            sides_desc = "dubbelsidiga" if self.overhangda_sides > 2 else "enkelsidiga"
            parts.append(f"överhängda:{self.overhangda_count}-st=>{sides_desc}")

        if self.balkong_count > 0:
            sides_desc = "Helt inglasad" if self.balkong_sides > 2 else "endast glasräcke"
            parts.append(f"balkong:{self.balkong_count}-st =>{sides_desc}")

        return ", ".join(parts)
    
    class Meta:
        verbose_name = "Windows För Fönsterputs"
        verbose_name_plural = "Windows För Fönsterputs"


class UserInfo(models.Model):
    service_request = models.OneToOneField(Storstadning, on_delete=models.CASCADE, related_name='user_info')
    firstName = models.CharField(max_length=100, blank=True, verbose_name='Förnamn')
    lastName = models.CharField(max_length=100, blank=True, verbose_name='Efternamn')
    phoneNumber = models.CharField(max_length=15, blank=True, verbose_name='Telefonnummer')
    email = models.EmailField(blank=True, verbose_name='Epost')
    gatuAdress = models.CharField(max_length=255, blank=True, verbose_name='Gatu Adress')
    postNummer = models.CharField(max_length=10, blank=True, verbose_name='Postnummer')
    postOrt = models.CharField(max_length=100, blank=True, verbose_name='Post Ort')

    def __str__(self):
        return f"{self.firstName} {self.lastName} - Storstäd-ID:{self.service_request.id}"
    
    class Meta:
        verbose_name = "User Info För Storstädning"
        verbose_name_plural = "User Info För Storstädning"


class UserInfoHemstadning(models.Model):
    service_request = models.OneToOneField(Hemstadning, on_delete=models.CASCADE, related_name='user_info')
    firstName = models.CharField(max_length=100, blank=True, verbose_name='Förnamn')
    lastName = models.CharField(max_length=100, blank=True, verbose_name='Efternamn')
    phoneNumber = models.CharField(max_length=15, blank=True, verbose_name='Telefonnummer')
    email = models.EmailField(blank=True, verbose_name='Epost')
    gatuAdress = models.CharField(max_length=255, blank=True, verbose_name='Gatu Adress')
    postNummer = models.CharField(max_length=10, blank=True, verbose_name='Postnummer')
    postOrt = models.CharField(max_length=100, blank=True, verbose_name='Post Ort')

    def __str__(self):
         return f"{self.firstName} {self.lastName} - Hemstäd-ID:{self.service_request.id}"
    
    class Meta:
        verbose_name = "User Info För Hemstädning"
        verbose_name_plural = "User Info För Hemstädning"


class UserInfoFonsterputs(models.Model):
    service_request = models.OneToOneField(Fonsterputs, on_delete=models.CASCADE, related_name='user_info')
    firstName = models.CharField(max_length=100, blank=True, verbose_name='Förnamn')
    lastName = models.CharField(max_length=100, blank=True, verbose_name='Efternamn')
    phoneNumber = models.CharField(max_length=15, blank=True, verbose_name='Telefonnummer')
    email = models.EmailField(blank=True, verbose_name='Epost')
    gatuAdress = models.CharField(max_length=255, blank=True, verbose_name='Gatu Adress')
    postNummer = models.CharField(max_length=10, blank=True, verbose_name='Postnummer')
    postOrt = models.CharField(max_length=100, blank=True, verbose_name='Post Ort')

    def __str__(self):
         return f"{self.firstName} {self.lastName} - Fönsterputs-ID:{self.service_request.id}"
    
    class Meta:
        verbose_name = "User Info För Fönsterputs"
        verbose_name_plural = "User Info För Fönsterputs"


class UserInfoFlyttstadning(models.Model):
    service_request = models.OneToOneField(Flyttstadning, on_delete=models.CASCADE, related_name='user_info')
    firstName = models.CharField(max_length=100, blank=True, verbose_name='Förnamn')
    lastName = models.CharField(max_length=100, blank=True, verbose_name='Efternamn')
    phoneNumber = models.CharField(max_length=15, blank=True, verbose_name='Telefonnummer')
    email = models.EmailField(blank=True, verbose_name='Epost')
    gatuAdress = models.CharField(max_length=255, blank=True, verbose_name='Gatu Adress')
    postNummer = models.CharField(max_length=10, blank=True, verbose_name='Postnummer')
    postOrt = models.CharField(max_length=100, blank=True, verbose_name='Post Ort')

    def __str__(self):
         return f"{self.firstName} {self.lastName} - Flyttstädning-ID:{self.service_request.id}"
    
    class Meta:
        verbose_name = "User Info För Flyttstädning"
        verbose_name_plural = "User Info För Flyttstädning"


class UserInfoFlytt(models.Model):
    service_request = models.OneToOneField(Flytt, on_delete=models.CASCADE, related_name='user_info')
    firstName = models.CharField(max_length=100, blank=True, verbose_name='Förnamn')
    lastName = models.CharField(max_length=100, blank=True, verbose_name='Efternamn')
    phoneNumber = models.CharField(max_length=15, blank=True, verbose_name='Telefonnummer')
    email = models.EmailField(blank=True, verbose_name='Epost')

    def __str__(self):
        return f"{self.firstName} {self.lastName} - Flytt-ID:{self.service_request.id}"
    
    class Meta:
        verbose_name = "User Info För Flytt"
        verbose_name_plural = "User Info För Flytt"


class Kontorsstadning(models.Model):
    foretagsNamn = models.CharField(max_length=100, blank=True, verbose_name='FöretagsNamn')
    orgNum = models.CharField(max_length=100, blank=True, verbose_name='Organisationsnummer')
    firstName = models.CharField(max_length=100, blank=True, verbose_name='Förnamn')
    lastName = models.CharField(max_length=100, blank=True, verbose_name='Efternamn')
    phoneNumber = models.CharField(max_length=15, blank=True, verbose_name='Telefonnummer')
    email = models.EmailField(blank=True, verbose_name='Epost')
    gatuAdress = models.CharField(max_length=255, blank=True, verbose_name='Gatu Adress')
    postNummer = models.CharField(max_length=10, blank=True, verbose_name='Postnummer')
    postOrt = models.CharField(max_length=100, blank=True, verbose_name='Post Ort')
    kommentar = models.TextField(blank=True, verbose_name='kommentar')

    def __str__(self):
        return f"{self.foretagsNamn} {self.orgNum} - {self.kommentar}"
    
    class Meta:
        verbose_name = "Kontorsstädning"
        verbose_name_plural = "Kontorsstädning"


class Trappstadning(models.Model):
    foretagsNamn = models.CharField(max_length=100, blank=True, verbose_name='FöretagsNamn')
    orgNum = models.CharField(max_length=100, blank=True, verbose_name='Organisationsnummer')
    firstName = models.CharField(max_length=100, blank=True, verbose_name='Förnamn')
    lastName = models.CharField(max_length=100, blank=True, verbose_name='Efternamn')
    phoneNumber = models.CharField(max_length=15, blank=True, verbose_name='Telefonnummer')
    email = models.EmailField(blank=True, verbose_name='Epost')
    gatuAdress = models.CharField(max_length=255, blank=True, verbose_name='Gatu Adress')
    postNummer = models.CharField(max_length=10, blank=True, verbose_name='Postnummer')
    postOrt = models.CharField(max_length=100, blank=True, verbose_name='Post Ort')
    kommentar = models.TextField(blank=True, verbose_name='kommentar')

    def __str__(self):
        return f"{self.foretagsNamn} {self.orgNum} - {self.kommentar}"
    
    class Meta:
        verbose_name = "Trappstädning"
        verbose_name_plural = "Trappstädning"