# 🎯 Copy করা Project থেকে নিজের Render Live Link তৈরি করার Checklist

**Important**: অন্য কারো project copy করেছেন, তাই এগুলো সবই change/add করতে হবে।

---

## ✅ **STEP 1: Environment Variables (সবচেয়ে গুরুত্বপূর্ণ)**

### Render Dashboard এ Environment Variables add করুন:

```
# Django Settings
PYTHON_VERSION=3.12.3
DEBUG=False
SECRET_KEY=<generate-new-secret-key>

# Your Own Email
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Your Own Cloudinary Account
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Your Own Payment Gateway (বাধ্যতামূলক নয়)
BKASH_APP_KEY=your-bkash-key
BKASH_APP_SECRET=your-bkash-secret

NAGAD_MERCHANT_ID=your-nagad-id
NAGAD_MERCHANT_PASS=your-nagad-pass
```

**Generate Secret Key:**
```bash
python generate_secret_key.py
```

---

## ✅ **STEP 2: Google OAuth Setup (Render domain এর জন্য)**

### আপনার নতুন Google Cloud Project তৈরি করুন:

1. Google Cloud Console → নতুন Project তৈরি করুন
2. APIs & Services → OAuth 2.0 Consent Screen setup করুন
3. Credentials → OAuth 2.0 Client ID (Web application) তৈরি করুন
4. **Authorized redirect URIs** add করুন:
   ```
   https://your-app-name.onrender.com/accounts/google/login/callback/
   https://127.0.0.1:8000/accounts/google/login/callback/
   ```
5. **Client ID এবং Secret copy করুন**

### Django Admin এ Social App setup করুন:
1. https://your-app-name.onrender.com/admin
2. Social applications → Add
3. Fill করুন:
   ```
   Provider: Google
   Name: Google
   Client id: your-client-id
   Secret key: your-secret-key
   Sites: your-app-name.onrender.com
   ```

---

## ✅ **STEP 3: Cloudinary Account (ছবি upload এর জন্য)**

### Cloudinary এ তিনটি জিনিস পাবেন:
1. Cloud Name
2. API Key
3. API Secret

এগুলো Render এর Environment Variables এ add করুন।

**settings.py তে update করুন:**
```python
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
    secure=True
)
```

---

## ✅ **STEP 4: Email Configuration**

### Gmail থেকে App Password তৈরি করুন:

1. Google Account → Security → 2FA enable করুন
2. App passwords → Gmail select → Device select
3. Password copy করুন
4. Render Environment Variables এ add করুন:
   ```
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ```

**settings.py already configured:**
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'your-email@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = 'Your Shop Name <your-email@gmail.com>'
```

---

## ✅ **STEP 5: Database (Optional - PostgreSQL recommendation)**

### SQLite থেকে PostgreSQL এ switch করুন (Production এর জন্য ভালো):

1. Render Dashboard → New PostgreSQL database তৈরি করুন
2. Internal Database URL copy করুন
3. Render Web Service এর Environment Variables এ add করুন:
   ```
   DATABASE_URL=postgresql://user:password@host/dbname
   ```

**settings.py automatically configure করবে dj-database-url দিয়ে:**
```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
```

---

## ✅ **STEP 6: Admin Panel Access**

### Superuser তৈরি করুন (Render এ):

```bash
python manage.py createsuperuser
```

**বা Render shell এ:**
```bash
# Render Dashboard → Web Service → Shell tab
python manage.py createsuperuser
```

---

## ✅ **STEP 7: Settings.py এ কি কি থাকবে (পুরানো remove করো):**

### Remove করো:
```python
❌ EMAIL_HOST_USER = 'sharatacharjee6@gmail.com'  # Old email
❌ EMAIL_HOST_PASSWORD = 'iyxrzfhdjoxvguhq'      # Old password
❌ ALLOWED_HOSTS = ['dailydairyshop-3.onrender.com']  # Old domain
```

### Add থাকবে:
```python
✅ EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
✅ EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
✅ CLOUDINARY_CONFIG = {
    'cloud_name': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'api_key': os.environ.get('CLOUDINARY_API_KEY'),
    'api_secret': os.environ.get('CLOUDINARY_API_SECRET'),
}
✅ ALLOWED_HOSTS = ['your-app-name.onrender.com', '.onrender.com', 'localhost', '127.0.0.1']
```

---

## ✅ **STEP 8: Media Files (Cloudinary এ থাকবে)**

### পুরানো ছবি delete করতে পারো:
```bash
rm -rf media/product/*  # ছবি folder পরিষ্কার করো
```

নতুন users যে ছবি upload করবে সেগুলো Cloudinary এ save হবে।

---

## ✅ **STEP 9: Database Reset (Important!)**

### Render এ fresh database চান?

```bash
# পুরানো data delete করো
rm db.sqlite3

# নতুন migrations run করো
python manage.py migrate
```

---

## ✅ **STEP 10: Final Checklist**

Deploy করার আগে নিশ্চিত করো:

- [ ] SECRET_KEY পরিবর্তন করেছো
- [ ] DEBUG=False production এ
- [ ] ALLOWED_HOSTS নিজের domain আছে
- [ ] Google OAuth credentials নতুন
- [ ] Email settings নিজের email
- [ ] Cloudinary account নিজের
- [ ] Superuser password নতুন
- [ ] সব Environment Variables add করেছো
- [ ] .env file .gitignore এ আছে
- [ ] Old media files delete করেছো

---

## 🚀 **Complete Deployment Workflow:**

1. **সব sensitive info environment variable এ রাখো**
   ```bash
   git add .
   git commit -m "Update with new credentials for independent deployment"
   git push
   ```

2. **Render Dashboard এ Environment Variables add করো**

3. **Manual Deploy করো বা GitHub থেকে auto deploy

4. **Test করো:**
   - https://your-app-name.onrender.com
   - Admin panel এ login করো
   - Products add করো
   - Google login test করো

---

## 🔐 Security Notes:

⚠️ **কখনও commit করবে না:**
- .env file (already in .gitignore)
- Secret keys
- API credentials
- Email passwords
- Database URLs

✅ **সবসময় Environment Variables ব্যবহার করো:**
```python
os.environ.get('VARIABLE_NAME', 'default_value')
```

---

## 📝 Original vs Your Version:

| Item | Original | Your Version |
|------|----------|--------------|
| Domain | dailydairyshop-3.onrender.com | your-app-name.onrender.com |
| Email | sharatacharjee6@gmail.com | your-email@gmail.com |
| Google OAuth | Original's OAuth | Your Google Cloud Project |
| Cloudinary | Original's account | Your Cloudinary account |
| Database | SQLite (shared) | PostgreSQL (your own) |
| Superuser | Original's user | Your credentials |

---

**এই সব করলে আপনার নিজস্ব independent Render live app থাকবে! 🎉**
