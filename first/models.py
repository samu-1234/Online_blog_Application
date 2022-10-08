from multiprocessing import parent_process
from pydoc import describe
from django.db import models
#from django.forms import CharField
# Create your models here.


class Reg(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    pass1=models.CharField(max_length=50)
    re_pass=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    



class Login(models.Model):

    name=models.CharField(max_length=50)
    pass1=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class BlogInfo(models.Model):
    image = models.ImageField(upload_to="./Images")
    title = models.CharField(max_length=50)
    description = models.TextField()
    post_type = models.CharField(max_length=20,choices=[('Online marketing','Online marketing'),('social media','social media'),('technology','technology'),('writting','writting')])

    def __str__(self):  
        return self.title

    def save(self , *args ,**kwargs):
        # self.slug = generate_slug(self.title)
        super(BlogInfo,self).save(*args,**kwargs)

class Comment(models.Model):
    # user = models.ForeignKey(user,on_delete=models.)
    # cmt=models.ForeignKey(BlogInfo,on_delete=models.CASCADE)
    content=models.TextField()
    
    def __str__(self):
        return self.content
    
    # blog=models.ForeignKey(BlogInfo,on_delete=models.CASCADE)
    # parent_comment=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    
