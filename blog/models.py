from django.db import models
from ckeditor.fields import RichTextField
#
# from blog.utils import image_files


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    description = RichTextField(max_length=600)
    image = models.ImageField(upload_to="blogs", null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

