# 🚀 আপনার নিজস্ব Render Live App তৈরি করার দ্রুত গাইড

**Status**: আপনার প্রজেক্ট সম্পূর্ণ ready! সব hardcoded credentials environment variables এ move করা হয়েছে।

---

## ⚡ Quick Setup (৫ মিনিটে Complete):

### 1️⃣ **নিজের Google OAuth Project তৈরি করুন**

- Google Cloud Console → নতুন Project
- OAuth 2.0 Consent Screen configure করুন
- OAuth 2.0 Client ID (Web app) তৈরি করুন
- **Redirect URIs:**
  ```
  https://your-app-name.onrender.com/accounts/google/login/callback/
  ```
- **Client ID এবং Secret copy করুন**

### 2️⃣ **নিজের Cloudinary Account setup করুন**

- Cloudinary.com এ sign up করুন
- Dashboard থেকে copy করুন:
  - Cloud Name
  - API Key
  - API Secret

### 3️⃣ **নিজের Email Setup করুন**

- Gmail Account → Security
- 2-Factor Authentication enable করুন
- App passwords → Create করুন
- App password copy করুন

### 4️⃣ **Render এ Environment Variables যোগ করুন**

Render Dashboard → আপনার Web Service → Environment:

```
# Django
DEBUG=False
SECRET_KEY=<run: python generate_secret_key.py>

# Email (আপনার email)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=Your Shop <your-email@gmail.com>

# Cloudinary (আপনার account)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Google OAuth (আপনার OAuth)
# Note: এটি Django admin থেকে add করবেন
```

### 5️⃣ **Django Admin এ Social App Configure করুন**

Deploy হওয়ার পর:

1. https://your-app-name.onrender.com/admin
2. **Social applications → Add**
3. Fill করুন:
   ```
   Provider: Google
   Name: Google
   Client id: your-client-id
   Secret key: your-secret-key
   Sites: your-app-name.onrender.com
   ```
4. Save করুন

### 6️⃣ **Render Deploy করুন**

GitHub push করলে automatic deploy হয়, বা:

- Render Dashboard → Manual Deploy করুন
- ৫-১০ মিনিট অপেক্ষা করুন
- Live যাবে ✅

---

## ✅ যা করা হয়েছে:

✓ All hardcoded credentials removed
✓ Environment variables configuration ready
✓ Settings.py production-ready
✓ Google OAuth template ready
✓ Email configuration flexible
✓ Cloudinary configuration flexible
✓ Database migration ready
✓ Static files WhiteNoise ready
✓ Security best practices implemented

---

## 🔒 Security Checklist:

- [ ] GitHub এ credentials commit করোনি
- [ ] .env file .gitignore এ আছে
- [ ] Render environment variables set করেছি
- [ ] SECRET_KEY new generate করেছি
- [ ] DEBUG=False production এ
- [ ] নিজের OAuth/Email/Cloudinary account

---

## 📝 সম্পূর্ণ Customization Guide:

বিস্তারিত: দেখুন `SETUP_YOUR_OWN_PROJECT_BN.md`

---

## 🎯 Next Steps:

1. Google OAuth setup করুন
2. Cloudinary account তৈরি করুন
3. Email app password generate করুন
4. Render environment variables update করুন
5. Django admin এ Social App configure করুন
6. Deploy করুন এবং test করুন

---

**আপনার নিজস্ব Render live app ready to launch! 🚀**
