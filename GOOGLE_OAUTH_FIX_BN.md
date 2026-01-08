# 🔧 Google OAuth "redirect_uri_mismatch" Error Fix করার গাইড

## সমস্যা:
যখন "Sign in with Google" ক্লিক করেন, তখন error দেখায়:
```
Error 400: redirect_uri_mismatch
```

এটি হয় কারণ Google Cloud Console এ যে redirect URIs configure করা আছে, সেগুলো আপনার app এর সাথে match করছে না।

---

## ✅ সমাধান (ধাপে ধাপে):

### ধাপ ১: Google Cloud Console এ যান

1. **Google Cloud Console** খুলুন: https://console.cloud.google.com
2. আপনার project select করুন (যেটি দিয়ে OAuth credentials তৈরি করেছিলেন)

### ধাপ ২: OAuth Credentials খুঁজুন

1. Left sidebar থেকে **"APIs & Services"** → **"Credentials"** এ যান
2. **OAuth 2.0 Client IDs** section এ আপনার Web client ক্লিক করুন

### ধাপ ৩: Authorized Redirect URIs যোগ করুন

**"Authorized redirect URIs"** section এ নিচের URIs গুলো যোগ করুন:

#### Local Development এর জন্য:
```
http://127.0.0.1:8000/accounts/google/login/callback/
http://localhost:8000/accounts/google/login/callback/
```

#### Render.com Production এর জন্য:
```
https://dailydairyshop-3.onrender.com/accounts/google/login/callback/
https://your-app-name.onrender.com/accounts/google/login/callback/
```

**⚠️ গুরুত্বপূর্ণ:**
- শেষে `/` (slash) দিতে ভুলবেন না!
- HTTP vs HTTPS সঠিক হতে হবে
- Production এ নিজের domain দিন

### ধাপ ৪: Save করুন

1. **"Save"** button ক্লিক করুন
2. কিছুক্ষণ অপেক্ষা করুন (2-5 মিনিট)

### ধাপ ৫: Django Admin এ Social App Configure করুন

1. আপনার Django admin panel এ যান:
   - Local: http://127.0.0.1:8000/admin
   - Production: https://dailydairyshop-3.onrender.com/admin

2. **Social applications** (বা "সামাজিক অ্যাপ্লিকেশন") এ যান

3. যদি Google app না থাকে, **"Add Social Application"** ক্লিক করুন:
   - **Provider**: Google
   - **Name**: Google (যেকোনো নাম)
   - **Client ID**: Google Cloud Console থেকে copy করুন
   - **Secret key**: Google Cloud Console থেকে copy করুন
   - **Sites**: আপনার site select করুন (example.com)
   - **Save** করুন

4. যদি ইতিমধ্যে আছে, edit করুন এবং Client ID ও Secret key verify করুন

---

## 📋 Complete Redirect URIs List:

আপনার Google Cloud Console এ এই সব URIs থাকা উচিত:

### Local Development:
```
http://127.0.0.1:8000/accounts/google/login/callback/
http://localhost:8000/accounts/google/login/callback/
```

### Production (Render.com):
```
https://dailydairyshop-3.onrender.com/accounts/google/login/callback/
```

### যদি custom domain থাকে:
```
https://yourdomain.com/accounts/google/login/callback/
```

---

## 🔍 Troubleshooting:

### সমস্যা: এখনও error দেখাচ্ছে

**সমাধান:**
1. Browser cache clear করুন
2. Incognito/Private mode এ try করুন
3. Google Cloud Console এ save করার পর 5 মিনিট অপেক্ষা করুন
4. আবার login try করুন

### সমস্যা: Client ID পাচ্ছি না

**সমাধান:**
1. Google Cloud Console → APIs & Services → Credentials
2. "Create Credentials" → "OAuth client ID"
3. Application type: "Web application"
4. Name দিন
5. Authorized redirect URIs add করুন
6. Create করুন
7. Client ID এবং Client Secret copy করুন

### সমস্যা: Django admin এ Social Applications নেই

**সমাধান:**
```bash
# Migration run করুন
python manage.py migrate

# Superuser তৈরি করুন (যদি না থাকে)
python manage.py createsuperuser
```

---

## 🎯 Step-by-Step Visual Guide:

### Google Cloud Console এ:

1. **Project Select করুন** → Top bar থেকে
2. **Menu** (☰) → APIs & Services → Credentials
3. আপনার **OAuth 2.0 Client ID** ক্লিক করুন
4. **"Authorized redirect URIs"** section খুঁজুন
5. **"+ ADD URI"** button ক্লিক করুন
6. URIs paste করুন (উপরের list থেকে)
7. **"SAVE"** button ক্লিক করুন

### Django Admin এ:

1. Admin panel এ login করুন
2. Left sidebar এ **"Social applications"** খুঁজুন
3. **"Add"** button ক্লিক করুন (বা existing edit করুন)
4. Form fill করুন:
   ```
   Provider: Google
   Name: Google OAuth
   Client id: <your-client-id>
   Secret key: <your-client-secret>
   Sites: example.com (available sites থেকে select)
   ```
5. **"Save"** করুন

---

## ✨ সফল হওয়ার পর:

✅ "Sign in with Google" button কাজ করবে
✅ Google login page খুলবে
✅ Permission দেওয়ার পর আপনার site এ redirect হবে
✅ User automatically login হবে

---

## 📝 Important Notes:

⚠️ **Local এবং Production আলাদা:**
- Development এ: http://127.0.0.1:8000
- Production এ: https://your-app.onrender.com

⚠️ **Protocol মিলাতে হবে:**
- Local: HTTP (http://)
- Production: HTTPS (https://)

⚠️ **Callback URL সবসময়:**
```
/accounts/google/login/callback/
```

---

## 🔗 সাহায্যকারী Links:

- Google Cloud Console: https://console.cloud.google.com
- Django Allauth Docs: https://django-allauth.readthedocs.io
- Google OAuth Setup: https://developers.google.com/identity/protocols/oauth2

---

**এই guide follow করলে Google OAuth সমস্যা solve হবে! 🎉**
