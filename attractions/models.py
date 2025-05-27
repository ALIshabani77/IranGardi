from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now

class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="نام شهر")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="اسلاگ")
    created_at = models.DateTimeField(default=now, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    cit_id = models.IntegerField(null=True, blank=True, verbose_name="شناسه شهر اکسل")

    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهرها"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Attraction(models.Model):
    ATTRACTION_TYPES = (
        ('historical', 'تاریخی'),
        ('religious', 'مذهبی'),
        ('natural', 'طبیعی'),
        ('cultural', 'فرهنگی'),
        ('entertainment', 'تفریحی'),
    )

    name = models.CharField(max_length=200, verbose_name="نام جاذبه")
    city = models.ForeignKey(
        City, 
        on_delete=models.CASCADE, 
        related_name='attractions',
        verbose_name="شهر"
    )
    attraction_type = models.CharField(
        max_length=50, 
        choices=ATTRACTION_TYPES, 
        default='cultural',
        verbose_name="نوع جاذبه"
    )
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
        null=True,
        blank=True,
        verbose_name="عرض جغرافیایی"
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
        null=True,
        blank=True,
        verbose_name="طول جغرافیایی"
    )
    address = models.TextField(blank=True, null=True, verbose_name="آدرس")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="تلفن")
    website = models.URLField(blank=True, null=True, verbose_name="وبسایت")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    created_at = models.DateTimeField(default=now, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    

    class Meta:
        verbose_name = "جاذبه گردشگری"
        verbose_name_plural = "جاذبه‌های گردشگری"
        ordering = ['city', 'name']
        unique_together = ('name', 'city')

    def __str__(self):
        return f"{self.name} - {self.city.name}"

    def get_coordinates(self):
        if self.latitude and self.longitude:
            return f"{self.latitude}, {self.longitude}"
        return "نامشخص"