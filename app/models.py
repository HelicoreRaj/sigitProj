from django.db import models

# Create your models here.

class CSVMaster(models.Model):
	CsvID=models.AutoField(primary_key=True)
	CsvName=models.FileField(upload_to='G:/SIGITApi')

	def __str__(self):
		return self.CsvName