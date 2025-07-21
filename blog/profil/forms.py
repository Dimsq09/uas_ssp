from django.forms import ModelForm
from . models import Barang, Certificate, Project
from django import forms
from .models import Contact
from .models import Profile

class FormBarang(ModelForm):
    class Meta:
        model= Barang
        fields= '__all__'
        widgets = {
            'kdbrg': forms.TextInput(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control'}),
            'link_gbr': forms.URLInput(attrs={'class': 'form-control'}),
            'id_jenis': forms.Select(attrs={'class': 'form-control'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nama', 'email', 'subject', 'message']

class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'certificate_file': forms.FileInput(attrs={'class': 'form-control'}),
            'date_earned': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'github_link': forms.URLInput(attrs={'class': 'form-control'}),
            'live_demo_link': forms.URLInput(attrs={'class': 'form-control'}),
            'technologies': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'HTML, CSS, JavaScript, Python, etc.'
            }),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'semester': forms.TextInput(attrs={'class': 'form-control'}),
            'jurusan': forms.TextInput(attrs={'class': 'form-control'}),
            'universitas': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi_utama': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'deskripsi_skill': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'teknologi_kiri': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'TypeScript, React.js, Unity'
            }),
            'teknologi_kanan': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Python, Java, AR.js'
            }),
            'deskripsi_hobi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'foto_profil': forms.FileInput(attrs={'class': 'form-control'}),
        }