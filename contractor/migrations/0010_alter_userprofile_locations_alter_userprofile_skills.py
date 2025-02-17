# Generated by Django 4.2.18 on 2025-02-17 08:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0009_rename_content_contractorrating_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='locations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('abingdon', 'Abingdon'), ('aldershot', 'Aldershot'), ('alton', 'Alton'), ('andover', 'Andover'), ('ascot', 'Ascot'), ('basingstoke', 'Basingstoke'), ('banbury', 'Banbury'), ('bicester', 'Bicester'), ('bracknell', 'Bracknell'), ('carterton', 'Carterton'), ('chipping', 'Chipping Norton'), ('crowthorne', 'Crowthorne'), ('didcot', 'Didcot'), ('earley', 'Earley'), ('eastleigh', 'Eastleigh'), ('eton', 'Eton'), ('faringdon', 'Faringdon'), ('farnborough', 'Farnborough'), ('henley', 'Henley-on-Thames'), ('hungerford', 'Hungerford'), ('lymington', 'Lymington'), ('maidenhead', 'Maidenhead'), ('newbury', 'Newbury'), ('oxford', 'Oxford'), ('petersfield', 'Petersfield'), ('portsmouth', 'Portsmouth'), ('reading', 'Reading'), ('ringwood', 'Ringwood'), ('sandhurst', 'Sandhurst'), ('slough', 'Slough'), ('southampton', 'Southampton'), ('thame', 'Thame'), ('thatcham', 'Thatcham'), ('totton', 'Totton'), ('wallingford', 'Wallingford'), ('wantage', 'Wantage'), ('winchester', 'Winchester'), ('windsor', 'Windsor'), ('witney', 'Witney'), ('wokingham', 'Wokingham'), ('woodley', 'Woodley'), ('woodstock', 'Woodstock')], max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('bricklaying', 'Bricklaying'), ('carpentry', 'Carpentry'), ('carpeting', 'Carpet fitting'), ('cladding', 'Cladding'), ('decking', 'Decking'), ('drywall', 'Drywall installation and finishing'), ('electrical', 'Electrical'), ('fencing', 'Fencing'), ('flooring', 'Flooring'), ('gas', 'Gas engineering'), ('glazing', 'Glazing'), ('hvac', 'HVAC'), ('insulation', 'Insulation'), ('kitchen', 'Kitchen fitting'), ('labouring', 'Labouring'), ('landscaping', 'Landscaping'), ('leather', 'Leather sofa repair'), ('locksmith', 'Locksmith'), ('loft', 'Loft conversions'), ('van', 'Man with a van'), ('masonry', 'Masonry'), ('painting', 'Painting and decorating'), ('patio', 'Patio doors'), ('pest', 'Pest and vermin control'), ('plastering', 'Plastering'), ('plumbing', 'Plumbing'), ('power', 'Power washing'), ('roof', 'Roof cleaning'), ('roofing', 'Roofing'), ('shed', 'Sheds'), ('shower', 'Shower repairs'), ('tiling', 'Tiler'), ('tree', 'Tree Surgery'), ('upholstery', 'Upholstery cleaning'), ('wallpaper', 'Wallpaper hanging'), ('window', 'Window cleaning'), ('wiring', 'Wiring'), ('wood', 'Wood restoration')], max_length=100), blank=True, null=True, size=None),
        ),
    ]
