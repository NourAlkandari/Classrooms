from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=120)
	date_of_birth = models.DateField()
	gender_choice = [("Female","Female"),("Male","Male")]
	gender = models.CharField(max_length=10, choices=gender_choice)
	exam_grade =models.DecimalField(max_digits=6,decimal_places=2)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
