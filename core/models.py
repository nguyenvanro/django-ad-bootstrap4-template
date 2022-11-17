from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# from django.contrib.auth.models import UserManager
# Create your models here.
class TimeStampedModelMixin(models.Model):
    """
    Abstract Mixin model to add timestamp
    """
    created_at = models.DateTimeField(u"Date created_at",auto_now_add=True)
    updated_at = models.DateTimeField(u"Date updated_at",auto_now=True, db_index=True)

    class Meta:
        abstract = True  

class UserAccount(AbstractUser):
    ''' Thông tin cá nhân '''
    gender_choices = [
        ['Nam', 'Nam'],
        ['Nam', 'Nam'],
        ['Khác/Không trả lời', 'Khác/Không trả lời']
    ]
    gender = models.CharField(max_length=255,choices=gender_choices,blank=True,null=True, verbose_name='Giới tính')
    address = models.CharField(max_length=255, default='',blank=True,null=True, verbose_name='Địa chỉ')
    phonenumber = models.CharField(max_length=15,blank=True,null=True, verbose_name='Số điện thoại')
    dateofbirth = models.CharField(max_length=10,default='',blank=True,null=True, verbose_name = 'Ngày sinh')
    email = models.CharField(max_length=255,blank=True,null=True,verbose_name='Email address')
    is_lock = models.BooleanField(default=False, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.is_superuser:
            self.is_superuser = False
        super(UserAccount, self).save(*args, **kwargs)

    def full_name(self):
        try:
            full_name = str(self.last_name) + \
                        " " + str(self.first_name)
        except:
            full_name = ""
        return full_name.strip()


    def __str__(self):
        return str(self.username)
   

    class Meta:
        verbose_name_plural = '00. Danh sách người dùng'