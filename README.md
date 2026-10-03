🤖 AI-Based Software Quality Prediction

📌 Project Overview

AI-Based Software Quality Prediction is a software engineering project that predicts the quality of a software system based on different software metrics.

The system analyzes metrics such as Lines of Code, Number of Bugs, Cyclomatic Complexity, Test Coverage, and Code Duplication. Based on these values, the system provides a Quality Score, Quality Level, Risk Level, and improvement suggestions.

🎯 Objectives

- Predict software quality using software metrics.
- Identify possible quality risks at an early stage.
- Help developers understand software quality.
- Provide improvement suggestions.
- Display prediction results through an easy-to-use web interface.
- Maintain prediction history using a database in the extended version.

⚙️ Software Metrics Used

Metric| Description
LOC| Number of lines in the software
Bugs| Number of detected software bugs
Complexity| Cyclomatic complexity of the code
Test Coverage| Percentage of code covered by testing
Duplication| Percentage of duplicate code

🧠 Prediction

The system analyzes the given metrics and predicts:

- Quality Score
- Quality Level
- Risk Level
- Improvement Suggestions

Example

Input:
LOC             : 2500
Bugs            : 12
Complexity      : 11
Test Coverage   : 80%
Duplication     : 6%

Output:
Quality Score   : 70/100
Quality         : Medium Quality
Risk Level      : Moderate Risk

🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Joblib
- MySQL
- Machine Learning

📂 Project Structure

AI_Software_Quality_Prediction/
│
├── app.py
├── train_model.py
├── dataset.csv
├── requirements.txt
├── README.md
└── quality_model.pkl

🚀 How to Run

1. Clone the project

git clone <your-github-repository-url>

2. Open the project folder

cd AI_Software_Quality_Prediction

3. Install required libraries

pip install -r requirements.txt

4. Run the Streamlit application

python -m streamlit run app.py

5. Open the application

The application will open in the browser through the local Streamlit URL.

📊 Future Enhancements

- Implement a proper Machine Learning model.
- Add Random Forest / other ML algorithms.
- Add MySQL database integration.
- Add prediction history.
- Add interactive dashboard and graphs.
- Add user login.
- Generate downloadable software quality reports.
- Deploy the application online.

👨‍💻 Project Type

Mini Project – Software Engineering

📜 License

This project is developed for educational purposes.