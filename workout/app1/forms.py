from django.forms import ModelForm
from . models import Studentinfo

class SForm(ModelForm):
    
    class Meta:
        model = Studentinfo
        fields = ('__all__')



