# Generated by Django 3.0.5 on 2020-06-29 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_libros_tipo_despacho_tipo_pago'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('mensaje', models.CharField(default='', max_length=50)),
            ],
        ),
    ]