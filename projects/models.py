from django.db import models
from django.urls import reverse

class ProjectCategory(models.Model):
    subject = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.subject}'

class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image1 = models.ImageField(upload_to='projects/%Y/%m/%d/')
    image2 = models.ImageField(upload_to='projects_sub/%Y/%m/%d/')
    image3 = models.ImageField(upload_to='projects_sub/%Y/%m/%d/', blank=True)
    estimate_cost = models.DecimalField(max_digits=10, decimal_places=2)
    commencement_date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('projects:detail', args=[self.id])
