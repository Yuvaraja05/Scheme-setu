import streamlit as st
import requests
import json

# Direct API approach - no problematic packages needed
AI_AVAILABLE = True
st.sidebar.success("✅ AI Service Available")

def call_gemini_api(api_key, prompt):
    """Call Gemini API directly using REST"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        if 'candidates' in result and len(result['candidates']) > 0:
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            return "Error: No response generated"
            
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")
    except KeyError as e:
        raise Exception(f"Unexpected API response format: {str(e)}")
    except Exception as e:
        raise Exception(f"API call error: {str(e)}")

# --- PAGE CONFIG ---
st.set_page_config(page_title="SchemeSetu | Government Scheme Finder", page_icon="🇮🇳", layout="wide")

# --- SIDEBAR: CONFIG ---
st.sidebar.header("⚙️ Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

st.sidebar.markdown("---")
st.sidebar.info("🇮🇳 **SchemeSetu** bridges the gap between citizens and government benefits.")
st.sidebar.markdown("### 🔑 How to get API Key:")
st.sidebar.markdown("1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)")
st.sidebar.markdown("2. Sign in with Google account")
st.sidebar.markdown("3. Click 'Create API Key'")
st.sidebar.markdown("4. Copy and paste here")

# --- MAIN UI ---
st.title("🇮🇳 SchemeSetu (स्कीम सेतु)")
st.subheader("Find Government Schemes You Are Eligible For")
st.markdown("Fill in your details to discover scholarships, subsidies, and welfare schemes tailor-made for you.")

# --- INPUT SECTION ---
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0, max_value=100, value=25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    state = st.selectbox("State/Territory", ["Tamil Nadu", "Karnataka", "Maharashtra", "Delhi", "Uttar Pradesh", "Other"])

with col2:
    occupation = st.selectbox("Occupation", ["Student", "Farmer", "Small Business Owner", "Unemployed", "Salaried Employee"])
    income = st.selectbox("Annual Family Income", ["< ₹1 Lakh", "₹1 Lakh - ₹3 Lakhs", "₹3 Lakhs - ₹8 Lakhs", "> ₹8 Lakhs"])
    category = st.selectbox("Category", ["General", "OBC", "SC/ST", "Minority"])

# --- LANGUAGE SELECTION ---
language = st.selectbox("Select Output Language / भाषा चुनें", ["English", "Hindi (हिंदी)", "Tamil (தமிழ்)", "Telugu (తెలుగు)", "Kannada (ಕನ್ನಡ)"])

# --- AI LOGIC ---
if st.button("🔍 Find My Schemes", type="primary"):
    if not api_key:
        st.error("🔑 Please enter your Gemini API Key in the sidebar to continue.")
        st.info("💡 Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)")
    else:
        try:
            # The Prompt that acts as a Government Expert
            prompt = f"""
            Act as an expert Government Policy Consultant for India.
            
            **User Profile:**
            - Age: {age}
            - Gender: {gender}
            - State: {state}
            - Occupation: {occupation}
            - Income Group: {income}
            - Category: {category}
            
            **Task:**
            1. Identify 3 major Government of India (Central or State specific to {state}) schemes this person is HIGHLY likely to be eligible for.
            2. **THE AI REASONING:** For each scheme, strictly explain *WHY* this specific user qualifies. Use this format:
               - **Scheme Name**
               - **One-line Benefit** (e.g., "Get ₹5,000 per month")
               - **WHY YOU QUALIFY:** "You qualify because you are [specific age/gender/occupation/income/category criteria that matches]. For example: 'You qualify because you are under 25, belong to {category} category, and your family income is {income} which falls within the scheme's income limits.'"
               - **Key Documents Needed**
            3. **Required Documents:** A consolidated list of all documents they will likely need across all schemes.
            
            **CRITICAL REQUIREMENTS:**
            - For each scheme, provide SPECIFIC reasoning based on the user's exact profile
            - Mention the EXACT criteria from their profile that makes them eligible
            - Be precise about age ranges, income limits, category requirements, etc.
            - Output EVERYTHING in this language: **{language}**.
            - Use clear, simple language suitable for a common citizen.
            - Format with clear headings and bullet points.
            """
            
            with st.spinner(f"Searching government database using AI in {language}..."):
                response_text = call_gemini_api(api_key, prompt)
                
                st.markdown("---")
                st.success("✅ AI Analysis Complete")
                st.markdown(response_text)
                
        except Exception as e:
            error_msg = str(e)
            st.error(f"❌ Error: {error_msg}")
            
            if "API_KEY" in error_msg.upper() or "INVALID" in error_msg.upper() or "403" in error_msg:
                st.error("🔑 Invalid API Key. Please check your Gemini API key and try again.")
                st.info("Make sure you copied the complete API key from Google AI Studio.")
            elif "quota" in error_msg.lower() or "429" in error_msg:
                st.error("📊 API quota exceeded. Please try again later or check your API limits.")
            elif "network" in error_msg.lower() or "timeout" in error_msg.lower():
                st.error("🌐 Network issue. Please check your internet connection and try again.")
            else:
                st.error("🔧 Technical issue occurred. Please try again in a moment.")
                with st.expander("🔍 Technical Details"):
                    st.code(error_msg)

# --- FOOTER ---
st.markdown("---")
st.caption("AI for Bharat | Track 3: Communities & Public Impact")