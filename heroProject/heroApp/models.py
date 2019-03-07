from django.db import models

# Create your models here.

class HeroAppModel(models.Model):
    Name = models.CharField(max_length=200, default=0)
    Origin = models.CharField(max_length=200, default=0)
    question1 = models.CharField(max_length=200, default=0)
    question2 = models.CharField(max_length=200, default=0)
    question3 = models.CharField(max_length=200, default=0)
    question4 = models.TextField(max_length=1000, default=0)







#     Are you rich or have super powers?
# If you have a super power, which ones? (Flight, Speed, Invisibility, Telekenetic, Healing, Other)
# Which of the following are you? (Good, kinda good, neutral, a little evil, evil)
# Give us 3 examples of when you used your super hero abilities.