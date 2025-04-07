from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    buck_amount = models.IntegerField()
    BELT_CHOICES = {
    "White": "White",
    "Yellow": "Yellow",
    "Orange": "Orange",
    "Green": "Green",
    "Blue": "Blue",
    "Purple": "Purple",
    "Brown": "Brown",
    "Red": "Red",
    "Black": "Black",
    "ScratchJR": "ScratchJR"
    }
    belt = models.CharField(max_length=10, choices=BELT_CHOICES)

    def __str__(self):
        self.fullname = str(self.first_name) + " " + str(self.last_name)
        return self.fullname

    def getUsername(self):
        self.username =  str(self.first_name) + "." + str(self.last_name)[0]
        return self.username
    
    def getAmount(self):
        return int(self.buck_amount)
    
    def getBelt(self):
        return f"myapp/images/{self.belt}.png"
    


class Reward(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to='./images/', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def getName(self):
        return str(self.name)
    
    def getPrice(self):
        return int(self.price)
    
    def getImage(self):
        if self.image:
            return self.image.url
        return None