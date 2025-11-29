# 📄 Resume Screening Agent

An AI-powered resume screening and ranking system that automates candidate evaluation using GPT-4. Built for the Rooman Technologies AI Agent Development Challenge.

## 🎯 Overview

This agent analyzes resumes against job descriptions and provides:
- **Automated scoring** across multiple dimensions (skills, experience, education)
- **Intelligent ranking** of candidates from best to worst fit
- **Detailed insights** including strengths, gaps, and recommendations
- **Export capabilities** for further analysis

## ✨ Features

### Core Capabilities
- ✅ **Multi-format support**: PDF, DOCX, and TXT resume uploads
- ✅ **Batch processing**: Analyze multiple resumes simultaneously
- ✅ **Comprehensive scoring**: Skills, experience, and education evaluation
- ✅ **Smart recommendations**: Categorizes candidates as Strong/Good/Moderate/Weak fit
- ✅ **Detailed analysis**: Identifies key strengths and potential gaps
- ✅ **Export results**: Download rankings as CSV for reporting

### Scoring Metrics
1. **Overall Score** (0-100): Holistic match assessment
2. **Skills Match** (0-100): Technical and soft skills alignment
3. **Experience Match** (0-100): Years and relevance of experience
4. **Education Match** (0-100): Qualifications and certifications

## 🛠️ Tech Stack

- **Framework**: Streamlit (UI)
- **AI Model**: OpenAI GPT-4o-mini
- **Document Processing**: PyPDF2, python-docx
- **Data Handling**: Pandas
- **Language**: Python 3.8+

## 📋 Prerequisites

1. Python 3.8 or higher
2. OpenAI API key ([Get it here](https://platform.openai.com/api-keys))
3. Git (for cloning the repository)

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd resume-screening-agent
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy and save it securely

## ▶️ Running the Application

### Local Development
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Using the Application

1. **Enter API Key**: Paste your OpenAI API key in the sidebar
2. **Add Job Description**: Paste the complete job posting in the text area
3. **Upload Resumes**: Upload one or more resumes (PDF/DOCX/TXT)
4. **Analyze**: Click "Analyze & Rank Candidates"
5. **Review Results**: View ranked candidates with detailed insights
6. **Export**: Download results as CSV if needed

## 🏗️ Architecture

```
┌─────────────────┐
│   Streamlit UI  │
│  (User Input)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Document Parser │
│  (PyPDF2/docx)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   OpenAI API    │
│   (GPT-4o-mini) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Result Ranking  │
│  & Presentation │
└─────────────────┘
```

### Flow Diagram
1. User uploads job description and resumes
2. System extracts text from each resume
3. AI analyzes resume against job description
4. Scoring algorithm evaluates multiple dimensions
5. Results are ranked and displayed
6. User can export or review detailed analysis

## 📊 Sample Output

```
Rank | Candidate      | Score | Recommendation | Skills | Experience | Education
-----|----------------|-------|----------------|--------|------------|----------
1    | john_doe.pdf   | 92    | Strong Fit     | 95     | 90         | 88
2    | jane_smith.pdf | 85    | Good Fit       | 88     | 82         | 84
3    | bob_jones.pdf  | 68    | Moderate Fit   | 70     | 65         | 70
```

## ⚠️ Limitations

1. **File Size**: Best for resumes under 5MB
2. **Format Quality**: Scanned PDFs may have poor text extraction
3. **API Costs**: Each analysis costs ~$0.01-0.02 (GPT-4o-mini pricing)
4. **Rate Limits**: OpenAI has rate limits (500 requests/min for paid tiers)
5. **Subjective Scoring**: AI evaluation may not match human judgment perfectly
6. **Language**: Currently optimized for English resumes

## 🔮 Potential Improvements

### Short-term
- [ ] Add support for more file formats (LinkedIn PDFs, HTML)
- [ ] Implement local caching to avoid re-analyzing same resumes
- [ ] Add batch job description templates
- [ ] Email notification when analysis is complete

### Medium-term
- [ ] Integration with ATS (Applicant Tracking Systems)
- [ ] Custom scoring weights (prioritize skills vs experience)
- [ ] Multi-language support
- [ ] Interview question generator based on gaps

### Long-term
- [ ] Fine-tuned model for specific industries
- [ ] Video resume analysis
- [ ] Automated interview scheduling for top candidates
- [ ] Integration with LinkedIn for profile verification
- [ ] Bias detection and diversity scoring

## 🐛 Troubleshooting

### Common Issues

**Issue**: "API key invalid"
- **Solution**: Check your OpenAI API key is correct and has credits

**Issue**: "Cannot extract text from PDF"
- **Solution**: PDF may be scanned. Try converting to text-based PDF first

**Issue**: "Rate limit exceeded"
- **Solution**: Wait a few seconds between large batches or upgrade OpenAI plan

**Issue**: "Module not found"
- **Solution**: Run `pip install -r requirements.txt` again

## 📝 Project Structure

```
resume-screening-agent/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── architecture.png      # Architecture diagram
└── sample_resumes/       # Sample test files (optional)
```

## 🔐 Security Notes

- API keys are never stored or logged
- All processing happens in your environment
- No resume data is saved to disk
- OpenAI retains API data per their policy (30 days for abuse monitoring)

## 📄 License

This project is submitted for the Rooman Technologies AI Agent Development Challenge.

## 👤 Author

**Your Name**
- Challenge: 48-Hour AI Agent Development
- Category: People & HR - Resume Screening Agent
- Submission Date: November 29, 2024

## 🙏 Acknowledgments

- Rooman Technologies for organizing the challenge
- OpenAI for providing GPT-4 API
- Streamlit for the amazing framework

## 📞 Contact

For questions or feedback about this project:
- Email: your.email@example.com
- GitHub: @yourusername

---

**Built with ❤️ in 48 hours for Rooman Technologies AI Agent Challenge**