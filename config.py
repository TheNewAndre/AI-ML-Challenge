# config.py
# ============================================================
# Centralized configuration for the Lithology Prediction project.
# Update the paths below to match your local directory structure.
# ============================================================

# ==============================
# DATA PATHS
# ==============================
TRAIN_PATH  = r"path/to/your/Train_dataset_folder"   # Folder containing per-well CSV files
TEST_PATH   = r"path/to/your/Test_dataset.csv"        # Single CSV test file
OUTPUT_PATH = r"path/to/your/lithology_predictions.csv"  # Where predictions will be saved

# ==============================
# LITHOLOGY MAPPING
# ==============================
LITHOLOGY_MAPPING = {
    30000: "Sandstone",
    65030: "Sandstone/Shale",
    65000: "Shale",
    80000: "Marl",
    74000: "Dolomite",
    70000: "Limestone",
    70032: "Chalk",
    88000: "Halite",
    86000: "Anhydrite",
    99000: "Tuff",
    90000: "Coal",
    93000: "Basement",
}

# ==============================
# COLUMNS TO EXCLUDE FROM FEATURES
# ==============================
LOCATION_COLUMNS = ["X_LOC", "Y_LOC", "Z_LOC", "DEPT", "DEPTH_MD"]

EXCLUDED_COLUMNS = [
    "file_name", "well_name", "Lithology_code", "Lithology_Label",
    "filename", "ROPA", "BS", "SGR", "RXO", "RMIC", "DTS",
] + LOCATION_COLUMNS

# ==============================
# MODEL HYPERPARAMETERS
# ==============================
LGBM_PARAMS = {
    "n_estimators": 850,
    "learning_rate": 0.05,
    "max_depth": 8,
    "reg_lambda": 5,
    "min_child_samples": 50,
    "random_state": 42,
    "objective": "multiclass",
    "class_weight": "balanced",
    "verbose": -1,
}

# ==============================
# CROSS-VALIDATION SETTINGS
# ==============================
CV_N_SPLITS   = 5
CV_SHUFFLE    = True
CV_RANDOM_STATE = 42

# ==============================
# TRAIN/VALIDATION SPLIT
# ==============================
TEST_SIZE    = 0.2
RANDOM_STATE = 42
