from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from .models import ContactMessage
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin
from .forms import CertificateForm, ProjectForm
from .models import Profile  # Tambahkan Profile ke import
from .forms import ProfileForm


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

# input model barang dan jenis 
from . models import Barang, Jenis, About, Contact, Certificate, Project

# Register your models here.
class BarangAdmin(admin.ModelAdmin):
    list_display = ('kdbrg', 'nama', 'stok', 'harga', 'link_gbr', 'tgl_input', 'id_jenis')
    list_filter = ('kdbrg', 'nama', 'id_jenis__nama')
    list_per_page = 3
    search_fields = ('id_jenis__nama',)

class CertificateAdmin(admin.ModelAdmin):
    form = CertificateForm
    list_display = ('title', 'organization', 'date_earned', 'created_at')
    list_filter = ('organization', 'date_earned')
    search_fields = ('title', 'organization')
    list_per_page = 10
    ordering = ['-date_earned']

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('title', 'technologies', 'is_featured', 'order', 'created_at')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('title', 'description', 'technologies')
    list_per_page = 10
    ordering = ['order', '-created_at']
    list_editable = ('is_featured', 'order')

class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    list_display = ('nama', 'jurusan', 'universitas', 'updated_at')
    list_filter = ('jurusan', 'universitas')
    search_fields = ('nama', 'jurusan', 'universitas')
    list_per_page = 10
    ordering = ['-updated_at']
    
    def has_add_permission(self, request):
        # Hanya izinkan satu profile
        return not Profile.objects.exists()

admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(ContactMessage)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile, ProfileAdmin)