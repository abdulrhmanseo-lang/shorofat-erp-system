from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    """نموذج الأقسام"""
    
    name = models.CharField(
        max_length=100,
        verbose_name='اسم القسم'
    )
    
    description = models.TextField(
        blank=True,
        verbose_name='الوصف'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ الإنشاء'
    )
    
    class Meta:
        verbose_name = 'قسم'
        verbose_name_plural = 'الأقسام'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class User(AbstractUser):
    """نموذج المستخدم المخصص"""
    
    ROLE_CHOICES = [
        ('SUPER_ADMIN', 'مدير النظام'),
        ('ADMIN', 'مدير'),
        ('MANAGER', 'مدير قسم'),
        ('EMPLOYEE', 'موظف'),
        ('CLIENT', 'عميل'),
    ]
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='EMPLOYEE',
        verbose_name='الدور'
    )
    
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='رقم الهاتف'
    )
    
    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True,
        verbose_name='صورة الملف الشخصي'
    )
    
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
        verbose_name='القسم'
    )
    
    is_active_employee = models.BooleanField(
        default=True,
        verbose_name='موظف نشط'
    )
    
    class Meta:
        verbose_name = 'مستخدم'
        verbose_name_plural = 'المستخدمون'
        ordering = ['-date_joined']
    
    def __str__(self):
        return f"{self.get_full_name()} - {self.get_role_display()}"
    
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    @property
    def is_admin(self):
        return self.role in ['SUPER_ADMIN', 'ADMIN']
    
    @property
    def is_manager(self):
        return self.role == 'MANAGER'
    
    @property
    def is_employee_role(self):
        return self.role == 'EMPLOYEE'
    
    @property
    def is_client(self):
        return self.role == 'CLIENT'


class Permission(models.Model):
    """نموذج الصلاحيات"""
    
    name = models.CharField(
        max_length=100,
        verbose_name='اسم الصلاحية'
    )
    
    codename = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='الكود'
    )
    
    description = models.TextField(
        blank=True,
        verbose_name='الوصف'
    )
    
    class Meta:
        verbose_name = 'صلاحية'
        verbose_name_plural = 'الصلاحيات'
    
    def __str__(self):
        return self.name


class Role(models.Model):
    """نموذج الأدوار"""
    
    name = models.CharField(
        max_length=100,
        verbose_name='اسم الدور'
    )
    
    permissions = models.ManyToManyField(
        Permission,
        related_name='roles',
        blank=True,
        verbose_name='الصلاحيات'
    )
    
    users = models.ManyToManyField(
        User,
        related_name='custom_roles',
        blank=True,
        verbose_name='المستخدمون'
    )
    
    class Meta:
        verbose_name = 'دور'
        verbose_name_plural = 'الأدوار'
    
    def __str__(self):
        return self.name