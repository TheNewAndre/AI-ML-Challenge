# 🪨 Lithology Prediction using LightGBM

A machine learning pipeline to predict subsurface **lithology** (rock types) from well log data using **LightGBM** with cross-validation and feature engineering.

---

## 📌 Project Overview

This project classifies 12 lithology types from petrophysical well log measurements. It was built for the **SCALE-UP Elimination Round** challenge.

**Predicted Lithology Classes:**

| Code  | Lithology         |
|-------|-------------------|
| 30000 | Sandstone         |
| 65030 | Sandstone/Shale   |
| 65000 | Shale             |
| 80000 | Marl              |
| 74000 | Dolomite          |
| 70000 | Limestone         |
| 70032 | Chalk             |
| 88000 | Halite            |
| 86000 | Anhydrite         |
| 99000 | Tuff              |
| 90000 | Coal              |
| 93000 | Basement          |

---

## 📂 Project Structure

```
├── Final_code.ipynb          # Main notebook: EDA, feature engineering, training
├── config.py                 # Path and model configuration
├── requirements.txt          # Python dependencies
├── .gitignore                # Files and folders excluded from Git
└── README.md                 # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Configure your paths
Open `config.py` and update the dataset paths to match your local setup:

```python
TRAIN_PATH = "path/to/your/train_dataset_folder"
TEST_PATH  = "path/to/your/Test_dataset.csv"
OUTPUT_PATH = "path/to/your/output_predictions.csv"
```

### 2. Run the notebook
```bash
jupyter notebook Final_code.ipynb
```

Run all cells from top to bottom. The notebook will:
- Load and preprocess well log data from multiple CSV files
- Engineer petrophysical features (e.g., shale volume `VSH_GR`)
- Train a LightGBM classifier using **5-Fold Stratified Cross-Validation**
- Output a classification report and feature importance plot
- Generate predictions on the test set

---

## 🧠 Model Details

| Parameter           | Value              |
|---------------------|--------------------|
| Model               | LGBMClassifier     |
| n_estimators        | 850                |
| learning_rate       | 0.05               |
| max_depth           | 8                  |
| reg_lambda          | 5                  |
| min_child_samples   | 50                 |
| class_weight        | balanced           |
| CV Strategy         | StratifiedKFold (5)|
| Metric              | F1-Score (macro)   |

---

## 📊 Feature Engineering

Key engineered features include:

- **VSH_GR** – Per-well normalized shale volume from Gamma Ray log
- Location columns (`X_LOC`, `Y_LOC`, `Z_LOC`, `DEPT`, `DEPTH_MD`) are **excluded** to avoid spatial data leakage

---

## 📈 Output

- `LGBM_8_800_lithology_predictions.csv` — Final lithology predictions on the test set
- `LGBM_8_800_lithology_feature_importance.png` — Feature importance bar chart

---

## 📦 Dependencies

See [`requirements.txt`](requirements.txt) for the full list.

---

## 🙌 Acknowledgements

Built for the **SCALE-UP Elimination Round** data science competition.
