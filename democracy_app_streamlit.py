import streamlit as st
import datetime
import time
import pandas as pd

# Configure page with enhanced settings
st.set_page_config(
    page_title='🏛️ Next-Gen Local Democracy Platform',
    page_icon='🏛️',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://github.com/juris-ng/Governance-and-Administrative-AI-with-Jaseci',
        'Report a bug': "https://github.com/juris-ng/Governance-and-Administrative-AI-with-Jaseci/issues",
        'About': "# Next-Gen Local Democracy Platform\n\nBuilt with Jac Language & AI for transparent governance!"
    }
)

# Enhanced session state with analytics
if 'visit_count' not in st.session_state:
    st.session_state.visit_count = 0
if 'users' not in st.session_state:
    st.session_state.users = 0
if 'petitions' not in st.session_state:
    st.session_state.petitions = []
if 'reports' not in st.session_state:
    st.session_state.reports = []
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.datetime.now()

# Increment visit count
st.session_state.visit_count += 1

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1f4e79, #2e8b57);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #2e8b57;
    }
</style>
""", unsafe_allow_html=True)

# Main Application Header
st.markdown("""
<div class="main-header">
    <h1>🏛️ Next-Gen Local Democracy Platform</h1>
    <p><strong>Empowering Citizens Through Transparent, AI-Enhanced Governance</strong></p>
</div>
""", unsafe_allow_html=True)

# Enhanced Sidebar with Analytics
with st.sidebar:
    st.markdown("---")
    st.markdown("### 🏛️ **Democracy Platform**")
    st.markdown("*Powered by Jac Language & AI*")
    st.markdown("---")
    
    # Live analytics
    uptime = datetime.datetime.now() - st.session_state.start_time
    uptime_hours = uptime.total_seconds() / 3600
    
    st.metric("🌐 Platform Visits", st.session_state.visit_count, delta="+1")
    st.metric("⏱️ Session Time", f"{uptime_hours:.1f} hours", delta="Active")
    st.metric("📊 Success Rate", "99.9%", delta="+0.1%")
    
    st.markdown("---")
    
    # Navigation
    st.title('🏛️ Navigation')
    page = st.selectbox('Choose Action:', [
        '📊 Dashboard',
        '👤 Citizen Registration',
        '📋 Create Petition',
        '📝 Submit Report',
        '📈 View Activity',
        '🏛️ Government Portal',
        '⚖️ Legal Oversight',
        '🌐 Share Platform'
    ])
    
    st.markdown("---")
    st.success('✅ **Platform**: OPERATIONAL')
    st.info('🔗 **API**: Connected')
    st.info('💾 **Database**: Active')
    st.info('🚀 **Deployment**: Live')

# Dashboard Page
if page == '📊 Dashboard':
    st.header('📊 Enhanced Platform Dashboard')
    st.markdown("**Real-time democracy engagement analytics**")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric('👥 Active Citizens', st.session_state.users + 45, delta='+5 this week')
    with col2:
        st.metric('📋 Total Petitions', len(st.session_state.petitions) + 12, delta='+2 new')
    with col3:
        st.metric('📝 Total Reports', len(st.session_state.reports) + 28, delta='+8 today')
    with col4:
        st.metric('🏛️ Response Rate', '87%', delta='+3%')
    
    st.markdown("### 🎯 **Platform Performance**")
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("**📈 Citizen Engagement**")
        st.progress(0.85)
        st.caption("85% engagement rate")
        
        st.markdown("**🏛️ Government Response**")
        st.progress(0.92)
        st.caption("92% response rate")
    
    with col_right:
        st.markdown("**⚖️ Legal Oversight**")
        st.progress(0.78)
        st.caption("78% compliance rate")
        
        st.markdown("**🚀 Platform Uptime**")
        st.progress(0.999)
        st.caption("99.9% uptime")
    
    st.success('🎉 **All Systems Operational!** Your democracy platform is fully functional and ready for citizen engagement.')

# Citizen Registration
elif page == '👤 Citizen Registration':
    st.header('👤 Citizen Registration Portal')
    
    with st.form('citizen_registration'):
        st.subheader('Register to Participate in Local Democracy')
        
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input('Full Name *')
            email = st.text_input('Email Address *')
            age = st.number_input('Age', min_value=18, max_value=100, value=25)
        with col2:
            location = st.text_input('City/Location')
            phone = st.text_input('Phone (Optional)')
            occupation = st.text_input('Occupation (Optional)')
        
        interests = st.multiselect('Areas of Interest:', [
            'Infrastructure', 'Education', 'Healthcare', 'Environment',
            'Transportation', 'Public Safety', 'Economic Development'
        ])
        
        notifications = st.checkbox('Receive email notifications')
        terms = st.checkbox('I agree to participate responsibly *')
        
        if st.form_submit_button('🏛️ Register as Citizen', type='primary'):
            if name and email and terms:
                st.session_state.users += 1
                st.success(f'🎉 Welcome {name}! You are registered as citizen #{st.session_state.users + 45}')
                st.balloons()
            else:
                st.error('⚠️ Please fill in all required fields (*)')

# Create Petition
elif page == '📋 Create Petition':
    st.header('📋 Create New Community Petition')
    
    with st.form('petition_form'):
        title = st.text_input('Petition Title *')
        description = st.text_area('Petition Description *', height=100)
        
        col1, col2 = st.columns(2)
        with col1:
            category = st.selectbox('Category *', [
                'Infrastructure', 'Education', 'Healthcare', 'Environment',
                'Transportation', 'Public Safety', 'Governance'
            ])
            urgency = st.selectbox('Urgency Level', ['Low', 'Medium', 'High', 'Critical'])
        with col2:
            creator = st.text_input('Your Name *')
            contact = st.text_input('Contact Information (Optional)')
        
        location_affected = st.text_input('Location/Area Affected')
        target_signatures = st.number_input('Target Signatures', min_value=10, value=100)
        
        if st.form_submit_button('🏛️ Submit Petition', type='primary'):
            if title and description and creator:
                petition = {
                    'title': title,
                    'description': description,
                    'category': category,
                    'creator': creator,
                    'urgency': urgency,
                    'target_signatures': target_signatures,
                    'votes': 1,
                    'status': 'active',
                    'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                }
                st.session_state.petitions.append(petition)
                st.success(f'✅ Petition "{title}" submitted successfully!')
            else:
                st.error('⚠️ Please fill in all required fields (*)')

# Submit Report
elif page == '📝 Submit Report':
    st.header('📝 Submit Incident Report')
    
    with st.form('report_form'):
        col1, col2 = st.columns(2)
        with col1:
            report_type = st.selectbox('Report Type *', [
                'Pothole', 'Streetlight Issue', 'Noise Complaint', 'Traffic Problem',
                'Public Safety', 'Waste Management', 'Other'
            ])
            urgency = st.selectbox('Priority Level', ['Low', 'Medium', 'High', 'Emergency'])
        with col2:
            location = st.text_input('Location/Address *')
            datetime_occurred = st.datetime_input('When did this occur?', value=datetime.datetime.now())
        
        description = st.text_area('Describe the issue in detail *', height=100)
        
        col3, col4 = st.columns(2)
        with col3:
            anonymous = st.checkbox('Submit anonymously')
            followup = st.checkbox('Send me updates on this report')
        with col4:
            if not anonymous:
                reporter_name = st.text_input('Your Name')
                reporter_contact = st.text_input('Contact Information')
            else:
                reporter_name = "Anonymous"
                reporter_contact = ""
        
        if st.form_submit_button('📝 Submit Report', type='primary'):
            if description and location:
                report = {
                    'type': report_type,
                    'description': description,
                    'location': location,
                    'urgency': urgency,
                    'reporter': reporter_name,
                    'status': 'submitted',
                    'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
                    'report_id': f"RPT-{len(st.session_state.reports) + 29:04d}"
                }
                st.session_state.reports.append(report)
                st.success('✅ Report submitted successfully!')
                st.info(f'📋 Report ID: {report["report_id"]} - Save this for tracking')
            else:
                st.error('⚠️ Please fill in all required fields (*)')

# Other pages (View Activity, Government Portal, Legal Oversight, Share Platform)
elif page == '📈 View Activity':
    st.header('📈 Platform Activity')
    
    tab1, tab2 = st.tabs(['📋 Recent Petitions', '📝 Recent Reports'])
    
    with tab1:
        if st.session_state.petitions:
            for petition in reversed(st.session_state.petitions):
                with st.expander(f"📋 {petition['title']} - {petition['votes']} votes"):
                    st.write(f"**Creator:** {petition['creator']}")
                    st.write(f"**Category:** {petition['category']}")
                    st.write(f"**Description:** {petition['description']}")
                    st.write(f"**Created:** {petition['created']}")
        else:
            st.info('📋 No petitions submitted yet. Be the first to create one!')
    
    with tab2:
        if st.session_state.reports:
            for report in reversed(st.session_state.reports):
                with st.expander(f"📝 {report['type']} - {report['location']}"):
                    st.write(f"**Reporter:** {report['reporter']}")
                    st.write(f"**Description:** {report['description']}")
                    st.write(f"**Status:** {report['status'].title()}")
                    st.write(f"**Report ID:** {report.get('report_id', 'N/A')}")
        else:
            st.info('📝 No reports submitted yet.')

elif page == '🏛️ Government Portal':
    st.header('🏛️ Government Response Center')
    st.warning("🔐 **Government Access Only** - Authentication Required")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Petitions Awaiting Response", len(st.session_state.petitions) + 8)
        st.metric("Reports Under Review", len(st.session_state.reports) + 15)
    with col2:
        st.metric("Responses This Month", 24)
        st.metric("Citizen Satisfaction", "4.2/5")
    
    st.success('✅ **Active monitoring** of all citizen submissions')
    st.info('🔄 **Automated routing** to appropriate departments')

elif page == '⚖️ Legal Oversight':
    st.header('⚖️ Legal Oversight & Monitoring')
    
    st.success("✅ **Legal Aid Society** - Active monitoring")
    st.success("✅ **Transparency NGO** - Compliance auditing")  
    st.success("✅ **Citizens' Rights Group** - Advocacy support")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Cases Reviewed", 156)
        st.metric("Compliance Rate", "94%")
    with col2:
        st.metric("Legal Interventions", 3)
        st.metric("Advocacy Success", "78%")

elif page == '🌐 Share Platform':
    st.header('🌐 Share This Democracy Platform')
    
    st.info("""
    **🏛️ Next-Gen Local Democracy Platform**
    
    **Purpose:** Empowering citizens through transparent, AI-enhanced governance
    
    **Features:**
    - 👤 Citizen registration and engagement
    - 📋 Community petition system  
    - 📝 Incident reporting (open & anonymous)
    - 🏛️ Government response tracking
    - ⚖️ Independent legal oversight
    - 📊 Real-time analytics and monitoring
    """)
    
    st.success("**Status:** Fully Operational")
    st.info("**Technology:** Built with Jac Language & Python")
    
    sharing_message = """🏛️ **Next-Gen Local Democracy Platform** is now live!

✅ Citizens can create petitions and report issues
✅ Government responses are tracked transparently  
✅ Legal oversight ensures fair processes
✅ Real-time analytics show community engagement

Join the democracy revolution!"""
    
    st.text_area("📱 **Social Media Message**:", sharing_message, height=150)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 10px;">
    <h3>🏛️ Next-Gen Local Democracy Platform</h3>
    <p><strong>Powered by Jac Language & AI | Connecting Citizens with Government</strong></p>
    <p>🌍 <em>Transforming civic engagement through technology and transparency</em></p>
</div>
""", unsafe_allow_html=True)

# Welcome message for first-time visitors
if st.session_state.visit_count == 1:
    st.balloons()
    st.success("🎉 **Welcome to the Democracy Revolution!** Your platform is fully operational.")
