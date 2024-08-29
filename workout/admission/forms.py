from django.forms import ModelForm
from . models import Admissioninfo

class Admissionform(ModelForm):
    
    class Meta:
        model = Admissioninfo
        fields = ('__all__')
