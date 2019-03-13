from django.db import models
import django.utils.timezone

class Puser(models.Model):
	user_id=models.CharField(max_length=30,primary_key='true')
	user_name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	phoneno=models.CharField(max_length = 30);
	bdate=models.DateTimeField();
	password=models.CharField(max_length=20)