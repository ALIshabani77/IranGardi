<div align="center">

# 🗺️ پروژه گردشگری ایران (IranGardi)

<a href="https://github.com/ALIshabani77/IranGardi">
  <img src="https://user-images.githubusercontent.com/56273934/183212873-c6514d7a-2661-4638-b11c-d38a096c4ead.png" alt="پروژه ایران گردی" width="800"/>
</a>

<br>

<p>
  یک ابزار هوشمند برای استخراج و جمع‌آوری اطلاعات جاذبه‌های گردشگری ایران از وب‌سایت‌ها با پایتون و جنگو.
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django" alt="Django">
  <img src="https://img.shields.io/badge/BeautifulSoup-4.x-orange?style=for-the-badge&logo=beautiful-soup" alt="BeautifulSoup">
  <img src="https://img.shields.io/badge/requests-2.x-brightgreen?style=for-the-badge&logo=python-requests" alt="Requests">
</p>

</div>

---

<details>
  <summary>📜 **فهرست مطالب**</summary>
  <ol>
    <li><a href="#-درباره-پروژه">درباره پروژه</a></li>
    <li><a href="#-ویژگی‌های-کلیدی">ویژگی‌های کلیدی</a></li>
    <li><a href="#-تکنولوژی‌های-استفاده-شده">تکنولوژی‌های استفاده شده</a></li>
    <li><a href="#-نصب-و-راه‌اندازی">نصب و راه‌اندازی</a></li>
    <li><a href="#-نحوه-استفاده">نحوه استفاده</a></li>
    <li><a href="#-مشارکت-در-پروژه">مشارکت در پروژه</a></li>
  </ol>
</details>

---

## 🚀 درباره پروژه

> **IranGardi** یک پروژه برای استخراج داده‌های جاذبه‌های گردشگری از وب‌سایت‌های ایرانی است. این سیستم با استفاده از اسکریپت‌های پایتون، اطلاعات را جمع‌آوری کرده، آن‌ها را طی یک فرآیند **ETL** (استخراج، تبدیل، بارگذاری) پاک‌سازی و پردازش می‌کند و در نهایت در یک پایگاه داده مبتنی بر **Django** ذخیره می‌نماید. هدف اصلی، ایجاد یک منبع داده‌ی تمیز و ساختاریافته از مکان‌های دیدنی ایران برای استفاده در سایر اپلیکیشن‌هاست.

## ✨ ویژگی‌های کلیدی

* 🌐 **Web Scraping:** جمع‌آوری هوشمند و خودکار داده‌ها از وب‌سایت‌های مرجع با استفاده از `BeautifulSoup` و `requests`.
* 🔄 **فرآیند ETL کامل:** شامل استخراج داده، پاک‌سازی اطلاعات ناقص، نگاشت انواع داده و بارگذاری در مدل‌های جنگو.
* 🗄️ **مدیریت پایگاه داده:** طراحی مکانیزم خودکار و تراکنشی برای ثبت و به‌روزرسانی اطلاعات شهرها و جاذبه‌ها.
* 📤 **خروجی JSON:** قابلیت تولید خروجی `JSON` استاندارد و ارسال آن به یک **REST API** دیگر.
* ⚙️ **مدیریت خطا و لاگ‌گیری:** پیاده‌سازی سیستم مدیریت خطا و ثبت لاگ برای شناسایی و گزارش داده‌های نامعتبر.

## 🛠️ تکنولوژی‌های استفاده شده

| دسته | تکنولوژی‌ها |
| :--- | :--- |
| **Backend** | `Python`, `Django` |
| **Web Scraping** | `BeautifulSoup`, `requests` |
| **Database** | `SQLite` (پیش‌فرض) |

## ⚙️ نصب و راه‌اندازی

برای اجرای این پروژه به صورت محلی، مراحل زیر را دنبال کنید:

1.  **کلون کردن ریپازیتوری:**
    ```bash
    git clone [https://github.com/ALIshabani77/IranGardi.git](https://github.com/ALIshabani77/IranGardi.git)
    cd IranGardi
    ```

2.  **ساخت و فعال‌سازی محیط مجازی:**
    ```bash
    # for Windows
    python -m venv venv && venv\Scripts\activate

    # for macOS/Linux
    python3 -m venv venv && source venv/bin/activate
    ```

3.  **نصب وابستگی‌ها (در صورت وجود فایل `requirements.txt`):**
    ```bash
    pip install -r requirements.txt
    ```
    *توجه: اگر فایل `requirements.txt` در پروژه وجود ندارد، کتابخانه‌های مورد نیاز را دستی نصب کنید:*
    ```bash
    pip install django beautifulsoup4 requests
    ```

4.  **اجرای مایگریشن‌ها:**
    ```bash
    python manage.py migrate
    ```

5.  **ساخت Superuser (برای دسترسی به پنل ادمین):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **اجرای سرور:**
    ```bash
    python manage.py runserver
    ```

> پروژه شما در آدرس `http://127.0.0.1:8000` در دسترس خواهد بود.

## 🚀 نحوه استفاده

پس از راه‌اندازی پروژه، می‌توانید اسکریپت اصلی جمع‌آوری داده را اجرا کنید. برای این کار، یک **Custom Command** در جنگو ایجاد کرده و آن را به شکل زیر اجرا کنید:

```bash
python manage.py start_scraping
```
*(این یک مثال است و ممکن است نیاز به پیاده‌سازی این دستور در فایل `management/commands` اپلیکیشن `attractions` داشته باشید.)*

## 🤝 مشارکت در پروژه

از مشارکت شما در این پروژه استقبال می‌شود. برای کمک به توسعه، لطفاً یک **Pull Request** ارسال کنید.

1.  پروژه را **Fork** کنید.
2.  یک **Branch** جدید بسازید (`git checkout -b feature/NewFeature`).
3.  تغییرات خود را **Commit** کنید (`git commit -m 'Add a new feature'`).
4.  تغییرات را به **Branch** خود **Push** کنید (`git push origin feature/NewFeature`).
5.  یک **Pull Request** باز کنید.

---

<p align="center">
  ساخته شده با ❤️ توسط <strong>علی شعبانی</strong>
</p>
<p align="center">
  <a href="https://github.com/ALIshabani77">GitHub Profile</a>
</p>
