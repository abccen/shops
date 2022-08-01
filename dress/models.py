from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# class Seasons(models.Model):
#     winter = 'Winter'
#     summer = 'Summer'
#     spring = 'Spring'
#     autumn = 'Autumn'
#     seasons = [
#         (winter,'Winter'),
#         (summer,'Summer'),
#         (spring,'Spring'),
#         (autumn,'Autumn')
#     ]
#     seasons = models.CharField(max_length=10, choices=seasons, blank=True, null=True)
#
#     def __str__(self):
#         return self.seasons


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    winter = 'Winter'
    summer = 'Summer'
    spring = 'Spring'
    autumn = 'Autumn'
    seasons = [
        (winter, 'Winter'),
        (summer, 'Summer'),
        (spring, 'Spring'),
        (autumn, 'Autumn')
    ]
    seasons = models.CharField(max_length=12, choices=seasons, blank=True, null=True)
    xs = 'XS'
    s = 'S'
    m = 'M'
    l = 'L'
    xl = 'XL'
    height = [
        (xs, 'XS'),
        (s, 'S'),
        (m, 'M'),
        (l, 'L'),
        (xl, 'XL')
    ]
    height = models.CharField(max_length=3, choices=height, blank=True, null=True)
    image = models.ImageField(upload_to='shop_photo', blank=True)
    description = models.TextField()
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name











