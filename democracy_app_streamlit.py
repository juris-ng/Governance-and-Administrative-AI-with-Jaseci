# MAU2 Democracy Platform - No External Dependencies Version
# Fixed for Streamlit Cloud Deployment
# Live at: https://mauvoice.streamlit.app/

import streamlit as st
import datetime
import pandas as pd
import time

# === PAGE CONFIGURATION ===
st.set_page_config(
    page_title="MAU2 - Civic Engagement Platform", 
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === SESSION STATE INITIALIZATION ===
def initialize_platform():
    if 'user_authenticated' not in st.session_state:
        st.session_state.user_authenticated = False
    if 'user_role' not in st.session_state:
        st.session_state.user_role = 'citizen'
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'landing'
    if 'petitions' not in st.session_state:
        st.session_state.petitions = []
    if 'reports' not in st.session_state:
        st.session_state.reports = []
    if 'notifications' not in st.session_state:
        st.session_state.notifications = []

initialize_platform()

# === MODERN CSS STYLING (MAU2-INSPIRED) ===
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        font-family: 'Inter', sans-serif;
    }
    
    /* MAU2 Header Styling */
    .mau2-header {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        padding: 1rem 2rem;
        margin: -1rem -1rem 2rem -1rem;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .mau2-logo {
        font-size: 1.8rem;
        font-weight: 700;
        color: white;
        text-decoration: none;
    }
    
    .mau2-nav {
        display: flex;
        gap: 2rem;
        align-items: center;
    }
    
    .mau2-nav-item {
        color: white;
        text-decoration: none;
        font-weight: 500;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        transition: background 0.3s;
        cursor: pointer;
    }
    
    .mau2-nav-item:hover {
        background: rgba(255,255,255,0.2);
    }
    
    /* Landing Page Styling */
    .mau2-hero {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border-radius: 16px;
        margin: 2rem 0;
    }
    
    .mau2-hero h1 {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #1e40af, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .mau2-hero p {
        font-size: 1.25rem;
        color: #64748b;
        margin-bottom: 2rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Card Styling */
    .mau2-card {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
        margin: 1rem 0;
    }
    
    .mau2-card h3 {
        color: #1e293b;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    /* Button Styling */
    .mau2-btn-primary {
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
        color: white;
        padding: 0.75rem 2rem;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        transition: transform 0.2s;
    }
    
    .mau2-btn-primary:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59,130,246,0.4);
    }
    
    /* Form Styling */
    .mau2-form-container {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        max-width: 800px;
        margin: 2rem auto;
    }
    
    .mau2-form-header {
        text-align: center;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #e2e8f0;
    }
    
    .mau2-form-header h2 {
        color: #1e293b;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .mau2-form-header p {
        color: #64748b;
        font-size: 0.9rem;
    }
    
    /* Progress Indicator */
    .mau2-progress {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 2rem 0;
    }
    
    .mau2-progress-step {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: #e2e8f0;
        color: #64748b;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        margin: 0 1rem;
        position: relative;
    }
    
    .mau2-progress-step.active {
        background: #3b82f6;
        color: white;
    }
    
    .mau2-progress-step.completed {
        background: #10b981;
        color: white;
    }
    
    /* Analytics Cards */
    .mau2-metric-card {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
        margin: 1rem 0;
    }
    
    .mau2-metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .mau2-metric-label {
        color: #64748b;
        font-weight: 500;
    }
    
    /* Hide Streamlit branding */
    #MainMenu, .stDeployButton, footer, header {
        visibility: hidden !important;
    }
    
    .stApp > div:first-child {
        padding-top: 0;
    }
    
    /* Navigation styling */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 2rem 0;
        flex-wrap: wrap;
    }
    
    .nav-button {
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        border: none;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .nav-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(59,130,246,0.4);
    }
    
    /* Map placeholder */
    .map-placeholder {
        height: 300px;
        background: linear-gradient(135deg, #93c5fd, #60a5fa);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# === NAVIGATION COMPONENT ===
def render_navigation():
    st.markdown("""
    <div class="nav-container">
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        if st.button("🏠 Home", key="nav_home", use_container_width=True):
            st.session_state.current_page = 'landing'
            st.rerun()
    
    with col2:
        if st.button("📋 Petitions", key="nav_petitions", use_container_width=True):
            st.session_state.current_page = 'petitions'
            st.rerun()
    
    with col3:
        if st.button("📝 Reports", key="nav_reports", use_container_width=True):
            st.session_state.current_page = 'reports'
            st.rerun()
    
    with col4:
        if st.button("🏛️ Dashboard", key="nav_dashboard", use_container_width=True):
            st.session_state.current_page = 'dashboard'
            st.rerun()
    
    with col5:
        if st.button("📊 Analytics", key="nav_analytics", use_container_width=True):
            st.session_state.current_page = 'analytics'
            st.rerun()
    
    with col6:
        if st.button("⚙️ Settings", key="nav_settings", use_container_width=True):
            st.session_state.current_page = 'settings'
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

# === HEADER COMPONENT ===
def render_mau2_header():
    st.markdown(f"""
    <div class="mau2-header">
        <div class="mau2-logo">
            <span style="background: linear-gradient(45deg, #ffffff, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800;">MAU2</span>
        </div>
        <div class="mau2-nav">
            <span class="mau2-nav-item" onclick="window.location.reload()">Home</span>
            <span class="mau2-nav-item">Petitions</span>
            <span class="mau2-nav-item">Reports</span>
            <span class="mau2-nav-item">Community</span>
            <span class="mau2-nav-item">About</span>
            <div style="margin-left: 1rem;">
                <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem;">
                    👤 {st.session_state.get('user_name', 'Sophia Carter')}
                </span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# === LANDING PAGE ===
def render_landing_page():
    render_mau2_header()
    
    st.markdown("""
    <div class="mau2-hero">
        <h1>Welcome to<br><span style="color: #3b82f6;">MAU2</span></h1>
        <p>Your platform for civic engagement. Create, track, and resolve community issues with transparency and collaboration.</p>
        <br>
        <p style="font-size: 0.9rem; margin-top: 2rem;">
            By continuing, you agree to our <a href="#" style="color: #3b82f6;">Terms of Service</a> and <a href="#" style="color: #3b82f6;">Privacy Policy</a>.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature showcase
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="mau2-card">
            <div style="text-align: center; margin-bottom: 1rem;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #3b82f6, #1d4ed8); border-radius: 50%; margin: 0 auto 1rem; display: flex; align-items: center; justify-content: center;">
                    <span style="color: white; font-size: 1.5rem;">📋</span>
                </div>
                <h3>Create Petitions</h3>
                <p style="color: #64748b; font-size: 0.9rem;">Start petitions for community issues and gather support from fellow citizens.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="mau2-card">
            <div style="text-align: center; margin-bottom: 1rem;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #10b981, #059669); border-radius: 50%; margin: 0 auto 1rem; display: flex; align-items: center; justify-content: center;">
                    <span style="color: white; font-size: 1.5rem;">📍</span>
                </div>
                <h3>Report Issues</h3>
                <p style="color: #64748b; font-size: 0.9rem;">Report incidents and issues in your community with location-based mapping.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="mau2-card">
            <div style="text-align: center; margin-bottom: 1rem;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #f59e0b, #d97706); border-radius: 50%; margin: 0 auto 1rem; display: flex; align-items: center; justify-content: center;">
                    <span style="color: white; font-size: 1.5rem;">📊</span>
                </div>
                <h3>Track Progress</h3>
                <p style="color: #64748b; font-size: 0.9rem;">Monitor the status and progress of your petitions and community issues.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Call to action
    if st.button("🚀 Get Started", key="cta_button", use_container_width=True):
        st.session_state.current_page = 'onboarding'
        st.rerun()
    
    render_navigation()

# === ONBOARDING/RIGHTS PAGE ===
def render_onboarding_page():
    render_mau2_header()
    
    st.markdown("""
    <div style="max-width: 600px; margin: 4rem auto; text-align: center;">
        <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #3b82f6, #1d4ed8); border-radius: 50%; margin: 0 auto 2rem; display: flex; align-items: center; justify-content: center;">
            <span style="color: white; font-size: 2rem;">🛡️</span>
        </div>
        <h1 style="color: #1e293b; margin-bottom: 2rem;">Know Your Rights</h1>
        <p style="color: #64748b; font-size: 1.1rem; line-height: 1.6; margin-bottom: 3rem;">
            As a citizen, you have the right to petition your government and escalate issues through proper channels. MAU2 helps you navigate this process effectively.
        </p>
        <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 3rem;">
            <div style="width: 8px; height: 8px; border-radius: 50%; background: #e2e8f0;"></div>
            <div style="width: 8px; height: 8px; border-radius: 50%; background: #3b82f6;"></div>
            <div style="width: 8px; height: 8px; border-radius: 50%; background: #e2e8f0;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Next", key="next_onboarding", use_container_width=True):
        st.session_state.current_page = 'dashboard'
        st.rerun()

# === DASHBOARD ===
def render_dashboard():
    render_mau2_header()
    
    # User profile section
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("""
        <div class="mau2-card">
            <div style="text-align: center;">
                <div style="width: 80px; height: 80px; border-radius: 50%; background: linear-gradient(135deg, #3b82f6, #1d4ed8); margin: 0 auto 1rem; display: flex; align-items: center; justify-content: center;">
                    <span style="color: white; font-size: 2rem;">👤</span>
                </div>
                <h3 style="margin-bottom: 0.5rem;">Sophia Carter</h3>
                <p style="color: #64748b; font-size: 0.9rem; margin-bottom: 1rem;">Citizen<br>Joined 2021</p>
                <div style="display: flex; justify-content: space-around; margin: 2rem 0;">
                    <div style="text-align: center;">
                        <div style="font-size: 1.5rem; font-weight: 700; color: #1e293b;">12</div>
                        <div style="font-size: 0.8rem; color: #64748b;">Petitions</div>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 1.5rem; font-weight: 700; color: #1e293b;">5</div>
                        <div style="font-size: 0.8rem; color: #64748b;">Reports</div>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 1.5rem; font-weight: 700; color: #1e293b;">2</div>
                        <div style="font-size: 0.8rem; color: #64748b;">Resolved</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick actions
        st.markdown("### Quick Actions")
        if st.button("📋 Create Petition", use_container_width=True):
            st.session_state.current_page = 'create_petition'
            st.rerun()
        if st.button("📝 Report an Issue", use_container_width=True):
            st.session_state.current_page = 'report_incident'
            st.rerun()
        if st.button("👀 View My Activity", use_container_width=True):
            st.session_state.current_page = 'my_activity'
            st.rerun()
    
    with col2:
        st.markdown("## Your Civic Feed")
        st.markdown("*Stay informed and engaged with your community.*")
        
        # Petitions section
        st.markdown("### Petitions")
        
        col_pet1, col_pet2 = st.columns(2)
        
        with col_pet1:
            st.markdown("""
            <div class="mau2-card">
                <div style="height: 120px; background: linear-gradient(135deg, #10b981, #059669); border-radius: 8px; margin-bottom: 1rem; display: flex; align-items: center; justify-content: center;">
                    <span style="color: white; font-size: 2rem;">🏞️</span>
                </div>
                <h4>Improve Local Park Facilities</h4>
                <p style="font-size: 0.9rem; color: #64748b; margin: 0.5rem 0;">A petition to upgrade the playground equipment and add more seating in Central Park.</p>
                <button style="background: none; border: none; color: #3b82f6; font-weight: 500; cursor: pointer;">View Petition</button>
            </div>
            """, unsafe_allow_html=True)
        
        with col_pet2:
            st.markdown("""
            <div class="mau2-card">
                <div style="height: 120px; background: linear-gradient(135deg, #3b82f6, #1d4ed8); border-radius: 8px; margin-bottom: 1rem; display: flex; align-items: center; justify-content: center;">
                    <span style="color: white; font-size: 2rem;">🚦</span>
                </div>
                <h4>Traffic Calming Measures on Elm Street</h4>
                <p style="font-size: 0.9rem; color: #64748b; margin: 0.5rem 0;">Request for speed bumps and pedestrian crossings to improve safety on Elm Street.</p>
                <button style="background: none; border: none; color: #3b82f6; font-weight: 500; cursor: pointer;">View Petition</button>
            </div>
            """, unsafe_allow_html=True)
        
        # Reports section
        st.markdown("### Reports")
        
        col_rep1, col_rep2 = st.columns(2)
        
        with col_rep1:
            st.markdown("""
            <div class="mau2-card">
                <div style="height: 120px; background: linear-gradient(135deg, #f59e0b, #d97706); border-radius: 8px; margin-bottom: 1rem; display: flex; align-items: center; justify-content: center;">
                    <span style="color: white; font-size: 2rem;">🕳️</span>
                </div>
                <h4>Pothole on Main Street</h4>
                <p style="font-size: 0.9rem; color: #64748b; margin: 0.5rem 0;">Report of a large pothole causing traffic hazards on Main Street.</p>
                <button style="background: none; border: none; color: #3b82f6; font-weight: 500; cursor: pointer;">View Report</button>
            </div>
            """, unsafe_allow_html=True)
        
        with col_rep2:
            st.markdown("""
            <div class="mau2-card">
                <div style="height: 120px; background: linear-gradient(135deg, #ef4444, #dc2626); border-radius: 8px; margin-bottom: 1rem; display: flex; align-items: center; justify-content: center;">
                    <span style="color: white; font-size: 2rem;">🗑️</span>
                </div>
                <h4>Illegal Dumping near Riverbank</h4>
                <p style="font-size: 0.9rem; color: #64748b; margin: 0.5rem 0;">Report of illegal waste dumping near the riverbank, posing environmental risks.</p>
                <button style="background: none; border: none; color: #3b82f6; font-weight: 500; cursor: pointer;">View Report</button>
            </div>
            """, unsafe_allow_html=True)
    
    render_navigation()

# === CREATE PETITION PAGE ===
def render_create_petition():
    render_mau2_header()
    
    # Progress indicator
    st.markdown("""
    <div class="mau2-progress">
        <div class="mau2-progress-step active">1</div>
        <div style="width: 50px; height: 2px; background: #e2e8f0;"></div>
        <div class="mau2-progress-step">2</div>
        <div style="width: 50px; height: 2px; background: #e2e8f0;"></div>
        <div class="mau2-progress-step">3</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mau2-form-container">
        <div class="mau2-form-header">
            <h2>Create a Petition</h2>
            <p>Fill in the details below to start your petition.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("petition_form"):
        petition_title = st.text_input("Petition Title", placeholder="Enter a concise title for your petition")
        
        category = st.selectbox("Category", [
            "Select a category",
            "Transportation", 
            "Environment",
            "Infrastructure", 
            "Public Safety",
            "Education",
            "Healthcare"
        ])
        
        description = st.text_area(
            "Description", 
            placeholder="Provide a detailed description of the issue you want to address",
            height=150
        )
        
        col_submit, col_back = st.columns([1, 1])
        with col_submit:
            submitted = st.form_submit_button("Next →", use_container_width=True)
        with col_back:
            if st.form_submit_button("← Back to Dashboard", use_container_width=True):
                st.session_state.current_page = 'dashboard'
                st.rerun()
        
        if submitted:
            if petition_title and category != "Select a category" and description:
                st.session_state.petition_draft = {
                    'title': petition_title,
                    'category': category,
                    'description': description
                }
                st.session_state.current_page = 'petition_evidence'
                st.rerun()
            else:
                st.error("Please fill in all required fields")
    
    render_navigation()

# === PETITION EVIDENCE & LOCATION PAGE ===
def render_petition_evidence():
    render_mau2_header()
    
    # Progress indicator
    st.markdown("""
    <div class="mau2-progress">
        <div class="mau2-progress-step completed">✓</div>
        <div style="width: 50px; height: 2px; background: #10b981;"></div>
        <div class="mau2-progress-step active">2</div>
        <div style="width: 50px; height: 2px; background: #e2e8f0;"></div>
        <div class="mau2-progress-step">3</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mau2-form-container">
        <div class="mau2-form-header">
            <h2>Specify Location & Upload Evidence</h2>
            <p>Pinpoint the incident on the map and provide supporting evidence.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📍 Incident Location")
        
        # Simulated map placeholder
        st.markdown("""
        <div class="map-placeholder">
            <div style="text-align: center;">
                <div>🗺️ Interactive Map</div>
                <div style="font-size: 0.9rem; margin-top: 0.5rem;">San Francisco Bay Area</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        location_input = st.text_input("Address or Coordinates", placeholder="e.g., 123 Main St, City Hall")
        
        col_auto1, col_auto2 = st.columns(2)
        with col_auto1:
            auto_snap_time = st.checkbox("Auto-snap location & time", value=True)
        with col_auto2:
            manual_override = st.button("Manual override")
    
    with col2:
        st.markdown("### 📎 Upload Evidence")
        st.markdown("*Drag and drop files here*")
        st.markdown("*or*")
        
        # File uploader
        uploaded_files = st.file_uploader(
            "Browse files",
            type=['jpg', 'png', 'mp4', 'pdf', 'mp3'],
            accept_multiple_files=True,
            help="Supports: Images, Videos, PDFs, Voice Notes. Max 25MB."
        )
        
        if uploaded_files:
            st.success(f"✅ {len(uploaded_files)} file(s) uploaded successfully")
            for file in uploaded_files:
                st.markdown(f"📎 `{file.name}`")
        
        st.info("**Supports:** Images, Videos, PDFs, Voice Notes. Max 25MB.")
    
    col_back, col_next = st.columns([1, 1])
    with col_back:
        if st.button("← Back", key="back_to_petition_form", use_container_width=True):
            st.session_state.current_page = 'create_petition'
            st.rerun()
    
    with col_next:
        if st.button("Submit Report →", key="submit_report", use_container_width=True):
            with st.spinner("Submitting report..."):
                time.sleep(2)
            st.success("✅ Report submitted successfully!")
            time.sleep(1)
            st.session_state.current_page = 'dashboard'
            st.rerun()
    
    render_navigation()

# === ANALYTICS PAGE ===
def render_analytics():
    render_mau2_header()
    
    st.markdown("## Analytics & Insights")
    st.markdown("*Key performance indicators for the MAU2 platform.*")
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="mau2-metric-card">
            <div class="mau2-metric-value">1,234</div>
            <div class="mau2-metric-label">Petitions Opened</div>
            <div style="color: #10b981; font-size: 0.9rem; margin-top: 0.5rem;">↗ +10%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="mau2-metric-card">
            <div class="mau2-metric-value">876</div>
            <div class="mau2-metric-label">Petitions Closed</div>
            <div style="color: #ef4444; font-size: 0.9rem; margin-top: 0.5rem;">↘ -5%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="mau2-metric-card">
            <div class="mau2-metric-value">2 days</div>
            <div class="mau2-metric-label">Avg. Response Time</div>
            <div style="color: #10b981; font-size: 0.9rem; margin-top: 0.5rem;">↗ +2%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="mau2-metric-card">
            <div class="mau2-metric-value">95%</div>
            <div class="mau2-metric-label">Verification Rate</div>
            <div style="color: #10b981; font-size: 0.9rem; margin-top: 0.5rem;">↗ +1%</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Map section
    st.markdown("### Incident Concentration Heatmap")
    
    st.markdown("""
    <div class="map-placeholder" style="height: 400px;">
        <div style="text-align: center;">
            <div>🌡️ Heat Map Visualization</div>
            <div style="font-size: 0.9rem; margin-top: 0.5rem;">New York Metro Area</div>
            <div style="margin-top: 1rem; display: flex; justify-content: center; gap: 1rem;">
                <span style="background: #ef4444; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.8rem;">High Activity</span>
                <span style="background: #f59e0b; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.8rem;">Medium Activity</span>
                <span style="background: #10b981; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.8rem;">Low Activity</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Charts section
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("### Petition Trends")
        st.markdown("*Opened vs. Closed over the last 6 months*")
        
        # Simple data for line chart
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        opened = [120, 135, 145, 160, 140, 155]
        closed = [100, 115, 125, 140, 130, 145]
        
        chart_data = pd.DataFrame({
            'Month': months + months,
            'Count': opened + closed,
            'Type': ['Opened'] * 6 + ['Closed'] * 6
        })
        
        st.line_chart(chart_data.pivot(index='Month', columns='Type', values='Count'))
    
    with col_chart2:
        st.markdown("### Response Time by Category")
        st.markdown("*Average days to first response*")
        
        categories = ['Road Safety', 'Public Health', 'Environment', 'Infrastructure', 'Other']
        response_times = [2.8, 2.1, 1.8, 3.2, 1.5]
        
        chart_data = pd.DataFrame({
            'Category': categories,
            'Response Time (Days)': response_times
        })
        
        st.bar_chart(chart_data.set_index('Category'))
    
    render_navigation()

# === SETTINGS PAGE ===
def render_settings():
    render_mau2_header()
    
    st.markdown("# Settings")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🛡️ Privacy")
        
        incognito_mode = st.toggle("Incognito Mode", help="Browse privately. Your activity won't be saved.")
        
    with col2:
        st.markdown("### 🔔 Notifications")
        
        general_notifications = st.toggle("General Notifications", value=True, help="Receive updates on petitions, issues, and community activity.")
        
        interaction_notifications = st.toggle("Interaction Notifications", value=True, help="Get notified about new comments and reactions on your posts.")
    
    st.markdown("---")
    
    st.markdown("### 🔐 Security")
    
    if st.button("Enable Two-Factor Authentication", use_container_width=True):
        st.info("Two-factor authentication setup would be initiated here.")
    
    st.markdown("---")
    
    st.markdown("*For more detailed information on how we handle your data, please refer to our [Privacy Policy](#).*")
    
    render_navigation()

# === MAIN APP ROUTING ===
def main():
    page = st.session_state.get('current_page', 'landing')
    
    if page == 'landing':
        render_landing_page()
    elif page == 'onboarding':
        render_onboarding_page()
    elif page == 'dashboard':
        render_dashboard()
    elif page == 'create_petition':
        render_create_petition()
    elif page == 'petition_evidence':
        render_petition_evidence()
    elif page == 'analytics':
        render_analytics()
    elif page == 'settings':
        render_settings()
    else:
        render_dashboard()  # Default fallback

if __name__ == "__main__":
    main()
