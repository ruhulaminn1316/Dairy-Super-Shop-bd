#!/usr/bin/env python
"""
Generate a new Django SECRET_KEY for production use.
Run this script to get a new secret key for Render deployment.
"""

from django.core.management.utils import get_random_secret_key

if __name__ == "__main__":
    secret_key = get_random_secret_key()
    print("\n" + "="*60)
    print("🔐 Your New Django SECRET_KEY:")
    print("="*60)
    print(f"\n{secret_key}\n")
    print("="*60)
    print("\n📋 Copy this key and add it to Render Environment Variables:")
    print("   Variable Name: SECRET_KEY")
    print(f"   Value: {secret_key}")
    print("\n⚠️  Keep this key SECRET! Never commit it to Git!")
    print("="*60 + "\n")
