# Generated by Django 4.2.13 on 2024-07-07 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JenisProduk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
                ('gambar', models.ImageField(blank=True, null=True, upload_to='jenis_gambar/')),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_produk', models.CharField(max_length=100)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('gambar', models.ImageField(upload_to='produk_gambar/')),
                ('stok', models.PositiveIntegerField()),
                ('jenis_produk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produks', to='rivo.jenisproduk')),
            ],
        ),
    ]