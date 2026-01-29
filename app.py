import streamlit as st

# Try importing the AI library with error handling
try:
    import google.generativeai as genai
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    st.error("⚠️ Google Generative AI library not available. Please check the deployment logs.")
    st.info("This might be a temporary issue with package installation. Try refreshing the page in a few minutes.")

# Demo data for different user profiles
def get_demo_schemes(age, gender, state, occupation, income, category, language):
    """Generate demo scheme recommendations based on user profile"""
    
    schemes = []
    
    # Scheme 1: Based on age and occupation
    if age <= 35 and occupation == "Student":
        schemes.append({
            "name": "PM Scholarship Scheme" if language == "English" else "प्रधानमंत्री छात्रवृत्ति योजना",
            "benefit": "Get ₹2,500 per month for studies" if language == "English" else "अध्ययन के लिए ₹2,500 प्रति माह प्राप्त करें",
            "qualification": f"You qualify because you are {age} years old (under 35), work as a {occupation}, and belong to {category} category. This scheme specifically targets young students from all backgrounds." if language == "English" else f"आप योग्य हैं क्योंकि आप {age} वर्ष के हैं (35 से कम), {occupation} हैं, और {category} श्रेणी से हैं।",
            "documents": ["Aadhaar Card", "Income Certificate", "Educational Documents"] if language == "English" else ["आधार कार्ड", "आय प्रमाण पत्र", "शैक्षणिक दस्तावेज"]
        })
    
    # Scheme 2: Based on income and category
    if income in ["< ₹1 Lakh", "₹1 Lakh - ₹3 Lakhs"] and category in ["SC/ST", "OBC"]:
        schemes.append({
            "name": "Post Matric Scholarship" if language == "English" else "पोस्ट मैट्रिक छात्रवृत्ति",
            "benefit": "Get ₹1,200 per month + fees reimbursement" if language == "English" else "₹1,200 प्रति माह + फीस की प्रतिपूर्ति प्राप्त करें",
            "qualification": f"You qualify because your family income is {income} (below ₹3 lakhs) and you belong to {category} category. This scheme is specifically designed for economically weaker sections." if language == "English" else f"आप योग्य हैं क्योंकि आपकी पारिवारिक आय {income} है और आप {category} श्रेणी से हैं।",
            "documents": ["Caste Certificate", "Income Certificate", "Bank Details"] if language == "English" else ["जाति प्रमाण पत्र", "आय प्रमाण पत्र", "बैंक विवरण"]
        })
    
    # Scheme 3: State-specific scheme
    if state == "Tamil Nadu" and occupation == "Farmer":
        schemes.append({
            "name": "Tamil Nadu Farmer Welfare Scheme" if language == "English" else "तमिलनाडु किसान कल्याण योजना",
            "benefit": "Get ₹6,000 per year + crop insurance" if language == "English" else "₹6,000 प्रति वर्ष + फसल बीमा प्राप्त करें",
            "qualification": f"You qualify because you are a {occupation} residing in {state} state. This scheme targets agricultural workers in Tamil Nadu specifically." if language == "English" else f"आप योग्य हैं क्योंकि आप {state} राज्य में रहने वाले {occupation} हैं।",
            "documents": ["Land Records", "Aadhaar Card", "Bank Passbook"] if language == "English" else ["भूमि रिकॉर्ड", "आधार कार्ड", "बैंक पासबुक"]
        })
    
    # Default schemes if no specific matches
    if len(schemes) < 3:
        default_schemes = [
            {
                "name": "Ayushman Bharat Health Scheme" if language == "English" else "आयुष्मान भारत स्वास्थ्य योजना",
                "benefit": "Get ₹5 lakh health insurance coverage" if language == "English" else "₹5 लाख स्वास्थ्य बीमा कवरेज प्राप्त करें",
                "qualification": f"You qualify because your family income is {income} and you belong to {category} category. This universal health scheme covers most Indian families." if language == "English" else f"आप योग्य हैं क्योंकि आपकी पारिवारिक आय {income} है और आप {category} श्रेणी से हैं।",
                "documents": ["Aadhaar Card", "Ration Card", "Income Certificate"] if language == "English" else ["आधार कार्ड", "राशन कार्ड", "आय प्रमाण पत्र"]
            },
            {
                "name": "PM Kisan Samman Nidhi" if language == "English" else "पीएम किसान सम्मान निधि",
                "benefit": "Get ₹6,000 per year in 3 installments" if language == "English" else "3 किस्तों में ₹6,000 प्रति वर्ष प्राप्त करें",
                "qualification": f"You qualify because you are {age} years old and your occupation is {occupation}. This scheme supports agricultural families across India." if language == "English" else f"आप योग्य हैं क्योंकि आप {age} वर्ष के हैं और आपका व्यवसाय {occupation} है।",
                "documents": ["Land Records", "Aadhaar Card", "Bank Details"] if language == "English" else ["भूमि रिकॉर्ड", "आधार कार्ड", "बैंक विवरण"]
            },
            {
                "name": "Digital India Initiative" if language == "English" else "डिजिटल इंडिया पहल",
                "benefit": "Get free digital literacy training" if language == "English" else "मुफ्त डिजिटल साक्षरता प्रशिक्षण प्राप्त करें",
                "qualification": f"You qualify because you are a {gender} from {state} state. This scheme promotes digital literacy across all demographics." if language == "English" else f"आप योग्य हैं क्योंकि आप {state} राज्य से {gender} हैं।",
                "documents": ["Aadhaar Card", "Mobile Number", "Email ID"] if language == "English" else ["आधार कार्ड", "मोबाइल नंबर", "ईमेल आईडी"]
            }
        ]
        
        # Add default schemes to reach 3 total
        for scheme in default_schemes:
            if len(schemes) < 3:
                schemes.append(scheme)
    
    return schemes[:3]  # Return exactly 3 schemes

# --- PAGE CONFIG ---
st.set_page_config(page_title="SchemeSetu | Government Scheme Finder", page_icon="🇮🇳", layout="wide")

# --- SIDEBAR: CONFIG ---
st.sidebar.header("⚙️ Configuration")
use_demo_mode = st.sidebar.checkbox("🚀 Use Demo Mode (No API Key Required)", value=True)

if not use_demo_mode:
    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
else:
    api_key = None
    st.sidebar.success("✅ Demo Mode Active - Using Sample Data")

st.sidebar.markdown("---")
st.sidebar.info("🇮🇳 **SchemeSetu** bridges the gap between citizens and government benefits.")

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
    if use_demo_mode:
        # Demo mode - use predefined schemes
        with st.spinner(f"Analyzing your profile using demo data in {language}..."):
            import time
            time.sleep(2)  # Simulate processing time
            
            demo_schemes = get_demo_schemes(age, gender, state, occupation, income, category, language)
            
            st.markdown("---")
            st.success("✅ Analysis Complete (Demo Mode)")
            
            # Display schemes
            for i, scheme in enumerate(demo_schemes, 1):
                st.markdown(f"### {i}. {scheme['name']}")
                st.markdown(f"**Benefit:** {scheme['benefit']}")
                st.markdown(f"**WHY YOU QUALIFY:** {scheme['qualification']}")
                st.markdown(f"**Documents Needed:** {', '.join(scheme['documents'])}")
                st.markdown("---")
            
            # Consolidated documents
            all_docs = set()
            for scheme in demo_schemes:
                all_docs.update(scheme['documents'])
            
            st.markdown("### 📋 Consolidated Document List")
            for doc in sorted(all_docs):
                st.markdown(f"• {doc}")
                
            st.info("💡 This is demo mode with sample data. For real-time AI analysis, uncheck 'Demo Mode' and enter your Gemini API key.")
            
    elif not AI_AVAILABLE:
        st.error("❌ AI service is not available. Please try Demo Mode or try again later.")
    elif not api_key:
        st.error("Please enter your Gemini API Key in the sidebar or enable Demo Mode.")
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
            st.error(f"Error: {e}")
            st.info("💡 Try Demo Mode for immediate results without API key requirements.")

# --- FOOTER ---
st.markdown("---")
st.caption("AI for Bharat | Track 3: Communities & Public Impact")