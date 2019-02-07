from django.db import models

# Create your models here.



class Problem(models.Model):
    problem_name = models.CharField(max_length=120)
    problem_description = models.TextField()
    problem_level = models.CharField(max_length=120)
    problem_sampleInput = models.CharField(max_length=120)
    problem_sampleOutput = models.CharField(max_length=120)
    problem_main_file = models.FileField()
    problem_testcase_file = models.FileField()
    problem_body_file = models.FileField()

class Text(models.Model):
    text_box = models.CharField(max_length=100)




