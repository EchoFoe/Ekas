from .models import *

def getting_privacy_policy(request):
    privacy_policy = PrivacyPolicy.objects.filter(is_active=True).last() #Ласт длает так, чтобы из несколько
    #  созданных использовалась последняя
    return locals()

def getting_bmk_objects(request):
    bmk_objects = BMKObjects.objects.filter(is_active=True).last() #Ласт длает так, чтобы из несколько
    #  созданных использовалась последняя
    return locals()

def getting_ekspertiza_objects(request):
    ekspertiza_objects = EkspertizaObjects.objects.filter(is_active=True).last() #Ласт длает так, чтобы из несколько
    #  созданных использовалась последняя
    return locals()