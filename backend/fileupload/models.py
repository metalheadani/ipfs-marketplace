from django.db import models
from django.contrib.auth.models import User


class FileUpload(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=250 ,blank=False, null=False)
	price = models.DecimalField(max_digits=7, decimal_places=5, default=0)
	ethaddress = models.CharField(max_length=250 ,blank=False, null=False)
	file = models.FileField(upload_to='files/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return '{}, {}, {}'.format(self.user.username, self.name, self.file)


class IpfsAddress(models.Model):
	file = models.ForeignKey(FileUpload, on_delete=models.CASCADE)
	value = models.CharField(max_length=250 ,blank=False, null=False)
	#blockchain_hash = models.CharField(max_length=250 ,blank=False, null=False)

	def __str__(self):
		return '{}, {}'.format(self.file.user.username, self.file.name)

