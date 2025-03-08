from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=15,default=99.99)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 1.1)
    
    def funny_number(self):
        return 12