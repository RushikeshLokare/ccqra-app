import streamlit as st
import time

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="CCQRA – Carbon Credit Quality Assessment",
    layout="wide"
)

# -------------------------------
# Header
# -------------------------------
st.title("Carbon Credit Quality & Risk Assessment Assistant")
st.subheader("AI-native decision support for voluntary carbon markets")

st.markdown(
    "Upload a carbon project document to receive a structured quality assessment, "
    "risk flags, and an investor-ready recommendation."
)

st.divider()

# -------------------------------
# Document Upload Section
# -------------------------------
st.header("Project Document Input")

uploaded_file = st.file_uploader(
    "📄 Upload Carbon Project Document (PDF)",
    type=["pdf"],
    help="Accepted files: Project Design Documents (PDDs), Monitoring Reports. Max file size: 20 MB."
)

st.caption("We analyze unstructured documents — no templates or formatting required.")

# -------------------------------
# Run Assessment Button
# -------------------------------
run = st.button("Run Quality Assessment")

# -------------------------------
# Processing State
# -------------------------------
if run and uploaded_file is not None:
    with st.spinner("Analyzing Project Quality..."):
        st.markdown(
            "Extracting project claims, checking assumptions, "
            "and evaluating risks across key quality dimensions."
        )
        time.sleep(2)

    st.divider()

    # -------------------------------
    # Results Header
    # -------------------------------
    st.header("Carbon Project Quality Assessment")
    st.caption(
        "This assessment provides decision support — it does not replace third-party verification."
    )

    # -------------------------------
    # Top Summary Cards
    # -------------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Overall Project Quality Score")
        st.metric(
            label="Score",
            value="72 / 100"
        )
        st.caption(
            "Moderate quality with identifiable risk areas requiring targeted due diligence."
        )

    with col2:
        st.subheader("Recommended Action")
        st.markdown(
            "### **Investigate Further Before Proceeding**"
        )
        st.caption(
            "Key risks identified in baseline integrity and long-term permanence assumptions."
        )

    st.divider()

    # -------------------------------
    # Quality Dimension Scores
    # -------------------------------
    st.subheader("Quality Dimension Scores")

    q1, q2, q3, q4, q5 = st.columns(5)

    with q1:
        st.metric("Additionality", "14 / 20")
        st.caption("Likelihood that emissions reductions would not occur without carbon finance")

    with q2:
        st.metric("Permanence", "13 / 20")
        st.caption("Risk of reversal or loss of credited emissions reductions")

    with q3:
        st.metric("Baseline Integrity", "12 / 20")
        st.caption("Credibility and conservativeness of baseline assumptions")

    with q4:
        st.metric("Leakage Risk", "16 / 20")
        st.caption("Risk of emissions displacement outside project boundaries")

    with q5:
        st.metric("Co-Benefits & SDG Alignment", "17 / 20")
        st.caption("Environmental and social benefits beyond carbon mitigation")

    st.divider()

    # -------------------------------
    # Risk Flags Section
    # -------------------------------
    st.subheader("Key Risk Flags Identified")

    st.warning(
        "**Baseline Inflation Risk**  \n"
        "Baseline relies on regional averages that may not reflect current policy or market conditions."
    )

    st.warning(
        "**Permanence Uncertainty**  \n"
        "Limited long-term monitoring commitments increase reversal risk beyond the crediting period."
    )

    st.warning(
        "**Data Verification Gaps**  \n"
        "Certain emissions factors lack third-party validation references."
    )

    st.caption(
        "These risks do not invalidate the project, but materially affect credit credibility and pricing."
    )

    st.divider()

    # -------------------------------
    # Due Diligence Checklist
    # -------------------------------
    st.subheader("Targeted Due Diligence Checklist")

    st.checkbox("Verify baseline assumptions against updated regional benchmarks")
    st.checkbox("Review permanence safeguards and buffer mechanisms")
    st.checkbox("Validate emissions factors with third-party sources")
    st.checkbox("Assess long-term monitoring and reporting commitments")

    st.caption("Focus human review on flagged areas to reduce time and cost.")

    st.divider()

    # -------------------------------
    # Investor-Ready Advisory Note
    # -------------------------------
    st.subheader("Executive Advisory Summary")

    st.markdown(
        """
        Based on the document analysis, the project demonstrates moderate additionality
        and co-benefits. However, weaknesses in baseline integrity and permanence
        assumptions introduce material quality risk. Proceeding without further
        verification may expose buyers to reputational and performance risk.
        """
    )

    st.caption("Prepared for investment and procurement decision-makers")

    st.divider()

    # -------------------------------
    # Footer Disclaimer
    # -------------------------------
    st.caption(
        "CCQRA provides AI-assisted decision support only. "
        "Final investment decisions should include independent verification "
        "and professional judgment."
    )

elif run and uploaded_file is None:
    st.error("Please upload a carbon project document to proceed.")
