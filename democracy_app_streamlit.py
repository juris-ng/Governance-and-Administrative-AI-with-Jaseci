# MAU2 Democracy Platform - Complete Professional Implementation
# Inspired by MAU2 UI/UX Screenshots - Production Ready
# Live at: https://mauvoice.streamlit.app/

import streamlit as st
import datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
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
    
    /* Privacy Controls */
    .mau2-privacy-controls {
        background: #f8fafc;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        border: 1px solid #e2e8f0;
    }
    
    .mau2-privacy-toggle {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .mau2-toggle-option {
        flex: 1;
        padding: 1rem;
        border: 2px solid #e2e8f0;
        border-radius: 8px;
        cursor: pointer;
        text-align: center;
        transition: all 0.3s;
    }
    
    .mau2-toggle-option.selected {
        border-color: #3b82f6;
        background: #dbeafe;
    }
    
    /* Map Container */
    .mau2-map-container {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin: 1rem 0;
    }
    
    /* Analytics Cards */
    .mau2-analytics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .mau2-metric-card {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
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
    
    /* Timeline Styling */
    .mau2-timeline {
        position: relative;
        padding-left: 2rem;
    }
    
    .mau2-timeline::before {
        content: '';
        position: absolute;
        left: 15px;
        top: 0;
        height: 100%;
        width: 2px;
        background: #e2e8f0;
    }
    
    .mau2-timeline-item {
        position: relative;
        margin-bottom: 2rem;
    }
    
    .mau2-timeline-marker {
        position: absolute;
        left: -20px;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #3b82f6;
        border: 3px solid white;
        box-shadow: 0 0 0 3px #3b82f6;
    }
    
    .mau2-timeline-content {
        background: white;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
    }
    
    /* Notification Styling */
    .mau2-notification {
        background: white;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-left: 4px solid #3b82f6;
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .mau2-notification.success {
        border-left-color: #10b981;
    }
    
    .mau2-notification.warning {
        border-left-color: #f59e0b;
    }
    
    .mau2-notification.error {
        border-left-color: #ef4444;
    }
    
    /* Hide Streamlit branding */
    #MainMenu, .stDeployButton, footer, header {
        visibility: hidden !important;
    }
    
    .stApp > div:first-child {
        padding-top: 0;
    }
</style>
""", unsafe_allow_html=True)

# === HEADER COMPONENT ===
def render_mau2_header():
    st.markdown(f"""
    <div class="mau2-header">
        <div class="mau2-logo">
            <span style="background: linear-gradient(45deg, #ffffff, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800;">MAU2</span>
        </div>
        <div class="mau2-nav">
            <a href="#" class="mau2-nav-item">Home</a>
            <a href="#" class="mau2-nav-item">Petitions</a>
            <a href="#" class="mau2-nav-item">Reports</a>
            <a href="#" class="mau2-nav-item">Community</a>
            <a href="#" class="mau2-nav-item">About</a>
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
        <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
            <button class="mau2-btn-primary" onclick="window.location.href='#get-started'">
                Get Started
            </button>
        </div>
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

# === MAIN DASHBOARD ===
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
        if st.button("⚙️ Settings", use_container_width=True):
            st.session_state.current_page = 'settings'
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
        
        if st.form_submit_button("Next", use_container_width=True):
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
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("← Back to Dashboard", key="back_to_dashboard"):
        st.session_state.current_page = 'dashboard'
        st.rerun()

# === PETITION EVIDENCE & LOCATION PAGE ===
def render_petition_evidence():
    render_mau2_header()
    
    # Progress indicator
    st.markdown("""
    <div class="mau2-progress">
        <div class="mau2-progress-step completed">1</div>
        <div style="width: 50px; height: 2px; background: #10b981;"></div>
        <div class="mau2-progress-step active">2</div>
        <div style="width: 50px; height: 2px; background: #e2e8f0;"></div>
        <div class="mau2-progress-step">3</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mau2-form-container">
        <div class="mau2-form-header">
            <h2>Add Evidence & Location</h2>
            <p>Upload images, short videos (max 60s), PDFs, or voice notes to support your petition. Clear and relevant evidence strengthens your case.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Upload Evidence")
        
        # File uploader with custom styling
        uploaded_files = st.file_uploader(
            "",
            type=['jpg', 'png', 'mp4', 'pdf', 'mp3'],
            accept_multiple_files=True,
            help="Supports: JPG, PNG, MP4, PDF, MP3"
        )
        
        if uploaded_files:
            st.success(f"✅ {len(uploaded_files)} file(s) uploaded successfully")
            for file in uploaded_files:
                st.write(f"📎 {file.name}")
    
    with col2:
        st.markdown("### Specify Location")
        st.markdown("*Pinpoint the location of the issue on the map.*")
        
        # Simulated map placeholder
        st.markdown("""
        <div style="height: 200px; background: linear-gradient(135deg, #93c5fd, #60a5fa); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 1rem 0;">
            <span style="color: white; font-size: 1.2rem;">🗺️ Interactive Map</span>
        </div>
        """, unsafe_allow_html=True)
        
        location_input = st.text_input("Location", placeholder="e.g., City Hall, 123 Main St")
        
        col_auto1, col_auto2 = st.columns(2)
        with col_auto1:
            auto_snap_time = st.checkbox("Auto-snap timestamp from evidence metadata", value=True)
        with col_auto2:
            auto_snap_geo = st.checkbox("Auto-snap geotag from evidence metadata", value=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    col_back, col_next = st.columns([1, 1])
    with col_back:
        if st.button("← Back", key="back_to_petition_form", use_container_width=True):
            st.session_state.current_page = 'create_petition'
            st.rerun()
    
    with col_next:
        if st.button("Next: Review & Submit →", key="next_to_review", use_container_width=True):
            st.session_state.current_page = 'petition_review'
            st.rerun()

# === PETITION REVIEW & SUBMIT ===
def render_petition_review():
    render_mau2_header()
    
    # Progress indicator
    st.markdown("""
    <div class="mau2-progress">
        <div class="mau2-progress-step completed">1</div>
        <div style="width: 50px; height: 2px; background: #10b981;"></div>
        <div class="mau2-progress-step completed">2</div>
        <div style="width: 50px; height: 2px; background: #10b981;"></div>
        <div class="mau2-progress-step active">3</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mau2-form-container">
        <div class="mau2-form-header">
            <h2>Review and Submit Petition</h2>
            <p>Final step to make your voice heard. Please review the details below.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Privacy Settings
    st.markdown("### Privacy Settings")
    st.markdown("*Choose how your identity is displayed.*")
    
    col_pub, col_priv = st.columns(2)
    
    with col_pub:
        if st.button("👁️ Public", key="public_option", use_container_width=True):
            st.session_state.petition_privacy = 'public'
    
    with col_priv:
        if st.button("🔒 Private", key="private_option", use_container_width=True):
            st.session_state.petition_privacy = 'private'
    
    incognito_mode = st.checkbox("🕵️ Incognito Mode", help="Report privately — MAU2 will hide your identity from public listings; organizations may still request verification.")
    
    # Petition Summary
    if 'petition_draft' in st.session_state:
        draft = st.session_state.petition_draft
        
        st.markdown("### Petition Summary")
        
        summary_data = {
            "Title": draft.get('title', 'N/A'),
            "Description": draft.get('description', 'N/A')[:100] + "..." if len(draft.get('description', '')) > 100 else draft.get('description', 'N/A'),
            "Category": draft.get('category', 'N/A'),
            "Location": "Elm Street, Springfield"  # Placeholder
        }
        
        for key, value in summary_data.items():
            st.write(f"**{key}**: {value}")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    col_back, col_submit = st.columns([1, 1])
    with col_back:
        if st.button("← Back", key="back_to_evidence", use_container_width=True):
            st.session_state.current_page = 'petition_evidence'
            st.rerun()
    
    with col_submit:
        if st.button("Submit Petition", key="submit_petition", use_container_width=True):
            # Simulate petition submission
            with st.spinner("Submitting petition..."):
                time.sleep(2)
            
            st.success("✅ Petition submitted successfully!")
            st.info("📧 Petition submitted — 4 organizations auto-notified")
            
            # Add to session state
            if 'petition_draft' in st.session_state:
                petition = st.session_state.petition_draft.copy()
                petition['id'] = f"PET-{len(st.session_state.petitions) + 1:04d}"
                petition['status'] = 'submitted'
                petition['votes'] = 1
                petition['submitted_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
                st.session_state.petitions.append(petition)
            
            time.sleep(2)
            st.session_state.current_page = 'dashboard'
            st.rerun()

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
    elif page == 'petition_review':
        render_petition_review()
    else:
        render_dashboard()  # Default fallback

if __name__ == "__main__":
    main()
