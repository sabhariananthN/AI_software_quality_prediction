import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Software Quality Prediction",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI-Based Software Quality Prediction")
st.write("Predict the quality of your software using software metrics.")

st.divider()

# Input section
st.subheader("📊 Enter Software Metrics")

col1, col2 = st.columns(2)

with col1:
    loc = st.number_input(
        "Lines of Code (LOC)",
        min_value=100,
        max_value=100000,
        value=2500
    )

    bugs = st.number_input(
        "Number of Bugs",
        min_value=0,
        max_value=1000,
        value=10
    )

    complexity = st.number_input(
        "Cyclomatic Complexity",
        min_value=1,
        max_value=100,
        value=10
    )

with col2:
    coverage = st.slider(
        "Test Coverage (%)",
        min_value=0,
        max_value=100,
        value=80
    )

    duplication = st.slider(
        "Code Duplication (%)",
        min_value=0,
        max_value=100,
        value=5
    )


# Prediction function
def predict_quality(bugs, complexity, coverage, duplication):

    score = 100

    score -= bugs * 1.2
    score -= complexity * 1.5
    score += (coverage - 70) * 0.5
    score -= duplication * 1.0

    score = max(0, min(100, score))

    if score >= 75:
        quality = "High Quality"
        risk = "Low Risk"

    elif score >= 50:
        quality = "Medium Quality"
        risk = "Moderate Risk"

    else:
        quality = "Low Quality"
        risk = "High Risk"

    return round(score, 2), quality, risk


# Prediction button
if st.button("🔍 Predict Software Quality"):

    score, quality, risk = predict_quality(
        bugs,
        complexity,
        coverage,
        duplication
    )

    st.divider()

    st.subheader("📋 Prediction Result")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Quality Score", f"{score}/100")

    with col2:
        st.metric("Quality", quality)

    with col3:
        st.metric("Risk Level", risk)

    st.success("Prediction completed successfully!")

    # Suggestions
    st.subheader("💡 Improvement Suggestions")

    if bugs > 20:
        st.warning("Reduce the number of software bugs.")

    if complexity > 15:
        st.warning("Reduce code complexity.")

    if coverage < 70:
        st.warning("Increase test coverage.")

    if duplication > 10:
        st.warning("Reduce duplicate code.")

    if bugs <= 20 and complexity <= 15 and coverage >= 70 and duplication <= 10:
        st.info("Software metrics are within a good range.")