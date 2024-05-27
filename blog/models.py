from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField('Zagolovok', max_length=255)
    text = models.TextField('Tekst Novosti')
    image = models.ImageField("Kartinka Posta", upload_to='post_img/')
    feature = models.BooleanField('v slaydere', default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    slug = models.SlugField('Ssilka', unique=True)
    created_at = models.DateTimeField('Data sozdaniya posta', default=timezone.now)

    class Meta:
        verbose_name = 'Novost'
        verbose_name_plural = "Novosti"

    def __str__(self):
        return self.title
    
    def get_link(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})
    
class Category(models.Model):    
    title = models.CharField('Nazvanie kategorii', max_length=255)
    image = models.ImageField('kartinka kategorii', upload_to='cat_img/')
    slug = models.SlugField('Ssilka',unique=True)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategorii'

    def __str__(self):
        return self.title 
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now) 
    text = models.TextField()  

    class Meta:
        verbose_name = 'Komentariy'
        verbose_name_plural = 'Komentarii'

    def __str__(self):    
        return self.author.username + ' ' + self.post.title



