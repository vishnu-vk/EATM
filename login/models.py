from django.db import models

# Create your models here.


class Accounts(models.Model):
    Id=models.IntegerField(primary_key=True,default=0000)
    Acc_number=models.BigIntegerField(null=False)
    Acc_name=models.CharField(max_length=50,null=False)
    Bank=models.CharField(max_length=3,null=False)
    Acc_balance=models.FloatField(null=False,default=0.0)

    def __int__(self):
        return self.Id