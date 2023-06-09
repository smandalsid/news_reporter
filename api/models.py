from django.db import models

# Create your models here.

class Google(models.Model):
    # primary=models.IntegerField(auto_created=True, primary_key=True, max_length=500)
    # _id=models.AutoField(primary_key=True)
    query=models.CharField(max_length=10, default="google", editable=False)
    batch=models.CharField(max_length=500, null=False, blank=False)
    title=models.TextField(unique=True, max_length=1000, null=False, blank=False)
    link=models.TextField(max_length=2000, null=False, blank=False)
    ago=models.DateField(null=False, blank=False)
    time=models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.title[:20]

class Apple(models.Model):
    # primary=models.IntegerField(auto_created=True, primary_key=True, max_length=500)
    # _id=models.AutoField(primary_key=True)
    query=models.CharField(max_length=10, default="apple", editable=False)
    batch=models.CharField(max_length=500, null=False, blank=False)
    title=models.TextField(unique=True, max_length=1000, null=False, blank=False)
    link=models.TextField(max_length=2000, null=False, blank=False)
    ago=models.DateField(null=False, blank=False)
    time=models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.title[:20]

class Microsoft(models.Model):
    # primary=models.IntegerField(auto_created=True, primary_key=True, max_length=500)
    # _id=models.AutoField(primary_key=True)
    query=models.CharField(max_length=10, default="microsoft", editable=False)
    batch=models.CharField(max_length=500, null=False, blank=False)
    title=models.TextField(unique=True, max_length=1000, null=False, blank=False)
    link=models.TextField(max_length=2000, null=False, blank=False)
    ago=models.DateField(null=False, blank=False)
    time=models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.title[:20]

class Meta(models.Model):
    
    query=models.CharField(max_length=10, default="meta", editable=False)
    batch=models.CharField(max_length=500, null=False, blank=False)
    title=models.TextField(unique=True, max_length=1000, null=False, blank=False)
    link=models.TextField(max_length=2000, null=False, blank=False)
    ago=models.DateField(null=False, blank=False)
    time=models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.title[:20]

