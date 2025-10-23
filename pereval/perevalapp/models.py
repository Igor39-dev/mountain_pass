from django.db import models

class User(models.Model):
    email = models.EmailField()
    fam = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    otc = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Level(models.Model):
    winter = models.CharField(max_length=100, blank=True, null=True)
    summer = models.CharField(max_length=100, blank=True, null=True)
    autumn = models.CharField(max_length=100, blank=True, null=True)
    spring = models.CharField(max_length=100, blank=True, null=True)


class Pereval(models.Model):
    STATUS_CHOICES = (
        ('new', 'новый'), ('pending', 'в работе'),
        ('accepted', 'принят'), ('rejected', 'отклонён')
    )    
    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=100)
    connect = models.CharField(max_length=100, blank=True, null=True)
    add_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')


class Images(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
    data = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
