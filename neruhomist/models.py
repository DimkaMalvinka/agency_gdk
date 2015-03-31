from django.db import models
from PIL import Image


class HouseType(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class SellType(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class House(models.Model):
	house_type = models.ForeignKey(HouseType)
	sell_type = models.ForeignKey(SellType)
	price = models.IntegerField()
	adress = models.CharField(max_length=255, blank=True)
	room_count = models.IntegerField()
	floor_count = models.IntegerField()
	ploshcha = models.IntegerField()
	rieltor_tel = models.IntegerField()
	about = models.TextField()
	def __str__(self):
		return self.adress

class HouseImage(models.Model):
    house = models.ForeignKey(House, related_name='images')
    image = models.ImageField(editable=True)
    def save(self):
        if not self.image:
            return            

        super(HouseImage, self).save()
        image1 = Image.open(self.image)
        (width, height) = image1.size     
        size = ( 300, 300)
        image1 = image1.resize(size, Image.ANTIALIAS)
        image1.save(self.image.path)


