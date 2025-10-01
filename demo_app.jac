import:py streamlit as st;

node democracy_platform {
    has platform_name: str = "Next-Gen Local Democracy";
    has active_users: int = 0;
    has total_petitions: int = 0;
    has total_reports: int = 0;
}

node citizen {
    has name: str;
    has petitions_created: list = [];
}

with entry {
    st.title("🏛️ Democracy Platform Demo");
    st.write("Welcome to the Next-Gen Local Democracy Platform!");
    
    # Create platform
    platform = spawn democracy_platform();
    
    # Display platform info
    st.header("📊 Platform Overview");
    st.write(f"Platform: {platform.platform_name}");
    
    # Citizen interaction
    st.header("👤 Citizen Portal");
    citizen_name = st.text_input("Enter your name:");
    
    if st.button("Join Platform") and citizen_name {
        citizen1 = spawn citizen(name=citizen_name);
        platform.active_users += 1;
        st.success(f"Welcome {citizen_name}! You are now registered.");
        st.write(f"Total users: {platform.active_users}");
    }
    
    # Petition creation
    st.header("📋 Create Petition");
    petition_title = st.text_input("Petition Title:");
    petition_desc = st.text_area("Petition Description:");
    
    if st.button("Submit Petition") and petition_title {
        platform.total_petitions += 1;
        st.success(f"Petition '{petition_title}' submitted successfully!");
        st.write(f"Total petitions: {platform.total_petitions}");
    }
    
    # Report submission
    st.header("📝 Submit Report");
    report_type = st.selectbox("Report Type:", ["Pothole", "Streetlight", "Noise", "Other"]);
    report_desc = st.text_area("Report Description:");
    
    if st.button("Submit Report") and report_desc {
        platform.total_reports += 1;
        st.success(f"Report about {report_type} submitted!");
        st.write(f"Total reports: {platform.total_reports}");
    }
    
    # Platform statistics
    st.header("📊 Platform Statistics");
    col1, col2, col3 = st.columns(3);
    
    with col1 {
        st.metric("Active Users", platform.active_users);
    }
    with col2 {
        st.metric("Total Petitions", platform.total_petitions);
    }
    with col3 {
        st.metric("Total Reports", platform.total_reports);
    }
}