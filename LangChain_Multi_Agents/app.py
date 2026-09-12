import streamlit as st
import time
from datetime import datetime
from pipeline.pipeline import run_research_pipeline

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown("""
<style>
    /* Main container */
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
   header[data-testid="stHeader"] {
    background: transparent !important;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Sidebar toggle arrow visible */
[data-testid="collapsedControl"] {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border-radius: 0 8px 8px 0 !important;
    z-index: 999999 !important;
}
    
    /* Title styling */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    .subtitle {
        text-align: center;
        color: #a0aec0;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Card styling */
    .card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        border-color: rgba(102, 126, 234, 0.5);
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.2);
    }
    
    /* Step badge */
    .step-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        letter-spacing: 0.5px;
    }
    
    /* Result card */
    .result-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-left: 4px solid #667eea;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    /* Metric cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #667eea;
    }
    
    .metric-label {
        font-size: 0.85rem;
        color: #a0aec0;
        margin-top: 0.3rem;
    }
    
    /* Status indicator */
    .status-dot {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin-right: 8px;
        animation: pulse 2s infinite;
    }
    
    .status-active {
        background: #48bb78;
        box-shadow: 0 0 10px #48bb78;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        color: #777777;
        padding: 0.75rem 1rem;
        font-size: 1rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255, 255, 255, 0.03);
        padding: 4px;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 0.5rem 1rem;
        color: #a0aec0;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: rgba(15, 12, 41, 0.95);
    }
    
    /* Divider */
    hr {
        border-color: rgba(255, 255, 255, 0.1);
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================
st.markdown('<h1 class="main-title">🔬 AI Research Agent</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Multi-agent intelligence • Search → Scrape → Write → Critique</p>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("### ⚙️ Pipeline")
    st.markdown("---")
    
    st.markdown("""
    <div class="card">
        <div class="step-badge">STEP 1</div>
        <h4>🔍 Search Agent</h4>
        <p style="color: #a0aec0; font-size: 0.9rem;">Finds recent, reliable information from the web</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="step-badge">STEP 2</div>
        <h4>📄 Reader Agent</h4>
        <p style="color: #a0aec0; font-size: 0.9rem;">Picks best URL and scrapes deeper content</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="step-badge">STEP 3</div>
        <h4>✍️ Writer</h4>
        <p style="color: #a0aec0; font-size: 0.9rem;">Drafts comprehensive research report</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="step-badge">STEP 4</div>
        <h4>🧐 Critic</h4>
        <p style="color: #a0aec0; font-size: 0.9rem;">Reviews and provides feedback</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.markdown("""
    - Use specific topics
    - Wait 30-60 seconds
    - Download the report
    """)


# ============================================================
# INPUT SECTION
# ============================================================
st.markdown("---")

col1, col2 = st.columns([4, 1])

with col1:
    topic = st.text_input(
        "🎯 Research Topic",
        placeholder="e.g., capital of india, quantum computing, climate change",
        label_visibility="collapsed"
    )

with col2:
    run_button = st.button("🚀 Start", type="primary", use_container_width=True)


# ============================================================
# RUN PIPELINE
# ============================================================
if run_button:
    if not topic.strip():
        st.error("⚠️ Please enter a research topic!")
    else:
        st.markdown("---")
        st.markdown(f"### 🔬 Researching: *{topic}*")
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        start_time = time.time()
        
        try:
            # ============================================
            # STEP 1
            # ============================================
            status_text.markdown("""
            <div class="card">
                <span class="status-dot status-active"></span>
                <strong>Step 1:</strong> 🔍 Search agent is working...
            </div>
            """, unsafe_allow_html=True)
            progress_bar.progress(10)
            
            result = run_research_pipeline(topic)
            
            progress_bar.progress(100)
            status_text.markdown("""
            <div class="card">
                <span class="status-dot status-active"></span>
                <strong>✅ Complete!</strong> Research finished.
            </div>
            """, unsafe_allow_html=True)
            
            elapsed = time.time() - start_time
            
            # ============================================
            # METRICS
            # ============================================
            st.markdown("---")
            st.markdown("### 📊 Research Summary")
            
            m1, m2, m3, m4 = st.columns(4)
            
            with m1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">4</div>
                    <div class="metric-label">Agents Used</div>
                </div>
                """, unsafe_allow_html=True)
            
            with m2:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">{elapsed:.1f}s</div>
                    <div class="metric-label">Time Taken</div>
                </div>
                """, unsafe_allow_html=True)
            
            with m3:
                word_count = len(result["report"].split())
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">{word_count}</div>
                    <div class="metric-label">Report Words</div>
                </div>
                """, unsafe_allow_html=True)
            
            with m4:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">✓</div>
                    <div class="metric-label">Status</div>
                </div>
                """, unsafe_allow_html=True)
            
            # ============================================
            # RESULTS TABS
            # ============================================
            st.markdown("---")
            st.markdown("### 📄 Results")
            
            tab1, tab2, tab3, tab4 = st.tabs([
                "📝 Report",
                "🧐 Feedback",
                "🔍 Search",
                "📄 Scraped"
            ])
            
            with tab1:
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.markdown(result["report"])
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.download_button(
                    "📥 Download Report",
                    data=result["report"],
                    file_name=f"report_{topic.replace(' ', '_')[:30]}.md",
                    mime="text/markdown",
                    use_container_width=True
                )
            
            with tab2:
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.markdown(result["feedback"])
                st.markdown('</div>', unsafe_allow_html=True)
            
            with tab3:
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.text(result.get("search_results", "No data"))
                st.markdown('</div>', unsafe_allow_html=True)
            
            with tab4:
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.text(result.get("scraped_content", "No data"))
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.success(f"✅ Research completed in {elapsed:.1f} seconds!")
            
        except Exception as e:
            progress_bar.progress(100)
            st.error(f"❌ Error: {str(e)}")
            with st.expander("🔍 Error Details"):
                st.exception(e)


# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #718096; font-size: 0.85rem;">'
    'Made with ❤️ using LangChain • Groq • Streamlit'
    '</p>',
    unsafe_allow_html=True
)