from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage
from django.contrib import messages


def home(request):
     return render(request, 'index.html')

from django.shortcuts import render
from .forms import FormBarang

def portofolio(request):
    return render(request, 'index.html')

def form_barang(request):
    from_barang = FormBarang()
    return render(request, 'tambah.html', {'form_barang': from_barang})

#contact view
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'contact_success.html')
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})


def contact_view(request):
    if request.method == "POST":
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        subjek = request.POST.get('subjek')
        pesan = request.POST.get('pesan')

        if nama and email and subjek and pesan:
            ContactMessage.objects.create(
                nama=nama,
                email=email,
                subjek=subjek,
                pesan=pesan,
            )
            messages.success(request, "Pesan berhasil dikirim!")
            return redirect('home')  # redirect ke halaman home atau halaman lain
        else:
            messages.error(request, "Mohon lengkapi semua field!")
            return redirect('contact')

    return render(request, 'index.html')