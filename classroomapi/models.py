from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
	subject = models.CharField(max_length=120)
	grade = models.IntegerField()
	year = models.CharField(max_length=40)
	teacher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.subject

class Student(models.Model):
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	dob = models.DateField()
	exam_grade = models.DecimalField(max_digits=5, decimal_places=2)
	classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)
	GENDERS = (
	('M', 'Male'),
    ('F', 'Female'),
	)
	gender = models.CharField(
		max_length = 2,
		choices = GENDERS,
		default = 'F',
	)

	def __str__(self):
		return self.first_name

	class Meta:
		ordering = ('first_name', 'exam_grade',)
