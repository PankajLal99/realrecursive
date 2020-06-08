from django.db import models

class Exam(models.Model):
    name=models.CharField(max_length=100,blank=True, null=True)
    desc=models.TextField(blank=True, null=True)
    photo=models.ImageField(upload_to='images')
    

    def __str__(self):
        return str(self.name)

class Round(models.Model):
    name=models.CharField(max_length=100,blank=True, null=True)
    desc=models.TextField(blank=True, null=True)
    exam=models.ForeignKey(Exam,on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.name)

class Blog(models.Model):
    rounds=models.ForeignKey(Round,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=100,blank=True, null=True)
    desc=models.TextField(blank=True, null=True)
    solution=models.TextField(blank=True, null=True)
    created_on=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)

class newsletter(models.Model):
    email=models.EmailField()

    def __str__(self):
        return str(self.email)

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phno=models.CharField(max_length=11)
    msg=models.TextField()
    
    def __str__(self):
        return str(self.email)