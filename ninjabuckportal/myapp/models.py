from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    buck_amount = models.IntegerField()
    belt = models.CharField(max_length=10)

    def __str__(self):
        self.fullname = str(self.first_name) + " " + str(self.last_name)
        return self.fullname

    def getUsername(self):
        self.username =  str(self.first_name) + "." + str(self.last_name)[0]
        return self.username

    def getBuck(self):
        return int(self.buck_amount)

    def getBelt(self):
        return str(self.belt)
