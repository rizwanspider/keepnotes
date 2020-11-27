from django.db import models

# Create your models here.
class ModelNote(models.Model):
    title = models.CharField(max_length=100) 
    content = models.TextField()
    author = models.CharField(max_length=50) 
    published = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "notes"
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title