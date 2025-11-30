"""
Test script to find available Gemini models
Run this to see which models work with your API key
"""

import google.generativeai as genai

 # PASTE YOUR GEMINI API KEY HERE
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual key 

print("🔍 Testing Gemini API and listing available models...\n")

try:
    # Configure API
    genai.configure(api_key=API_KEY)
    
    # List all available models
    print("📋 Available Models:")
    print("-" * 60)
    
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"✅ {model.name}")
            print(f"   Description: {model.description}")
            print(f"   Methods: {model.supported_generation_methods}")
            print()
    
    print("-" * 60)
    print("\n🧪 Testing a simple generation...\n")
    
    # Try different model names
    test_models = [
        'gemini-pro',
        'gemini-1.5-pro',
        'gemini-1.5-flash',
        'models/gemini-pro',
        'models/gemini-1.5-pro',
        'models/gemini-1.5-flash'
    ]
    
    for model_name in test_models:
        try:
            print(f"Testing: {model_name}...", end=" ")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content("Say hello")
            print(f"✅ WORKS! Response: {response.text[:50]}...")
            print(f"\n🎯 USE THIS MODEL: {model_name}\n")
            break
        except Exception as e:
            print(f"❌ Failed: {str(e)[:80]}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n⚠️ Check your API key is correct!")

print("\n" + "=" * 60)
print("Copy the working model name and use it in app.py")
print("=" * 60)