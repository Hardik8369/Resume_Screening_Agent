# 🚀 Deployment Guide - Resume Screening Agent

## Quick Deploy to Streamlit Cloud (RECOMMENDED - FREE)

### Step 1: Prepare Your Repository

1. **Create a GitHub repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Resume Screening Agent"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/resume-screening-agent.git
   git push -u origin main
   ```

### Step 2: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `YOUR_USERNAME/resume-screening-agent`
5. Set:
   - **Main file path**: `app.py`
   - **Python version**: 3.9
6. Click "Deploy"
7. Wait 2-3 minutes for deployment

### Step 3: Get Your Live Demo Link

Once deployed, you'll get a URL like:
```
https://YOUR_USERNAME-resume-screening-agent-app-xxxxx.streamlit.app
```

**This is your Working Demo Link for submission!**

---

## Alternative: Deploy to Hugging Face Spaces (FREE)

### Setup
1. Create account at https://huggingface.co/
2. Go to https://huggingface.co/spaces
3. Click "Create new Space"
4. Choose:
   - **Name**: resume-screening-agent
   - **SDK**: Streamlit
   - **Visibility**: Public

### Upload Files
1. Upload all project files
2. Hugging Face will auto-deploy
3. Get your URL: `https://huggingface.co/spaces/YOUR_USERNAME/resume-screening-agent`

---

## Local Testing (Before Deployment)

### Test Locally First
```bash
# 1. Activate virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 2. Run the app
streamlit run app.py

# 3. Open browser at http://localhost:8501
```

### Test Checklist
- [ ] App loads without errors
- [ ] Can upload PDF/DOCX/TXT files
- [ ] API key input works
- [ ] Analysis completes successfully
- [ ] Results display correctly
- [ ] CSV export works

---

## Submission Checklist

Before submitting at 6 PM, ensure you have:

### 1. ✅ Working Demo Link
- [ ] App is deployed and accessible
- [ ] URL is tested and working
- [ ] No errors on load

### 2. ✅ Git Repository (Public)
- [ ] All code committed
- [ ] README.md is complete
- [ ] Architecture diagram included
- [ ] .gitignore prevents sensitive data

### 3. ✅ Architecture Diagram
- [ ] Clear visual representation
- [ ] Shows all components
- [ ] Data flow is visible

### 4. ✅ README Document
- [ ] Overview section
- [ ] Features list
- [ ] Tech stack
- [ ] Setup instructions
- [ ] Limitations
- [ ] Potential improvements

### 5. ✅ Optional: Video Demo
- [ ] 2-3 minute walkthrough
- [ ] Shows key features
- [ ] Explains workflow

---

## Submission Form

Submit here: https://forms.office.com/r/GQmPNZ6PgG

Fill in:
- **Working Demo Link**: Your Streamlit Cloud URL
- **GitHub Repository**: Your repo URL
- **Architecture**: Link to diagram or upload
- **Video** (optional): YouTube/Drive link

---

## Troubleshooting Deployment

### Issue: "Requirements installation failed"
**Solution**: Check requirements.txt has correct versions

### Issue: "App crashes on startup"
**Solution**: Check imports, ensure all dependencies listed

### Issue: "File upload not working"
**Solution**: Check file size limits, ensure proper file handling

### Issue: "API calls failing"
**Solution**: Users need to provide their own API key (don't hardcode!)

---

## Performance Tips

1. **Use GPT-4o-mini** instead of GPT-4 (faster, cheaper)
2. **Add progress bars** for better UX
3. **Cache results** to avoid re-processing
4. **Limit file sizes** to under 5MB

---

## Security Checklist

- [ ] Never commit API keys
- [ ] Use .gitignore properly
- [ ] API keys input by user only
- [ ] No sensitive data in repo
- [ ] Validate file uploads

---

## Timeline for Submission (Next 5 Hours)

**12:00 PM - 1:00 PM**: Test locally, fix bugs
**1:00 PM - 2:00 PM**: Deploy to Streamlit Cloud
**2:00 PM - 3:00 PM**: Test live deployment thoroughly
**3:00 PM - 4:00 PM**: Create video demo (optional)
**4:00 PM - 5:30 PM**: Finalize documentation
**5:30 PM - 6:00 PM**: Submit form with all links

---

## Emergency Support

If deployment fails close to deadline:
1. Use **Streamlit Cloud** (fastest)
2. Record local demo video as backup
3. Push all code to GitHub
4. Submit with video + GitHub link
5. Explain deployment attempt in form

---

## After Submission

You'll be contacted for:
- Live presentation to jury
- Architecture explanation
- Q&A session
- Demo walkthrough

**Good luck! 🚀**