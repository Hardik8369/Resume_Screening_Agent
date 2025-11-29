"""
Test script for Resume Screening Agent
Run this to verify your setup before deployment
"""

import sys
import subprocess

def test_imports():
    """Test if all required packages are installed"""
    print("🔍 Testing imports...")
    
    required_packages = [
        ('streamlit', 'Streamlit'),
        ('openai', 'OpenAI'),
        ('PyPDF2', 'PyPDF2'),
        ('docx', 'python-docx'),
        ('pandas', 'Pandas')
    ]
    
    all_good = True
    for package, name in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {name} installed")
        except ImportError:
            print(f"  ❌ {name} NOT installed")
            all_good = False
    
    return all_good

def test_python_version():
    """Check Python version"""
    print("\n🐍 Checking Python version...")
    version = sys.version_info
    
    if version.major == 3 and version.minor >= 8:
        print(f"  ✅ Python {version.major}.{version.minor}.{version.micro} (Compatible)")
        return True
    else:
        print(f"  ❌ Python {version.major}.{version.minor}.{version.micro} (Need 3.8+)")
        return False

def test_api_key_format():
    """Guide user to test API key"""
    print("\n🔑 API Key Testing:")
    print("  ⚠️  You'll need to test this manually in the app")
    print("  1. Get your OpenAI API key from: https://platform.openai.com/api-keys")
    print("  2. It should start with 'sk-'")
    print("  3. Keep it secure - never commit to Git!")
    return True

def test_file_structure():
    """Check if all required files exist"""
    print("\n📁 Checking file structure...")
    
    import os
    required_files = [
        'app.py',
        'requirements.txt',
        'README.md',
        '.gitignore'
    ]
    
    all_good = True
    for file in required_files:
        if os.path.exists(file):
            print(f"  ✅ {file} found")
        else:
            print(f"  ❌ {file} missing")
            all_good = False
    
    return all_good

def create_sample_job_description():
    """Create a sample job description for testing"""
    return """
Software Engineer - Python & AI
We are looking for a talented Software Engineer with strong Python skills and experience in AI/ML.

Requirements:
- 3+ years of Python development experience
- Experience with machine learning frameworks (TensorFlow, PyTorch)
- Strong understanding of REST APIs
- Bachelor's degree in Computer Science or related field
- Experience with cloud platforms (AWS, Azure, GCP)
- Excellent problem-solving skills

Nice to have:
- Experience with NLP
- Knowledge of Docker and Kubernetes
- Contributions to open-source projects
"""

def main():
    """Run all tests"""
    print("=" * 60)
    print("🧪 RESUME SCREENING AGENT - SETUP TEST")
    print("=" * 60)
    
    tests = [
        ("Python Version", test_python_version),
        ("Package Imports", test_imports),
        ("File Structure", test_file_structure),
        ("API Key Setup", test_api_key_format)
    ]
    
    results = []
    for test_name, test_func in tests:
        result = test_func()
        results.append((test_name, result))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 60)
    
    if all_passed:
        print("✅ ALL TESTS PASSED!")
        print("\n📝 Next Steps:")
        print("1. Get your OpenAI API key")
        print("2. Run: streamlit run app.py")
        print("3. Test the app with sample resumes")
        print("4. Deploy to Streamlit Cloud")
        print("5. Submit before 6 PM!")
    else:
        print("❌ SOME TESTS FAILED!")
        print("\n🔧 Fix the issues above, then run this test again.")
        print("\nQuick fix: pip install -r requirements.txt")
    
    print("\n💡 Sample Job Description for Testing:")
    print("-" * 60)
    print(create_sample_job_description())
    print("-" * 60)
    
    print("\n🚀 Good luck with your submission!")
    print("=" * 60)

if __name__ == "__main__":
    main()