# 🔴 Google OAuth redirect_uri_mismatch - Production Render Debug

## সমস্যা এখনও হচ্ছে?

এই চেকলিস্ট follow করুন:

---

## ✅ Step 1: Google Cloud Console Verify

Google OAuth redirect URIs **exactly** থাকা উচিত:

```
https://dairy-shop-bd.onrender.com/accounts/google/login/callback/
```

**শেষে `/` (slash) আছে কি না নিশ্চিত করুন!**

### Check করুন:
1. Google Cloud Console → APIs & Services → Credentials
2. আপনার OAuth 2.0 Client ID খুলুন
3. **"Authorized redirect URIs"** section দেখুন
4. Exact copy করুন এবং তালিকায় আছে কি না দেখুন

---

## ✅ Step 2: Django Admin Social Application

এটি অত্যন্ত গুরুত্বপূর্ণ!

### Render production এ যান:
1. https://dairy-shop-bd.onrender.com/admin
2. Login করুন (superuser credentials)
3. **"Social applications"** খুঁজুন
4. **"Google"** app এ ক্লিক করুন

### এটি verify করুন:
```
Provider: Google ✓
Name: Google (বা যেকোনো নাম) ✓
Client id: <EXACT Google Client ID> ✓
Secret key: <EXACT Google Client Secret> ✓
Sites: অবশ্যই dairy-shop-bd.onrender.com থাকতে হবে ✓
```

**যদি কিছু মিসম্যাচ থাকে, ঠিক করুন এবং Save করুন।**

---

## ✅ Step 3: Sites Framework Check

django.contrib.sites এ সাইট config আছে কি না:

1. Admin → **"Sites"** → খুঁজুন `dairy-shop-bd.onrender.com`
2. না থাকলে add করুন:
   - **Domain name**: `dairy-shop-bd.onrender.com`
   - **Display name**: `Daily Dairy Shop`
3. এটি **default site** করুন (কোনো site এ তারকা চিহ্ন থাকা উচিত)

---

## ✅ Step 4: Check Frontend Redirect

আপনার login button যে URL এ যাচ্ছে তা চেক করুন:

Template এ খুঁজুন:
```html
<a href="/accounts/google/login/">Sign in with Google</a>
<!-- OR -->
<a href="{% provider_login_url 'google' %}">Sign in with Google</a>
```

এটি সঠিক?

---

## ✅ Step 5: Clear Browser Cache

Google এর কাছে কিছু cache থাকতে পারে:

1. **Incognito/Private ব্রাউজার** খুলুন
2. https://dairy-shop-bd.onrender.com এ যান
3. Google login try করুন

---

## 🔧 Advanced Debug

### URL এ কি পাঠানো হচ্ছে দেখুন:

1. Developer Console খুলুন (F12)
2. **Network** tab ক্লিক করুন
3. Google login বাটন ক্লিক করুন
4. Request URL দেখুন (redirect_uri parameter দেখুন)

সেটি match করছে কি Google Console এর সাথে?

---

## 🆘 সবচেয়ে Common ভুলগুলো:

❌ **ভুল**: `https://dairy-shop-bd.onrender.com/accounts/google/login/callback` (শেষে `/` নেই)
✅ **সঠিক**: `https://dairy-shop-bd.onrender.com/accounts/google/login/callback/` (শেষে `/` আছে)

❌ **ভুল**: Google Console এ নেই কিন্তু Django admin এ আছে
✅ **সঠিক**: Google Console এ আছে এবং Django admin এও আছে

❌ **ভুল**: Django admin Social Application এ wrong Client ID
✅ **সঠিক**: Google Console থেকে copy করা exact same Client ID

---

## 📝 Complete Checklist (Production):

- [ ] Google Cloud Console এ redirect URI আছে (`/callback/` এ শেষ হয়)
- [ ] Django admin Social Application আছে
- [ ] Social App এ correct Client ID/Secret
- [ ] Social App এ correct Site selected
- [ ] Sites framework এ dairy-shop-bd.onrender.com আছে
- [ ] Frontend এ login button সঠিক URL এ পয়েন্ট করছে
- [ ] Incognito mode এ test করেছি

---

## 🎯 Quick Fix (যদি এখনও fail হয়):

1. Google Console এ new OAuth Client তৈরি করুন
2. New Client ID/Secret copy করুন
3. Django admin এ update করুন
4. Save করুন
5. 2 মিনিট অপেক্ষা করুন
6. আবার try করুন

---

## 🔗 সাহায্য লিংক:

- Django Allauth Social: https://django-allauth.readthedocs.io/en/latest/installation.html
- Google OAuth: https://developers.google.com/identity/protocols/oauth2
- Troubleshooting: https://django-allauth.readthedocs.io/en/latest/faq.html

---

**আমাকে জানান কোন step এ stuck আছেন!**
