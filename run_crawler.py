import os
import django

# تنظیم مسیر پروژه
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IranGardi.settings')
django.setup()

from attractions.crawler import EghamatCrawler

if __name__ == "__main__":
    print("شروع فرآیند کرولینگ...")
    results = EghamatCrawler.save_attractions()
    print("\nنتایج نهایی:")
    print(f"تعداد شهرهای پردازش شده: {results['total_cities']}")
    print(f"شهرهای موفق: {results['success']}")
    print(f"شهرهای ناموفق: {results['failed']}")
    print(f"جاذبه‌های اضافه شده: {results['attractions_added']}")
    print(f"جاذبه‌های به‌روز شده: {results['attractions_updated']}")