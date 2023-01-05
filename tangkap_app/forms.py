from django.forms import ModelForm
from django import forms
from .models import *

class FormTangkap(ModelForm):
    class Meta:
        model = Tangkap
        fields = '__all__'

        widgets = {
            'koordinat' : forms.TextInput({'class':'form-control', 'placeholder':'Koordinat', 'required':'required'}),
            'gambar' : forms.FileInput({'class':'form-control', 'placeholder':'Gambar', 'required':'required'}),
            'jenistangkapan' : forms.TextInput({'class':'form-control', 'placeholder':'Jenis', 'required':'required'}),
            'harga' : forms.TextInput({'class':'form-control', 'placeholder':'Harga', 'required':'required'}),    
            'jenis_id' : forms.Select({'class':'form-control', 'placeholder':'Jenis Tangkapan', 'required':'required'}),
        }


class FormNelayan(ModelForm):
    class Meta:
        model = Nelayan
        fields = '__all__'

        widgets = {
            'gambar' : forms.FileInput({'class':'form-control', 'placeholder':'Gambar', 'required':'required'}),
            'nama' : forms.TextInput({'class':'form-control', 'placeholder':'Nama Nelayan', 'required':'required'}),
            'tipe' : forms.TextInput({'class':'form-control', 'placeholder':'Tipe Nelayan', 'required':'required'}),
            'tentang' : forms.Textarea({'class':'form-control', 'placeholder':'Tentang Nelayan', 'required':'required'}),
            'usaha_id' : forms.Select({'class':'form-control', 'placeholder':'Usaha Nelayan', 'required':'required'}),
        }
        
