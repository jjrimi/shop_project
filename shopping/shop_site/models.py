from django.db import models
import base64

class Product(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_image_base64(self):
        if self.image:
            return base64.b64encode(self.image).decode('utf-8')
        else:
            return None

