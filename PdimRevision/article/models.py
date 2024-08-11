from django.db import models
from django.urls import reverse



class Articles(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    actif = models.BooleanField(default=False)
    image = models.ImageField(blank=True, upload_to='images')
   # date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=10)
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        
        def __str__(self):
            return self.name
    
    
    # la fonction de l'url absolute
    
    def get_absolute_url(self):
        return reverse("update", kwargs={"my_id": self.pk})
    
    
