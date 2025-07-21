from django.shortcuts import render, redirect
from .forms import ContactForm, FormBarang
from .models import ContactMessage, Certificate, Project, Profile  # Tambahkan Profile
from django.contrib import messages


def home(request):
    # Mengambil data certificate, projects, dan profile dari database
    certificates = Certificate.objects.all()
    projects = Project.objects.all()
    featured_projects = Project.objects.filter(is_featured=True)[:3]  # Max 3 for carousel
    
    # Mengambil profile (ambil yang pertama jika ada)
    profile = Profile.objects.first()
    
    context = {
        'certificates': certificates,
        'projects': projects,
        'featured_projects': featured_projects,
        'profile': profile,
    }
    return render(request, 'index.html', context)

def portofolio(request):
    certificates = Certificate.objects.all()
    projects = Project.objects.all()
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    profile = Profile.objects.first()
    
    context = {
        'certificates': certificates,
        'projects': projects,
        'featured_projects': featured_projects,
        'profile': profile,
    }
    return render(request, 'index.html', context)

def form_barang(request):
    if request.method == 'POST':
        form_barang = FormBarang(request.POST)
        if form_barang.is_valid():
            form_barang.save()
            messages.success(request, 'Data barang berhasil ditambahkan!')
            return redirect('tambah_barang')  # redirect ke halaman form lagi
        else:
            messages.error(request, 'Terjadi kesalahan saat menyimpan data.')
    else:
        form_barang = FormBarang()
    
    return render(request, 'Tambah.html', {'form_barang': form_barang})

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