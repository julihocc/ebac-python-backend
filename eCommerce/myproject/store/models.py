from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cart(models.Model):
    products = models.ManyToManyField(Product)
    owner = models.CharField(max_length=255)
    total = models.FloatField(default=0.0)

    def add_product(self, product):
        self.products.add(product)
        self.save()

    def get_cart_total(self):
        self.total = sum(product.price for product in self.products.all())
        return self.total

    def checkout(self):
        total = self.get_cart_total()
        # This method should now return a string instead of printing it, 
        # as we'll use this return value in the view to pass to the template.
        return f"{self.owner}, your total is: ${total}. Proceeding to checkout."
