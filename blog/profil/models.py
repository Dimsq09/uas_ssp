from django.db import models

# Create your models here.
# Model Jenis harus didefinisikan dulu
class Jenis(models.Model):
    nama = models.CharField(max_length=20)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kdbrg = models.CharField(max_length=8)
    nama = models.CharField(max_length=50)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gbr = models.CharField(max_length=150, blank=True)
    tgl_input = models.DateTimeField(auto_now_add=True)
    id_jenis = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama

class About(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()

    def __str__(self):
        return self.judul
    
# Model untuk kontak
class Contact(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.nama} - {self.email}"

class ContactMessage(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    subjek = models.CharField(max_length=255)
    pesan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama} - {self.subjek}"

# Model untuk Certificate
class Certificate(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=100)
    image = models.ImageField(upload_to='certificates/')
    certificate_file = models.FileField(upload_to='certificates/files/', blank=True, null=True)
    date_earned = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_earned']

# Model untuk Project
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=300, help_text="Comma-separated list of technologies used")
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, help_text="Show in showcase carousel")
    order = models.IntegerField(default=0, help_text="Order in showcase (lower numbers first)")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order', '-created_at']

    def get_technologies_list(self):
        """Returns technologies as a list"""
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]
    
class Profile(models.Model):
    judul = models.CharField(max_length=200, default="Tentang Saya")
    nama = models.CharField(max_length=100)
    semester = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=100)
    universitas = models.CharField(max_length=100)
    deskripsi_utama = models.TextField(help_text="Paragraf pembuka tentang diri Anda")
    deskripsi_skill = models.TextField(help_text="Paragraf tentang skill yang sedang dikembangkan")
    teknologi_kiri = models.TextField(help_text="Teknologi kolom kiri (pisahkan dengan koma)")
    teknologi_kanan = models.TextField(help_text="Teknologi kolom kanan (pisahkan dengan koma)")
    deskripsi_hobi = models.TextField(help_text="Paragraf tentang hobi dan aktivitas di luar kuliah")
    foto_profil = models.ImageField(upload_to='profile/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile - {self.nama}"
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def get_teknologi_kiri_list(self):
        """Returns left technologies as a list"""
        return [tech.strip() for tech in self.teknologi_kiri.split(',') if tech.strip()]
    
    def get_teknologi_kanan_list(self):
        """Returns right technologies as a list"""
        return [tech.strip() for tech in self.teknologi_kanan.split(',') if tech.strip()]