from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from .models import ContactMessage

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


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
from . models import Barang, Jenis, About, Contact

# Register your models here.
class BarangAdmin(admin.ModelAdmin):
    list_display = ('kodebarang', 'nama', 'stok', 'harga', 'link_gambar', 'tgl_input', 'id_jenis')
    list_filter = ('kodebarang', 'nama', 'id_jenis__nama')
    list_per_page = 3
    search_fields = ('id_jenis__nama',)

admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(ContactMessage)
