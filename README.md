# Simulation

# Thyroid Function Simulation

This project is an interactive tool to simulate and explore how changes in thyroid-related lab test results correlate with potential dysfunctions and symptoms. While currently designed for thyroid function tests, the framework can be expanded to include other medical tests for different organs or systems.

## Overview
The simulation allows users to:
- Input test results for TSH, Free T4, Free T3, and thyroid-related antibodies (TPO and Thyroglobulin).
- Tinker with the values to observe how abnormalities in these tests connect to specific thyroid dysfunctions or related symptoms like hair loss and brain fog.
- Understand potential root causes, including regulatory systems such as the pituitary gland, hypothalamus, liver, or immune system.

The tool provides:
1. **Dynamic insights** based on user input.
2. **Symptom mapping** tied to lab abnormalities.
3. **Recommendations** for further evaluation or management strategies.

## Key Features
- Interactive sliders for lab test values:
  - TSH (Thyroid-Stimulating Hormone)
  - Free T4 (Thyroxine)
  - Free T3 (Triiodothyronine)
  - TPO Antibodies
  - Thyroglobulin Antibodies
- Real-time analysis of thyroid health.
- Decision-tree-like logic to connect test results to symptoms and potential causes.
- Expandable design for future tests and systems.

## Future Expansion
This simulation is designed to grow and include tests for other organs or systems, such as:
- **Liver Function Tests** (ALT, AST, Bilirubin, etc.)
- **Adrenal Function Tests** (Cortisol, ACTH)
- **Kidney Function Tests** (eGFR, Creatinine, BUN)
- **Nutritional Deficiencies** (Iron, Selenium, Vitamin D, etc.)

The goal is to build a comprehensive decision-making roadmap that links test results to the root cause of dysfunctions, helping users understand complex relationships in the body.

## Requirements
- **Python 3.7+**
- **Streamlit**

Install Streamlit using pip:
```bash
pip install streamlit
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ThyroidSimulation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ThyroidSimulation
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run thyroid_simulation.py
   ```
4. Open the app in your browser using the link provided by Streamlit.

## Usage Instructions
1. Input your lab test results using the sliders.
2. Observe the real-time analysis and insights in the "Analysis" section.
3. Explore potential root causes in the "Symptom Mapping" section.
4. Review recommendations for next steps based on the input.

## Example Use Case
- A user inputs low TSH and high Free T4 levels. The simulation identifies potential hyperthyroidism and suggests further evaluation of TPO antibodies to check for autoimmune causes.
- If Free T3 is low, the app suggests evaluating selenium levels and liver function for impaired T4 to T3 conversion.

## Contributing
This project is open to contributions! If you'd like to add new tests or features:
1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License.

## Contact
For questions or suggestions, feel free to reach out:
- **Author**: Zain Khan

