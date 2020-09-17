from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'


	
	def save(self, *args, **kwargs):
		super().save( *args, **kwargs)

		img = Image.open(self.image.path)
		width, height = img.size
		#print(width, height)

		# check which one is smaller
		if height < width:
			# make square by cutting off equal amounts left and right
			left = (width - height) / 2
			right = (width + height) / 2
			top = 0
			bottom = height
			img = img.crop((left, top, right, bottom))
			img.thumbnail((300, 300))
			img.save(self.image.path)

		elif width < height:
			# make square by cutting from bottom
			left = 0
			right = width
			top = 0
			bottom = width
			img = img.crop((left, top, right, bottom))
			img.thumbnail((300, 300))

		img.save(self.image.path)