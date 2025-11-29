import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
import docx
import json
import pandas as pd
from typing import List, Dict
import io

# Page configuration
st.set_page_config(
    page_title="Resume Screening Agent",
    page_icon="📄",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e40af;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #64748b;
        margin-bottom: 2rem;
    }
    .score-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
    }
    .candidate-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 2px solid #e2e8f0;
        margin-bottom: 1rem;
        background: white;
    }
    .metric-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background: #f8fafc;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def extract_text_from_pdf(file) -> str:
    """Extract text from PDF file"""
    try:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return ""

def extract_text_from_docx(file) -> str:
    """Extract text from DOCX file"""
    try:
        doc = docx.Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        st.error(f"Error reading DOCX: {str(e)}")
        return ""

def extract_text_from_txt(file) -> str:
    """Extract text from TXT file"""
    try:
        return file.read().decode('utf-8')
    except Exception as e:
        st.error(f"Error reading TXT: {str(e)}")
        return ""

def extract_text(file) -> str:
    """Extract text based on file type"""
    file_type = file.name.split('.')[-1].lower()
    
    if file_type == 'pdf':
        return extract_text_from_pdf(file)
    elif file_type == 'docx':
        return extract_text_from_docx(file)
    elif file_type == 'txt':
        return extract_text_from_txt(file)
    else:
        st.error(f"Unsupported file type: {file_type}")
        return ""

def analyze_resume(resume_text: str, job_description: str, api_key: str, file_name: str) -> Dict:
    """Analyze resume using Google Gemini"""
    
    # Configure Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-2.5-flash')
    
    prompt = f"""Job Description:
{job_description}

Resume:
{resume_text}

Analyze this resume against the job description and provide a JSON response with:
1. overall_score (0-100): Overall match score
2. skills_match (0-100): How well skills match
3. experience_match (0-100): How well experience matches
4. education_match (0-100): How well education matches
5. key_strengths (array): Top 3-5 strengths
6. gaps (array): Top 3-5 gaps or concerns
7. recommendation (string): "Strong Fit", "Good Fit", "Moderate Fit", or "Weak Fit"
8. summary (string): 2-3 sentence summary of the candidate

Respond ONLY with valid JSON, no markdown formatting or extra text."""

    try:
        response = model.generate_content(prompt)
        content = response.text
        
        # Clean up response - remove markdown code blocks if present
        content = content.replace('```json', '').replace('```', '').strip()
        
        # Find JSON in the response
        start_idx = content.find('{')
        end_idx = content.rfind('}') + 1
        
        if start_idx != -1 and end_idx > start_idx:
            json_str = content[start_idx:end_idx]
            analysis = json.loads(json_str)
        else:
            analysis = json.loads(content)
        
        analysis['file_name'] = file_name
        return analysis
    
    except Exception as e:
        st.error(f"Error analyzing resume {file_name}: {str(e)}")
        return None

def get_score_color(score: float) -> str:
    """Get color based on score"""
    if score >= 80:
        return "🟢"
    elif score >= 60:
        return "🔵"
    elif score >= 40:
        return "🟡"
    else:
        return "🔴"

def main():
    # Header
    st.markdown('<div class="main-header">📄 Resume Screening Agent</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">AI-powered resume analysis and candidate ranking system (Powered by Google Gemini)</div>', unsafe_allow_html=True)
    
    # Sidebar - API Key
    with st.sidebar:
        st.header("⚙️ Configuration")
        api_key = st.text_input("Google Gemini API Key", type="password", help="Enter your Google Gemini API key")
        
        st.markdown("---")
        st.markdown("### 📊 About")
        st.info("""
        This agent:
        - Analyzes resumes against job descriptions
        - Provides detailed scoring
        - Ranks candidates automatically
        - Identifies strengths and gaps
        
        **Powered by Google Gemini AI**
        """)
        
        st.markdown("### 🔑 Get Free API Key")
        st.success("Get your FREE Gemini API key at: https://makersuite.google.com/app/apikey")
        
        st.markdown("### 🔒 Privacy")
        st.success("Your API key and data are secure and never stored.")
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📝 Job Description")
        job_description = st.text_area(
            "Paste the complete job description",
            height=300,
            placeholder="Enter the job title, responsibilities, requirements, qualifications..."
        )
    
    with col2:
        st.subheader("📤 Upload Resumes")
        uploaded_files = st.file_uploader(
            "Upload candidate resumes (PDF, DOCX, TXT)",
            accept_multiple_files=True,
            type=['pdf', 'docx', 'txt']
        )
        
        if uploaded_files:
            st.success(f"✅ {len(uploaded_files)} resume(s) uploaded")
            with st.expander("View uploaded files"):
                for file in uploaded_files:
                    st.write(f"📄 {file.name}")
    
    # Analyze button
    st.markdown("---")
    
    if st.button("🚀 Analyze & Rank Candidates", type="primary", use_container_width=True):
        # Validation
        if not api_key:
            st.error("⚠️ Please enter your Google Gemini API key in the sidebar")
            return
        
        if not job_description:
            st.error("⚠️ Please enter a job description")
            return
        
        if not uploaded_files:
            st.error("⚠️ Please upload at least one resume")
            return
        
        # Process resumes
        with st.spinner("🔍 Analyzing resumes... This may take a minute..."):
            results = []
            
            progress_bar = st.progress(0)
            for idx, file in enumerate(uploaded_files):
                # Extract text
                resume_text = extract_text(file)
                
                if resume_text:
                    # Analyze
                    analysis = analyze_resume(resume_text, job_description, api_key, file.name)
                    if analysis:
                        results.append(analysis)
                
                progress_bar.progress((idx + 1) / len(uploaded_files))
            
            progress_bar.empty()
        
        if results:
            # Sort by overall score
            results.sort(key=lambda x: x['overall_score'], reverse=True)
            
            # Display results
            st.success(f"✅ Analysis complete! {len(results)} candidates ranked")
            
            # Summary metrics
            st.markdown("### 📊 Quick Overview")
            cols = st.columns(4)
            
            with cols[0]:
                st.metric("Total Candidates", len(results))
            with cols[1]:
                strong_fits = sum(1 for r in results if r['recommendation'] == 'Strong Fit')
                st.metric("Strong Fits", strong_fits)
            with cols[2]:
                avg_score = sum(r['overall_score'] for r in results) / len(results)
                st.metric("Average Score", f"{avg_score:.1f}")
            with cols[3]:
                top_score = results[0]['overall_score']
                st.metric("Top Score", f"{top_score}")
            
            st.markdown("---")
            st.markdown("### 🏆 Candidate Rankings")
            
            # Display each candidate
            for idx, candidate in enumerate(results):
                with st.container():
                    col1, col2, col3 = st.columns([3, 2, 1])
                    
                    with col1:
                        st.markdown(f"### #{idx+1} - {candidate['file_name']}")
                        
                        # Recommendation badge
                        rec = candidate['recommendation']
                        if rec == 'Strong Fit':
                            st.success(f"✅ {rec}")
                        elif rec == 'Good Fit':
                            st.info(f"👍 {rec}")
                        elif rec == 'Moderate Fit':
                            st.warning(f"⚠️ {rec}")
                        else:
                            st.error(f"❌ {rec}")
                    
                    with col2:
                        st.markdown("#### Score Breakdown")
                        st.write(f"{get_score_color(candidate['skills_match'])} Skills: {candidate['skills_match']}")
                        st.write(f"{get_score_color(candidate['experience_match'])} Experience: {candidate['experience_match']}")
                        st.write(f"{get_score_color(candidate['education_match'])} Education: {candidate['education_match']}")
                    
                    with col3:
                        st.markdown("#### Overall")
                        st.markdown(f"<div class='score-card'><h1>{candidate['overall_score']}</h1></div>", unsafe_allow_html=True)
                    
                    # Summary
                    st.markdown("**Summary:**")
                    st.write(candidate['summary'])
                    
                    # Expandable details
                    with st.expander("📋 View Detailed Analysis"):
                        col_a, col_b = st.columns(2)
                        
                        with col_a:
                            st.markdown("**✅ Key Strengths:**")
                            for strength in candidate.get('key_strengths', []):
                                st.write(f"• {strength}")
                        
                        with col_b:
                            st.markdown("**⚠️ Gaps/Concerns:**")
                            for gap in candidate.get('gaps', []):
                                st.write(f"• {gap}")
                    
                    st.markdown("---")
            
            # Export option
            st.markdown("### 💾 Export Results")
            
            # Create DataFrame for export
            df = pd.DataFrame([
                {
                    'Rank': idx + 1,
                    'File Name': r['file_name'],
                    'Overall Score': r['overall_score'],
                    'Recommendation': r['recommendation'],
                    'Skills Match': r['skills_match'],
                    'Experience Match': r['experience_match'],
                    'Education Match': r['education_match'],
                    'Summary': r['summary']
                }
                for idx, r in enumerate(results)
            ])
            
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name="resume_screening_results.csv",
                mime="text/csv"
            )

if __name__ == "__main__":
    main()