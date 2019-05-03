from django.db import models


# Create your models here.
class Landscape(models.Model):
    img = models.ImageField(
        upload_to='static/upload/landscape',
        verbose_name='风景')
    time = models.DateField(verbose_name='发表时间')
    #name = models.CharField(max_length=30,null=False,verbose_name='风景')
    title = models.CharField(max_length=50, null=False, verbose_name='标题')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'landscape'
        verbose_name = '风景'
        verbose_name_plural = verbose_name


class Life(models.Model):
    img = models.ImageField(
        upload_to='static/upload/life',
        verbose_name='生活')
    time = models.DateField(verbose_name='发表时间')
    # name = models.CharField(max_length=30,null=False,verbose_name='风景')
    title = models.CharField(max_length=50, null=False, verbose_name='标题')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'life'
        verbose_name = '生活'
        verbose_name_plural = verbose_name

class Food(models.Model):
    img = models.ImageField(
        upload_to='static/upload/food',
        verbose_name='美食')
    time = models.DateField(verbose_name='发表时间')
    # name = models.CharField(max_length=30,null=False,verbose_name='美食')
    title = models.CharField(max_length=50, null=False, verbose_name='标题')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'food'
        verbose_name = '美食'
        verbose_name_plural = verbose_name

class Happiness(models.Model):
    img = models.ImageField(
        upload_to='static/upload/happiness',
        verbose_name='心情')
    time = models.DateField(verbose_name='发表时间')
    # name = models.CharField(max_length=30,null=False,verbose_name='心情')
    title = models.CharField(max_length=50, null=False, verbose_name='标题')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'happiness'
        verbose_name = '心情'
        verbose_name_plural = verbose_name