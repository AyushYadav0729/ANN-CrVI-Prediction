# ANN Model for Cr(VI) Removal Prediction

## Overview
This project develops an Artificial Neural Network (ANN) to predict chromium (Cr(VI)) removal efficiency using adsorption data.

## Features
- Input: Time, Concentration, pH, Dosage, Temperature, Adsorbent
- Output: Removal Efficiency (%)
- Model: ANN (128-64-32 architecture)
- Techniques: L2 Regularization, Dropout, MAE Loss

## Results
- Mean R² = 0.8849  (≈ 0.885)
- Standard Deviation : 0.0082
- Min = 0.8694  
- Max = 0.8984

## Files
- Folder -> Train_info
  contains the traning info of the model training along with the dataset used to train the model
- Folder -> static
  contains style.css for the local webpage
- Folder -> templates
  contains html webpage for the prediction.
  
- Main
  ```bash
  ann_removal_model_v3.keras
  preprocessor_v3.pkl
  y_scaler_v3.pkl
  ```
  -saved model files

  ```bash
  train_ann_v3.py
  ```
  -ANN Model code
  
  ```bash
  predict_ann_v3.py
  app.py
  ```
  -Predict Files
  
## Requirements

Install these libraries before running the scripts:
```bash
pip install pandas numpy matplotlib tensorflow scikit-learn joblib openpyxl
```

