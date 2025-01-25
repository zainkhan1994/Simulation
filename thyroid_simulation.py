import streamlit as st

# Title of the simulation
st.title("Thyroid Function Simulation")

# Description of the tool
st.write("This interactive simulation helps you explore how changes in thyroid-related lab test results could correlate with potential dysfunctions and symptoms.")

# Input fields for lab test results
tsh = st.slider("TSH (mIU/L)", min_value=0.0, max_value=10.0, value=2.5, step=0.1)
free_t4 = st.slider("Free T4 (ng/dL)", min_value=0.5, max_value=2.5, value=1.2, step=0.1)
free_t3 = st.slider("Free T3 (pg/mL)", min_value=2.0, max_value=6.0, value=3.5, step=0.1)
anti_tpo = st.slider("TPO Antibodies (IU/mL)", min_value=0, max_value=500, value=25, step=5)
anti_tg = st.slider("Thyroglobulin Antibodies (IU/mL)", min_value=0, max_value=500, value=20, step=5)

# Analyze results and provide potential insights
st.subheader("Analysis")

if tsh < 0.5:
    st.write("**Low TSH:** This may indicate hyperthyroidism (overactive thyroid). Consider checking Free T4 and Free T3 for confirmation.")
elif tsh > 5.0:
    st.write("**High TSH:** This may indicate hypothyroidism (underactive thyroid). Evaluate Free T4 and Free T3 to confirm.")
else:
    st.write("**Normal TSH:** Thyroid function appears normal based on TSH levels.")

if free_t4 < 0.8:
    st.write("**Low Free T4:** This suggests underactive thyroid or central hypothyroidism (pituitary/hypothalamus issue).")
elif free_t4 > 2.0:
    st.write("**High Free T4:** This is consistent with hyperthyroidism.")
else:
    st.write("**Normal Free T4:** No abnormalities detected in Free T4 levels.")

if free_t3 < 2.3:
    st.write("**Low Free T3:** This may indicate poor conversion of T4 to T3 (e.g., due to liver issues or selenium deficiency).")
elif free_t3 > 4.2:
    st.write("**High Free T3:** Often seen in hyperthyroidism.")
else:
    st.write("**Normal Free T3:** Free T3 levels are within the expected range.")

if anti_tpo > 35:
    st.write("**High TPO Antibodies:** This is indicative of Hashimoto's Thyroiditis or another autoimmune thyroid condition.")
else:
    st.write("**Normal TPO Antibodies:** No evidence of autoimmune thyroid disease based on TPO antibodies.")

if anti_tg > 40:
    st.write("**High Thyroglobulin Antibodies:** This may indicate Hashimoto's or another autoimmune condition affecting the thyroid.")
else:
    st.write("**Normal Thyroglobulin Antibodies:** No evidence of autoimmune thyroid disease based on thyroglobulin antibodies.")

# Symptom mapping and recommendations
st.subheader("Symptom Mapping")

st.write("Based on your inputs, here are potential causes for symptoms like hair loss and brain fog:")
if tsh > 5.0 or free_t4 < 0.8:
    st.write("- Hypothyroidism: Common symptoms include hair loss, brain fog, and fatigue.")
if free_t3 < 2.3:
    st.write("- Poor T4 to T3 conversion: Consider evaluating liver function and selenium levels.")
if anti_tpo > 35 or anti_tg > 40:
    st.write("- Autoimmune thyroid disease: Symptoms may include inflammation and gradual thyroid dysfunction.")

st.write("### Recommendations")
if tsh > 5.0 or free_t4 < 0.8:
    st.write("- Discuss potential hypothyroidism with your provider and consider further testing.")
if anti_tpo > 35 or anti_tg > 40:
    st.write("- Autoimmune-focused interventions (e.g., anti-inflammatory diet, stress management).")
if free_t3 < 2.3:
    st.write("- Assess selenium and liver health to improve T4 to T3 conversion.")
