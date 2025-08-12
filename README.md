Wine Classification with ANN (Streamlit Deployment)
markdown
Copy
Edit
# 🍷 Wine Quality Classification with ANN (Streamlit Deployment)

This project uses an **Artificial Neural Network (ANN)** to classify wine quality based on physicochemical features from a wine dataset.  
The trained model is deployed using **Streamlit** to provide an interactive web interface for predictions.

---

## 📂 Dataset

The dataset contains various physicochemical properties of wine samples, such as:
- Fixed acidity
- Volatile acidity
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- Alcohol content
- Quality (target variable)

**Dataset source:** [Wine Quality Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality)

---

## 🛠️ Technologies Used
- **Python 3.x**
- **TensorFlow / Keras**
- **NumPy** & **Pandas**
- **Matplotlib** & **Seaborn** (for visualization)
- **Streamlit** (for deployment)
- **scikit-learn** (for preprocessing & evaluation)

---

## 📜 Project Structure

├── wine_ann.py # ANN model training & evaluation
├── app.py # Streamlit web app for predictions
├── wine.csv # Dataset file
├── requirements.txt # Required dependencies
├── README.md # Project documentation
└── saved_model/ # Directory to save trained model
---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/wine-quality-ann.git
cd wine-quality-ann
Create a virtual environment

python -m venv venv
venv\Scripts\activate        # Windows
Install dependencies

pip install -r requirements.txt
🏗️ Model Training
Run the training script:

python wine_ann.py
The trained model will be saved in the saved_model/ directory.

🚀 Running the Streamlit App
Start the web app:

streamlit run app.py
The app will open in your default browser at:
http://localhost:8501
🌐 Streamlit Web App Features
User Input Form for wine physicochemical properties

Instant Predictions of wine quality class

Probability Confidence for each predicted class

Visualizations (optional: feature importance, dataset insights)

📊 ANN Model Architecture
Input Layer: 11 features

Hidden Layer 1: Dense + ReLU activation

Hidden Layer 2: Dense + ReLU activation

Output Layer: Softmax activation for multi-class classification

Example:
model = Sequential([
    Dense(64, activation='relu', input_shape=(11,)),
    Dense(32, activation='relu'),
    Dense(6, activation='softmax')  # 6 wine quality classes
])
📈 Results
Loss Function: categorical_crossentropy

Optimizer: Adam

Accuracy: ~80–85% on validation data

🧠 Key Learnings
ANN models work well with tabular classification problems after proper scaling.

Streamlit simplifies deployment for interactive ML apps.

Input feature scaling significantly impacts ANN performance.

📜 License
This project is licensed under the MIT License.

✨ Author
David Ndiritu Mwaniki
📧 davidndiritu2000@gmail.com
