import streamlit as st

# Try importing the AI library with error handling
try:
    import google.generativeai as genai
    AI_AVAILABLE = True
    st.sidebar.success("✅ AI Service Available")
except ImportError as e:
    AI_AVAILABLE = False
    st.sidebar.error("❌ AI Service Unavailable")
    st.sidebar.info("Package installation in progress...")
except Exception as e:
    AI_AVAILABLE = False
    st.sidebar.warning(f"⚠️ AI Service Issue: {str(e)}")

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
    elif not AI_AVAILABLE:
        st.error("❌ AI service is currently unavailable due to package installation issues.")
        st.info("🔧 This is a temporary deployment issue. The app is being updated to resolve this.")
        
        # Show a temporary message with next steps
        st.markdown("---")
        st.markdown("### 🚧 Temporary Service Notice")
        st.markdown("""
        **What's happening?** The AI package is still installing on the server.
        
        **What can you do?**
        - ⏰ Wait 2-3 minutes and refresh the page
        - 🔄 Try clicking the button again
        - 📱 The app interface is working - only AI analysis is temporarily unavailable
        
        **Your profile is ready:**
        - Age: {age}
        - Gender: {gender}  
        - State: {state}
        - Occupation: {occupation}
        - Income: {income}
        - Category: {category}
        - Language: {language}
        """.format(age=age, gender=gender, state=state, occupation=occupation, income=income, category=category, language=language))
        
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            
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
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.success("✅ AI Analysis Complete")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            if "API_KEY" in str(e).upper() or "INVALID" in str(e).upper():
                st.error("🔑 Invalid API Key. Please check your Gemini API key and try again.")
                st.info("Make sure you copied the complete API key from Google AI Studio.")
            else:
                st.error("🔧 Technical issue occurred. Please try again or check your internet connection.")
                st.info("If the problem persists, the AI service may be temporarily unavailable.")

# --- FOOTER ---
st.markdown("---")
st.caption("AI for Bharat | Track 3: Communities & Public Impact")