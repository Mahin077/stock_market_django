from django.db import models

# Create your models here.
class StockMarket(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=18)
    high = models.DecimalField(decimal_places=1,max_digits=8)
    low = models.DecimalField(decimal_places=1,max_digits=8)
    open = models.DecimalField(decimal_places=1,max_digits=8)
    close = models.DecimalField(decimal_places=1,max_digits=8)
    volume = models.IntegerField()

    def __str__(self):
        return self.trade_code+str(self.date)