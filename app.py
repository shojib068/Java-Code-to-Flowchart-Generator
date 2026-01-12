import streamlit as st
from main import java_code2flow

# -----------------------------
# Page Config & Styles
# -----------------------------
st.set_page_config(
    page_title="🧠 Java Code → Workflow",
    layout="wide",
    page_icon="🧩"
)

# Custom CSS for dashing UI
st.markdown("""
<style>
/* Background gradient */
body {
    background: linear-gradient(to right, #1c1c1c, #2c3e50);
    color: #f5f5f5;
}

/* Hide Streamlit header/footer */
header, footer {visibility: hidden;}

/* Custom card for text area */
textarea {
    border-radius: 12px !important;
    border: 2px solid #4CAF50 !important;
    padding: 10px !important;
    font-size: 16px !important;
}

/* Button styling */
.stButton>button {
    background: linear-gradient(90deg, #4CAF50, #2ecc71);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 20px;
    transition: 0.3s;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #2ecc71, #27ae60);
}

/* Mermaid diagram container */
.mermaid {
    background: #1e1e2f;
    padding: 15px;
    border-radius: 15px;
    color: #f5f5f5;
}

/* Cards for code download section */
.download-card {
    background: #2c3e50;
    padding: 15px;
    border-radius: 15px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.markdown("## 🛠 Options")
st.sidebar.markdown("- Paste your Java code")
st.sidebar.markdown("- Click 'Generate Flowchart'")
st.sidebar.markdown("- Download the Mermaid source for sharing")

# -----------------------------
# Title & Description
# -----------------------------
st.markdown("<h1 style='text-align:center; color:#4CAF50;'>🧠 Java Code → Human Workflow Diagram</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px;'>Paste your Java code below to generate an interactive workflow diagram.</p>", unsafe_allow_html=True)

# -----------------------------
# Input area
# -----------------------------
code = st.text_area(
    "Paste your Java code here:",
    height=350,
    placeholder="public class Example { ... }"
)

# -----------------------------
# Generate Workflow Button
# -----------------------------
if st.button("Generate Flowchart"):
    if code.strip():
        # Generate Mermaid workflow
        mermaid = java_code2flow(code)

        # Display Mermaid diagram scrollable
        mermaid_html = f"""
        <div style="overflow: auto; width: 100%; height: 700px; border: 2px solid #4CAF50; border-radius: 15px; padding: 10px;">
            <div class="mermaid">{mermaid}</div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <script>
            mermaid.initialize({{ startOnLoad: true, flowchart: {{ curve: 'basis' }}}});
        </script>
        """
        st.components.v1.html(mermaid_html, height=720)

        # Show Mermaid code for download
        st.markdown("<h3 style='color:#4CAF50;'>📝 Mermaid Source</h3>", unsafe_allow_html=True)
        st.code(mermaid, language="mermaid")

        # Download Mermaid source in a nice card
        st.markdown('<div class="download-card">', unsafe_allow_html=True)
        st.download_button(
            label="📥 Download Mermaid Source",
            data=mermaid,
            file_name="workflow.mmd",
            mime="text/plain"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please paste Java code first!")
