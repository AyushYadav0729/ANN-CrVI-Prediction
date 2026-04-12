# ANN-Based Cr(VI) Removal Efficiency Predictor

## Overview
This project develops an Artificial Neural Network (ANN) model to predict the percentage removal efficiency of Chromium (Cr(VI)) from aqueous solutions using adsorption data collected from research papers.

The model takes key adsorption parameters as input and provides real-time predictions through a Flask-based web application.

---

## Features
- Predicts Cr(VI) removal efficiency (%)
- Uses trained ANN model with optimized performance (R² ≈ 0.89)
- Cleaned and refined dataset (conflict removal applied)
- Interactive web interface for real-time predictions
- Complete ML pipeline (preprocessing → training → inference)

---

## Project Structure
```
.
├── Train_info/
│   ├── ANN_Predictions_v3.xlsx
│   ├── ANN_Test_Metrics_v3.xlsx
│   ├── actual_vs_predicted_v3.png
│   ├── error_histogram_v3.png
│   ├── final_cleaned_dataset_v3.csv
│   ├── loss_curve_v3.png
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── ann_removal_model_v3.keras
├── app.py
├── predict_ann_v3.py
├── preprocessor_v3.pkl
├── train_ann_v3.py
├── y_scaler_v3.pkl
├── README.md
```

---

## Model Details

**Input Features:**
- Adsorbent (categorical)
- Time (minutes)
- Initial Concentration (mg/L)
- pH
- Dosage (g/L)
- Temperature (°C)

**Output:**
- Removal Efficiency (%)

**Architecture:**
- Dense(128) → Dense(64) → Dense(32) → Output
- Activation: ReLU
- Optimizer: Adam
- Learning Rate: 0.00085

---

## Dataset
- Collected from multiple research papers
- Cleaned and standardized
- Conflicting samples removed (key improvement step)
- Final dataset: balanced and physically consistent

---

## Results
- Average R²: ~0.885
- Best R²: ~0.898
- Improved performance after dataset refinement
- Stable training with minimal overfitting

Evaluation plots included:
- Actual vs Predicted
- Error Histogram
- Training vs Validation Loss

---

## Web Application

The project includes a Flask-based web interface.

### How it works:
1. Select adsorbent from dropdown  
2. Enter input parameters  
3. Click Predict  
4. Model returns removal efficiency (%)  

### Run the web app:
```bash
python app.py
```

Then open in browser:
http://127.0.0.1:5000/

---

## How to Use

### Install dependencies
```bash
pip install -r requirements.txt
```

### Launch web app
```bash
python app.py
```

---

## Important Files
- ann_removal_model_v3.keras → trained ANN model  
- preprocessor_v3.pkl → input preprocessing pipeline  
- y_scaler_v3.pkl → output scaler  
- app.py → Flask app  
- train_ann_v3.py → training script  
- predict_ann_v3.py → if want prediction in terminal 

---

## Key Contribution
- Identification and removal of conflicting data samples  
- Demonstrated that data quality > model complexity  
- End-to-end ML pipeline with deployment  

---

## Future Work
- Include additional features (surface area, synthesis method)  
- Expand dataset with more adsorbents  
- Improve generalization for multi-modal behavior  

---

## Author
**Ayush Yadav**  
B.Tech CSE (Data Science)

---

## License
This project is for academic and research purposes.
