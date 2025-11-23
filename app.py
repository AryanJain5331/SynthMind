import streamlit as st
import google.generativeai as genai
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SynthMind Î©",
    page_icon="ðŸ§ ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM STYLING ---
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #0e1117; border-radius: 4px; color: #fafafa; font-weight: 600; }
    .stTabs [aria-selected="true"] { background-color: #ff4b4b; color: white; }
    h1 { color: #ff4b4b; }
    .role-card { padding: 15px; border-radius: 10px; background-color: #262730; margin-bottom: 10px; border: 1px solid #41444e;}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103832.png", width=50) # Placeholder icon
    st.title("SynthMind Î©")
    st.caption("The Transparent AI Co-Designer")
    st.markdown("---")
    
    api_key = st.text_input("Enter Gemini API Key", type="password", help="Get one from aistudio.google.com")
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
        genai.configure(api_key=api_key)
        st.success("API Key Connected!")
    
    st.markdown("### How it Works")
    st.markdown("1. **Input:** Describe your idea.")
    st.markdown("2. **Designer:** Drafts architecture.")
    st.markdown("3. **Coder:** Writes logic.")
    st.markdown("4. **Critic:** Reviews & Refines.")
    
    st.markdown("---")
    st.caption("Built with Gemini 1.5 Pro & Streamlit")

# --- HELPER FUNCTION ---
def get_gemini_response(prompt, role_name):
    if not api_key:
        return "âš ï¸ Please enter your API Key in the sidebar first."
    
    try:
        model = genai.GenerativeModel('gemini-2.5-pro')
        # System instruction to ensure specific persona behavior
        full_prompt = f"""
        You are SynthMind Omega, specifically acting in the role of the {role_name}.
        
        ROLE DEFINITION:
        {prompt}
        
        Ensure your output is structured, clear, and educational. Explaining your reasoning is mandatory.
        """
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# --- MAIN SESSION STATE ---
if 'design_output' not in st.session_state:
    st.session_state.design_output = ""
if 'code_output' not in st.session_state:
    st.session_state.code_output = ""
if 'critic_output' not in st.session_state:
    st.session_state.critic_output = ""
if 'user_idea' not in st.session_state:
    st.session_state.user_idea = ""

# --- MAIN UI ---
st.title("SynthMind Î©")
st.subheader("Turn ideas into blueprints while watching the AI think.")

# INPUT SECTION
with st.container():
    st.markdown("#### 01. User Input")
    user_input = st.text_area("Describe your goal in plain language:", height=100, placeholder="E.g., I want an app that tracks my water intake and gamifies it with a growing plant.")
    
    if st.button("Initialize Co-Design Process", type="primary"):
        if not user_input:
            st.warning("Please describe your idea first.")
        elif not api_key:
            st.error("Please enter your API key in the sidebar.")
        else:
            st.session_state.user_idea = user_input
            with st.spinner("SynthMind is thinking..."):
                # 1. DESIGNER PHASE
                design_prompt = f"""
                Act as the **DESIGNER**.
                User Goal: "{user_input}"
                Tasks:
                1. Interpret the idea.
                2. Create a high-level system architecture.
                3. Define modules and data flow.
                Output Format: Markdown with clear headers.
                """
                st.session_state.design_output = get_gemini_response(design_prompt, "DESIGNER")
                
                # 2. CODER PHASE
                coder_prompt = f"""
                Act as the **CODER**.
                Based on this design: {st.session_state.design_output}
                Tasks:
                1. Generate minimal pseudocode or skeleton Python code.
                2. Add comments explaining *why* specific logic was chosen.
                """
                st.session_state.code_output = get_gemini_response(coder_prompt, "CODER")
                
                # 3. CRITIC PHASE
                critic_prompt = f"""
                Act as the **CRITIC**.
                Review the Design: {st.session_state.design_output}
                Review the Code: {st.session_state.code_output}
                Tasks:
                1. Identify potential flaws or edge cases.
                2. Suggest improvements for transparency or efficiency.
                3. Give a final "Reasoning Summary".
                """
                st.session_state.critic_output = get_gemini_response(critic_prompt, "CRITIC")
            
            st.success("Synthesis Complete! Explore the tabs below.")

# TABS SECTION
if st.session_state.user_idea:
    st.markdown("---")
    tab1, tab2, tab3 = st.tabs(["ðŸŽ¨ Designer", "ðŸ’» Coder", "ðŸ§ Critic"])

    with tab1:
        st.markdown("<div class='role-card'><b>Role: Designer</b><br>Interprets idea & drafts architecture.</div>", unsafe_allow_html=True)
        st.markdown(st.session_state.design_output)

    with tab2:
        st.markdown("<div class='role-card'><b>Role: Coder</b><br>Generates functional logic skeleton.</div>", unsafe_allow_html=True)
        st.code(st.session_state.code_output, language='python')

    with tab3:
        st.markdown("<div class='role-card'><b>Role: Critic</b><br>Reviews & improves design transparently.</div>", unsafe_allow_html=True)
        st.markdown(st.session_state.critic_output)

