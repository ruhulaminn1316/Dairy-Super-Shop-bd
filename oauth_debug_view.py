"""
Debug helper - Google OAuth configuration checker
Add this to your urls.py temporarily to debug OAuth issues
"""

# Add this view to check what's happening with OAuth
from django.http import JsonResponse
from django.conf import settings
from django.contrib.sites.models import Site

def oauth_debug(request):
    """Debug view to check OAuth configuration"""
    try:
        from allauth.socialaccount.models import SocialApp
        
        google_app = SocialApp.objects.filter(provider='google').first()
        current_site = Site.objects.get_current()
        
        debug_info = {
            "status": "success",
            "current_domain": current_site.domain,
            "allowed_hosts": settings.ALLOWED_HOSTS,
            "debug_mode": settings.DEBUG,
            "google_oauth_configured": bool(google_app),
        }
        
        if google_app:
            debug_info["google_app"] = {
                "name": google_app.name,
                "client_id": google_app.client_id[:10] + "..." if google_app.client_id else None,
                "has_secret": bool(google_app.secret),
                "sites": list(google_app.sites.values_list('domain', flat=True)),
            }
        
        # Expected redirect URI
        debug_info["expected_redirect_uri"] = f"https://{current_site.domain}/accounts/google/login/callback/"
        
        return JsonResponse(debug_info, indent=2)
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# Add this to ec/urls.py:
# path('debug/oauth/', oauth_debug, name='oauth_debug'),
# Then visit: https://dairy-shop-bd.onrender.com/debug/oauth/
