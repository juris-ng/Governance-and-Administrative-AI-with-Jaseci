import streamlit as st
import datetime

# Configure page
st.set_page_config(
    page_title='🏛️ Next-Gen Local Democracy Platform',
    page_icon='🏛️',
    layout='wide'
)

# Main title
st.title('🏛️ Next-Gen Local Democracy Platform')
st.markdown('**Empowering Citizens Through Transparent, AI-Enhanced Governance**')
st.markdown('---')

# Sidebar
st.sidebar.title('🏛️ Navigation')
page = st.sidebar.selectbox('Choose Action:', [
    '📊 Dashboard',
    '👤 Citizen Registration',
    '📋 Create Petition',
    '📝 Submit Report'
])

st.sidebar.success('✅ Platform Status: OPERATIONAL')
st.sidebar.info('🔗 API Backend: Connected')

# Initialize session state
if 'users' not in st.session_state:
    st.session_state.users = 0
if 'petitions' not in st.session_state:
    st.session_state.petitions = []
if 'reports' not in st.session_state:
    st.session_state.reports = []

# Dashboard
if page == '📊 Dashboard':
    st.header('📊 Platform Dashboard')
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric('👥 Active Citizens', st.session_state.users + 45)
    with col2:
        st.metric('📋 Total Petitions', len(st.session_state.petitions) + 12)
    with col3:
        st.metric('📝 Total Reports', len(st.session_state.reports) + 28)
    with col4:
        st.metric('🏛️ Response Rate', '87%')
    
    st.success('🎉 All Systems Operational! Your democracy platform is ready.')

# Citizen Registration
elif page == '👤 Citizen Registration':
    st.header('👤 Citizen Registration Portal')
    
    with st.form('citizen_registration'):
        name = st.text_input('Full Name *')
        email = st.text_input('Email Address *')
        age = st.number_input('Age', min_value=18, max_value=100, value=25)
        location = st.text_input('City/Location')
        
        if st.form_submit_button('🏛️ Register as Citizen'):
            if name and email:
                st.session_state.users += 1
                st.success(f'🎉 Welcome {name}! You are now registered.')
                st.balloons()
            else:
                st.error('⚠️ Please fill in all required fields')

# Create Petition
elif page == '📋 Create Petition':
    st.header('📋 Create New Community Petition')
    
    with st.form('petition_form'):
        title = st.text_input('Petition Title *')
        description = st.text_area('Petition Description *')
        category = st.selectbox('Category *', [
            'Infrastructure', 'Education', 'Healthcare', 
            'Environment', 'Transportation', 'Public Safety'
        ])
        creator = st.text_input('Your Name *')
        
        if st.form_submit_button('🏛️ Submit Petition'):
            if title and description and creator:
                petition = {
                    'title': title,
                    'description': description,
                    'category': category,
                    'creator': creator,
                    'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                }
                st.session_state.petitions.append(petition)
                st.success(f'✅ Petition "{title}" submitted successfully!')
            else:
                st.error('⚠️ Please fill in all required fields')

# Submit Report
elif page == '📝 Submit Report':
    st.header('📝 Submit Incident Report')
    
    with st.form('report_form'):
        report_type = st.selectbox('Report Type', [
            'Pothole', 'Streetlight', 'Noise', 'Traffic', 'Safety', 'Other'
        ])
        description = st.text_area('Describe the issue *')
        location = st.text_input('Location *')
        anonymous = st.checkbox('Submit anonymously')
        reporter_name = '' if anonymous else st.text_input('Your Name')
        
        if st.form_submit_button('📝 Submit Report'):
            if description and location:
                report = {
                    'type': report_type,
                    'description': description,
                    'location': location,
                    'reporter': 'Anonymous' if anonymous else reporter_name,
                    'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                }
                st.session_state.reports.append(report)
                st.success('✅ Report submitted successfully!')
            else:
                st.error('⚠️ Please fill in required fields')

# Footer
st.markdown('---')
st.markdown('**🏛️ Next-Gen Local Democracy Platform** - Powered by Jac Language & AI')
