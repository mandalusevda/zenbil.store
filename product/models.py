from django.db import models
import datetime
import django
# from django.contrib.postgres.fields import ArrayField
# Create your models here.
class product1(models.Model):
    pic=models.ImageField(upload_to ='uploads/',height_field=None,width_field=None,max_length=100,null=True,blank=True)
    title=models.CharField(max_length=300)
    size=models.IntegerField()
    price=models.IntegerField()
    body=models.TextField()
    cdate=models.DateTimeField(default=django.utils.timezone.now)
    # default="false"
    # sortx=models.ArrayField()
    # Marketer = models.ForeignKey(User, on_delete=models.CASCADE)
    def namex(self):
        return self.name
    def captionx(self):
        return self.caption[:100]
    def date(self):
        return self.cdate.strftime('%b %e %Y')

# class product2(models.Model):
#     title=models.CharField(max_length=300)
#     size=models.IntegerField()
#     price=models.IntegerField()
#     body=models.TextField()
#     cdate=models.DateTimeField(default=django.utils.timezone.now)
#     pic=models.ImageField(upload_to ='uploads/',height_field=None,width_field=None,max_length=100,null=True,blank=True)
#     # sorty=models.Array()
#     # Marketer = models.ForeignKey(User, on_delete=models.CASCADE)
#     def namex(self):
#         return self.name
#     def captionx(self):
#         return self.caption[:100]
#     def date(self):
#         return self.cdate.strftime('%b %e %Y')
