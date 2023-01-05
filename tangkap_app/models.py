from django.db import models

# Create your models here.

class Jenis(models.Model):
   nama = models.CharField(max_length=100)
   keterangan = models.TextField()

   def __str__(self):
      return self.nama

class Tangkap(models.Model):
   koordinat = models.CharField(max_length=100)
   gambar = models.FileField(upload_to='map/', null=True)
   jenistangkapan = models.CharField(max_length=100)
   harga = models.CharField(max_length=100)
   jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)
   
   def __str__(self):
      return self.jenistangkapan



class Usaha(models.Model):
   nama = models.CharField(max_length=100)
   keterangan = models.TextField()

   def __str__(self):
      return self.nama

class Nelayan(models.Model):
   gambar = models.FileField(upload_to='nelayan/', null=True)
   nama = models.CharField(max_length=100)
   tipe = models.CharField(max_length=100)
   tentang = models.TextField()
   usaha_id = models.ForeignKey(Usaha, on_delete=models.CASCADE, null=True)
   
   def __str__(self):
      return self.nama
