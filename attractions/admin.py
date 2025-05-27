from django.contrib import admin
from django.utils.html import format_html
from .models import City, Attraction

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'cit_id', 'created_at', 'updated_at')
    search_fields = ('name', 'cit_id')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'city', 
        'attraction_type',
        'get_coordinates_link',
        'is_active',
        'updated_at'
    )
    list_filter = ('city', 'attraction_type', 'is_active')
    search_fields = ('name', 'city__name', 'description')
    list_editable = ('is_active',)
    list_per_page = 25
    date_hierarchy = 'updated_at'
    fieldsets = (
        (None, {
            'fields': ('name', 'city', 'attraction_type', 'is_active')  
        }),
        ('مشخصات جغرافیایی', {
            'fields': ('latitude', 'longitude', 'address')
        }),
        ('اطلاعات تماس', {
            'fields': ('phone', 'website')
        }),
        ('توضیحات', {
            'fields': ('description',)
        }),
    )

    def get_coordinates_link(self, obj):
        if obj.latitude and obj.longitude:
            url = f"https://www.google.com/maps?q={obj.latitude},{obj.longitude}"
            return format_html('<a href="{}" target="_blank">مشاهده در نقشه</a>', url)
        return "نامشخص"
    get_coordinates_link.short_description = "مختصات"