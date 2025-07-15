from django.db import models

# Create your models here.
# Model Jenis harus didefinisikan dulu
class Jenis(models.Model):
    nama = models.CharField(max_length=20)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebarang = models.CharField(max_length=8)
    nama = models.CharField(max_length=50)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gambar = models.CharField(max_length=150, blank=True)
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