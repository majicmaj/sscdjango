from django.db import models

# Create your models here.
class Listing(models.Model):
    title: models.CharField(max_length=120)
    price: models.IntegerField()
    quantity: models.IntegerField()
    category: models.CharField(max_length=120)
    image: models.CharField()
    description: models.TextField()
    label: models.CharField(max_length=3)


    def __str__(self):
        return self.title

    def get(self):
        return (
            self.title,
            self.price,
            self.category,
            self.image,
            self.description,
            self.label
            )
    def add_to_cart(self):
        return (self.id)
