from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.db.models.deletion import CASCADE
from django.utils.html import mark_safe

# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, blank=True)
    username = models.CharField(max_length=500, null=True, blank=True)
    bio = models.CharField(max_length=500, null=True, blank=True,default='Hi! Im new user')
    photo = models.ImageField(upload_to="profilePicture",null=True,blank=True,default='profilePicture/profile-default-1.jpg')
    tel = models.CharField(max_length=500, null=False, blank=True)
    facebook = models.CharField(max_length=500, null=False, blank=True)
    twitter = models.CharField(max_length=500, null=False, blank=True)
    instagram = models.CharField(max_length=500, null=False, blank=True)
    website = models.CharField(max_length=500, null=False, blank=True)
    github = models.CharField(max_length=500, null=False, blank=True)
    usertype = models.CharField(max_length=100,default='member', choices=[('member','member'), ('admin','admin')])

    def __str__(self):
        # return self.user.first_name + ' ' + str(self.user.last_name)
        return '%s %s' % (self.user.first_name, self.user.last_name)

    def __str__(self):
        return "ลำดับ : " + str(self.id) + ' | ' "โปรไฟล์ของ : "  + str(self.user.first_name) + '  ' + str(self.user.last_name)

class Province (models.Model):
    prov_name = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.prov_name

class Post (models.Model):
    thumbnail = models.ImageField(upload_to="postimage/",null=True,blank=False)
    title = models.CharField(max_length=255,null=True, blank=False)
    prov = models.ForeignKey(Province,on_delete=models.CASCADE,null=True, blank=True)
    location = models.CharField(max_length=255,null=True, blank=True)
    location2 = models.CharField(max_length=255,null=True, blank=True)
    location3 = models.CharField(max_length=255,null=True, blank=True)
    location4 = models.CharField(max_length=255,null=True, blank=True)
    position = models.CharField(max_length=255,null=True, blank=False)
    Intern_type = models.CharField(max_length=255,null=False, blank=False, choices=[('1-2 เดือน','1-2 เดือน'),('2-3 เดือน','2-3 เดือน'),('3-4 เดือน','3-4 เดือน'),('4-5 เดือน','4-5 เดือน'),('6 เดือนขึ้นไป','6 เดือนขึ้นไป')])
    money = models.IntegerField(default=1, blank=True)
    money_type = models.CharField(max_length=255,null=True, blank=True, choices=[('วัน','วัน'),('สัปดาห์','สัปดาห์'),('เดือน','เดือน')])
    introduce = models.CharField(max_length=1000,null=True, blank=False)
    body = RichTextField(blank=False,null=True)
    body2 = RichTextField(blank=False,null=True)
    body3 = RichTextField(blank=False,null=True)
    body4 = RichTextField(blank=False,null=True)
    body5 = RichTextField(blank=False,null=True)
    rating = models.CharField(max_length=255,null=False, blank=False, choices=[('น้อยมาก','น้อยมาก'),('น้อย','น้อย'),('ปานกลาง','ปานกลาง'),('มาก','มาก'),('มากที่สุด','มากที่สุด')])
    post_date = models.DateField(auto_now_add=True)
    createBy = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, null=True)
    likes = models.ManyToManyField(Profile, blank=True, related_name='likes')
    active = models.BooleanField(default=False)
    
    def __str__(self):
        # return self.title + ' | ' + str(self.createBy) + ' ' + str(self.post_date) + ' | ' + str(self.id)
        return "เนื้อหาที่ : " + str(self.id) + ' | ' "ชื่อเนื้อหา : " + str(self.title) + ' | ' "เจ้าของเนื้อหา : " + str(self.createBy) + ' | ' "วันที่ลงเนื้อหา : " + str(self.post_date)


    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('article-detail', args=[self.id])

    
class otherPostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE)
    image = models.ImageField(upload_to="otherPostImage/",null=True,blank=True)
    image_name = models.CharField(max_length=100)

    def __str__(self):
        return "รูปที่ : " + str(self.id) + ' | ' "ชื่อรูป : " + str(self.image_name) + ' | ' "จากเนื้อหา : " + str(self.post.title)

class internWorks(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE)
    work = models.CharField(max_length=500 ,null=True,blank=True)
    work_name = models.CharField(max_length=500 ,null=True,blank=True)
    work_detail = models.CharField(max_length=1000 ,null=False,blank=True)

    def __str__(self):
        return "ลิงก์ที่ : " + str(self.id) + ' | ' "ชื่อลิงก์ : " + str(self.work_name) + ' | ' "จากเนื้อหา : " + str(self.post.title)

class Bookmark(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bookmark = models.ForeignKey(Post, on_delete=models.CASCADE)
    bookmarkId = models.IntegerField(null=True)

    def __str__(self):
        return "บันที่กที่ : " + str(self.id) + ' | ' "ชื่อเนื้อหา : " + str(self.bookmark.title) + ' | ' "บันทึกโดย : " + str(self.user.user.first_name) + '  ' + str(self.user.user.last_name)

class Comment (models.Model):
    user = models.ForeignKey(Profile, on_delete=CASCADE)
    comment = models.CharField(max_length=1000,null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    stamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.post)
