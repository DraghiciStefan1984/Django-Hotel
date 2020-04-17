from django.db import models


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'


PROPERTY_TYPE=(
    ('S', 'sale'),
    ('R', 'rent')
)

class Property(models.Model):
    name=models.CharField(max_length=50)
    property_type=models.CharField(choices=PROPERTY_TYPE, max_length=10)
    price=models.PositiveIntegerField()
    category=models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    area=models.DecimalField(decimal_places=2, max_digits=5)
    beds_number=models.PositiveIntegerField()
    baths_number=models.PositiveIntegerField()
    garages_number=models.PositiveIntegerField()
    image=models.ImageField(upload_to='properties', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Property'
        verbose_name_plural='Properties'

