from django.db import models
from accounts.models import User
from django.utils import timezone


class Task(models.Model):
    """نموذج المهام"""
    
    STATUS_CHOICES = [
        ('TODO', 'قيد الانتظار'),
        ('IN_PROGRESS', 'قيد التنفيذ'),
        ('COMPLETED', 'مكتملة'),
        ('CANCELLED', 'ملغاة'),
    ]
    
    PRIORITY_CHOICES = [
        ('LOW', 'منخفضة'),
        ('MEDIUM', 'متوسطة'),
        ('HIGH', 'عالية'),
        ('URGENT', 'عاجلة'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='عنوان المهمة')
    description = models.TextField(verbose_name='الوصف')
    
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='مُسند إلى'
    )
    
    assigned_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assigned_tasks',
        verbose_name='مُسند بواسطة'
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='TODO',
        verbose_name='الحالة'
    )
    
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='MEDIUM',
        verbose_name='الأولوية'
    )
    
    due_date = models.DateTimeField(verbose_name='تاريخ الاستحقاق')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name='تاريخ الإنجاز')
    
    class Meta:
        verbose_name = 'مهمة'
        verbose_name_plural = 'المهام'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    @property
    def is_overdue(self):
        return self.due_date < timezone.now() and self.status != 'COMPLETED'


class Attendance(models.Model):
    """نموذج الحضور والانصراف"""
    
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='attendances',
        verbose_name='الموظف'
    )
    
    date = models.DateField(verbose_name='التاريخ')
    check_in = models.TimeField(verbose_name='وقت الحضور')
    check_out = models.TimeField(null=True, blank=True, verbose_name='وقت الانصراف')
    
    notes = models.TextField(blank=True, verbose_name='ملاحظات')
    
    is_late = models.BooleanField(default=False, verbose_name='متأخر')
    is_early_leave = models.BooleanField(default=False, verbose_name='انصراف مبكر')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'حضور'
        verbose_name_plural = 'الحضور والانصراف'
        ordering = ['-date']
        unique_together = ['employee', 'date']
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.date}"
    
    @property
    def working_hours(self):
        if self.check_out:
            from datetime import datetime, timedelta
            check_in_dt = datetime.combine(self.date, self.check_in)
            check_out_dt = datetime.combine(self.date, self.check_out)
            duration = check_out_dt - check_in_dt
            return duration.total_seconds() / 3600
        return 0


class Leave(models.Model):
    """نموذج الإجازات"""
    
    TYPE_CHOICES = [
        ('ANNUAL', 'إجازة سنوية'),
        ('SICK', 'إجازة مرضية'),
        ('EMERGENCY', 'إجازة طارئة'),
        ('UNPAID', 'إجازة بدون راتب'),
    ]
    
    STATUS_CHOICES = [
        ('PENDING', 'قيد المراجعة'),
        ('APPROVED', 'موافق عليها'),
        ('REJECTED', 'مرفوضة'),
    ]
    
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='leaves',
        verbose_name='الموظف'
    )
    
    leave_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        verbose_name='نوع الإجازة'
    )
    
    start_date = models.DateField(verbose_name='تاريخ البداية')
    end_date = models.DateField(verbose_name='تاريخ النهاية')
    
    reason = models.TextField(verbose_name='السبب')
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING',
        verbose_name='الحالة'
    )
    
    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_leaves',
        verbose_name='تمت الموافقة بواسطة'
    )
    
    approval_date = models.DateTimeField(null=True, blank=True, verbose_name='تاريخ الموافقة')
    rejection_reason = models.TextField(blank=True, verbose_name='سبب الرفض')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الطلب')
    
    class Meta:
        verbose_name = 'إجازة'
        verbose_name_plural = 'الإجازات'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.get_leave_type_display()}"
    
    @property
    def total_days(self):
        return (self.end_date - self.start_date).days + 1


class Payroll(models.Model):
    """نموذج كشوف المرتبات"""
    
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='payrolls',
        verbose_name='الموظف'
    )
    
    month = models.DateField(verbose_name='الشهر')
    
    basic_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='الراتب الأساسي'
    )
    
    allowances = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='البدلات'
    )
    
    deductions = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='الخصومات'
    )
    
    overtime_hours = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        verbose_name='ساعات إضافية'
    )
    
    overtime_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='مبلغ الساعات الإضافية'
    )
    
    net_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='الراتب الصافي'
    )
    
    is_paid = models.BooleanField(default=False, verbose_name='تم الدفع')
    payment_date = models.DateTimeField(null=True, blank=True, verbose_name='تاريخ الدفع')
    
    notes = models.TextField(blank=True, verbose_name='ملاحظات')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'كشف راتب'
        verbose_name_plural = 'كشوف المرتبات'
        ordering = ['-month']
        unique_together = ['employee', 'month']
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.month.strftime('%B %Y')}"
    
    def save(self, *args, **kwargs):
        # حساب الراتب الصافي تلقائياً
        self.net_salary = (
            self.basic_salary + 
            self.allowances + 
            self.overtime_amount - 
            self.deductions
        )
        super().save(*args, **kwargs)