# Render.com এ Django Project Deploy করার সম্পূর্ণ গাইড

## ধাপ ১: GitHub Repository তৈরি করুন

প্রথমে আপনার কোড GitHub এ push করুন:

```bash
git init
git add .
git commit -m "Initial commit for Render deployment"
git branch -M main
git remote add origin https://github.com/your-username/dairy-super-shop.git
git push -u origin main
```

## ধাপ ২: Render.com এ একাউন্ট তৈরি করুন

1. https://render.com এ যান
2. GitHub দিয়ে Sign Up করুন
3. আপনার repository access দিন

## ধাপ ৩: নতুন Web Service তৈরি করুন

1. Dashboard থেকে **"New +"** ক্লিক করুন
2. **"Web Service"** সিলেক্ট করুন
3. আপনার GitHub repository সিলেক্ট করুন

## ধাপ ৪: Service Configuration

নিচের settings দিন:

- **Name**: `dairy-super-shop` (বা যে কোন নাম)
- **Region**: আপনার নিকটস্থ region (যেমন: Singapore)
- **Branch**: `main`
- **Runtime**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn ec.wsgi:application`

## ধাপ ৫: Environment Variables যোগ করুন

**Environment** section এ যান এবং এই variables গুলো যোগ করুন:

```
PYTHON_VERSION=3.12.3
DEBUG=False
SECRET_KEY=your-super-secret-key-here-generate-a-new-one
```

**SECRET_KEY generate করতে Python console এ:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Optional (যদি database ব্যবহার করেন):
```
DATABASE_URL=your-database-url
```

### Cloudinary (ইতিমধ্যে আছে):
```
CLOUDINARY_CLOUD_NAME=dfkzni71h
CLOUDINARY_API_KEY=813172256721514
CLOUDINARY_API_SECRET=bip7IZdpeaHp9w71Up-HncjPoX0
```

### Payment Gateway (যদি লাইভে ব্যবহার করতে চান):
```
BKASH_APP_KEY=your-bkash-key
BKASH_APP_SECRET=your-bkash-secret
BKASH_BASE_URL=https://tokenized.pay.bka.sh

NAGAD_MERCHANT_ID=your-nagad-id
NAGAD_MERCHANT_PASS=your-nagad-pass
NAGAD_BASE_URL=https://api.mynagad.com
```

### Email Settings:
```
EMAIL_HOST_USER=sharatacharjee6@gmail.com
EMAIL_HOST_PASSWORD=iyxrzfhdjoxvguhq
```

## ধাপ ৬: Deploy করুন

1. **"Create Web Service"** button ক্লিক করুন
2. Render আপনার app build এবং deploy করবে (5-10 মিনিট লাগতে পারে)
3. Deploy সম্পূর্ণ হলে, আপনার app URL দেখতে পাবেন

## ধাপ ৭: Custom Domain (Optional)

যদি আপনার নিজের domain যোগ করতে চান:

1. Service Settings এ যান
2. **"Custom Domain"** section এ আপনার domain add করুন
3. আপনার domain provider এ Render এর DNS records add করুন

## গুরুত্বপূর্ণ নোট:

### ⚠️ Security:
- **SECRET_KEY** সবসময় পরিবর্তন করুন (GitHub এ push করার আগে)
- **DEBUG=False** production এ রাখুন
- Sensitive information environment variables এ রাখুন

### 📁 Static Files:
- Render automatically `build.sh` run করবে
- WhiteNoise static files serve করবে

### 🗄️ Database:
- বর্তমানে SQLite ব্যবহার করছেন
- Production এ PostgreSQL ব্যবহার করা better
- Render এ free PostgreSQL পেতে পারেন

### 🔄 Auto Deploy:
- GitHub এ push করলে automatically deploy হবে
- Manual deploy option ও আছে

## Database Migration (SQLite থেকে PostgreSQL এ যেতে চাইলে):

1. Render dashboard এ **"New PostgreSQL"** database তৈরি করুন
2. Database URL copy করুন
3. Environment Variables এ add করুন:
   ```
   DATABASE_URL=postgresql://...
   ```
4. settings.py তে dj-database-url ইতিমধ্যে আছে (automatically configure হবে)

## Troubleshooting:

### যদি deploy fail করে:
1. Render logs দেখুন
2. `build.sh` executable কিনা check করুন: `chmod +x build.sh`
3. requirements.txt এ সব dependencies আছে কিনা check করুন

### Static files load না হলে:
1. `STATIC_ROOT` properly set আছে কিনা check করুন
2. `python manage.py collectstatic` manually run করুন

### Database error হলে:
1. `python manage.py migrate` run করুন
2. PostgreSQL ব্যবহার করলে DATABASE_URL সঠিক আছে কিনা check করুন

## লাইভ URL:

Deploy সম্পূর্ণ হলে আপনার app এই URL এ পাবেন:
```
https://dairy-super-shop.onrender.com
```

বা আপনার দেওয়া custom name অনুযায়ী।

## সাহায্য লিংক:

- Render Documentation: https://render.com/docs
- Django Deployment Guide: https://docs.djangoproject.com/en/5.0/howto/deployment/

---

**সফল deployment এর জন্য শুভকামনা! 🚀**
