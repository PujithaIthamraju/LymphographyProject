# LymphographyProject 

# Lymphography Classification Using Machine Learning

## Description

This project is a **medical machine learning web application** that classifies lymphography data into diagnostic categories using a trained ML model.

It uses:

-  **Python + scikit-learn** for training a Decision Tree Classifier  
-   **Flask + React** to create an interactive user interface  
-  Manual patient inputs (18 features) to make real-time predictions

---

##  Purpose

To demonstrate how **machine learning** can assist in **medical diagnosis**, specifically for classifying lymph node conditions based on imaging and clinical features.

---

##  Features

- Trains a classification model using real lymphography data  
- Allows manual input of 18 medical parameters  
- Predicts the class:  
  - **Class 1:** Normal  
  - **Class 2:** Metastases  
  - **Class 3:** Malign lymph  
  - **Class 4:** Fibrosis  
- Easy-to-use web form (React)  
- Backend API using Flask 

---

##  Technologies Used

- Python  
- scikit-learn  
- pandas  
- joblib  
- Gradio / Flask  
- React (for frontend, if used)

---

##  Medical Features Used (Inputs)

- lymphatics  
- block_of_afferent_lymphatics  
- bl_of_lymph_c  
- bl_of_lymph_s  
- by_pass  
- extravasates  
- regeneration_of_ly  
- early_uptake_in_ly  
- lym_nodes_dimin  
- lym_nodes_enlar  
- changes_in_lym  
- defect_in_node  
- changes_in_node  
- changes_in_stru  
- special_forms  
- dislocation_of  
- exclusion_of_no  
- no_of_nodes_in  

---

##  Output

- Predicted classification label (1 to 4)
- Result shown in browser interface (React)

---


## Files

| File                  | Description                         |
|-----------------------|-------------------------------------|
| `app.py`              | Flask backend script                |
| `lymphography_model.joblib` | Saved ML model                |
| `App.tsx`             | React frontend                      |
| `requirements.txt`    | List of required Python libraries   |
| `README.md`           | Project description                 |

---
