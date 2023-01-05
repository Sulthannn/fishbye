from django.contrib import admin

# Register your models here.
from .models import *

class olahtangkap(admin.ModelAdmin):
    list_display = ['koordinat', 'gambar', 'jenistangkapan', 'harga']
    search_fields = ['koordinat', 'jenistangakapan']
    list_filter = ['jenis_id']
    list_per_page = 5

admin.site.register(Tangkap, olahtangkap)
admin.site.register(Jenis)

class olahnelayan(admin.ModelAdmin):
    list_display = ['nama', 'gambar', 'tipe', 'tentang']
    search_fields = ['nama', 'tipe']
    list_filter = ['usaha_id']
    list_per_page = 5

admin.site.register(Nelayan, olahnelayan)
admin.site.register(Usaha)