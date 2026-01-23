# -*- coding: utf-8 -*-
"""
🔮 ML Predictor - Sistem de predicții folosind ML
"""

import os
import pickle
from pathlib import Path
from typing import Optional, Dict, Any, List
import numpy as np


class MLPredictor:
    """Predictor ML pentru diverse task-uri"""
    
    def __init__(self):
        self.models = {}
        self.models_path = Path("astra_ml_engine/model_weights")
        self.models_path.mkdir(parents=True, exist_ok=True)
        self.use_real_ml = self._check_ml_available()
    
    def _check_ml_available(self) -> bool:
        """Verifică dacă bibliotecile ML sunt disponibile"""
        try:
            import sklearn
            import xgboost
            return True
        except ImportError:
            return False
    
    def load_model(self, model_name: str, model_type: str = "xgboost"):
        """Încarcă un model ML"""
        if not self.use_real_ml:
            print("⚠️ sklearn/xgboost nu sunt instalate. Instalează cu: pip install scikit-learn xgboost")
            return None
        
        model_path = self.models_path / f"{model_name}.pkl"
        
        if model_path.exists():
            try:
                with open(model_path, 'rb') as f:
                    self.models[model_name] = pickle.load(f)
                print(f"✅ Model {model_name} încărcat")
                return self.models[model_name]
            except Exception as e:
                print(f"⚠️ Eroare la încărcare model {model_name}: {e}")
        else:
            print(f"⚠️ Model {model_name} nu există la {model_path}")
        
        return None
    
    def train_model(self, model_name: str, X: np.ndarray, y: np.ndarray, 
                   model_type: str = "xgboost"):
        """Antrenează un model ML"""
        if not self.use_real_ml:
            print("[ML Mock] Ar antrena model...")
            return None
        
        try:
            if model_type == "xgboost":
                import xgboost as xgb
                model = xgb.XGBRegressor() if len(np.unique(y)) > 10 else xgb.XGBClassifier()
            elif model_type == "random_forest":
                from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
                model = RandomForestRegressor() if len(np.unique(y)) > 10 else RandomForestClassifier()
            else:
                from sklearn.linear_model import LinearRegression, LogisticRegression
                model = LinearRegression() if len(np.unique(y)) > 10 else LogisticRegression()
            
            model.fit(X, y)
            
            # Salvează modelul
            model_path = self.models_path / f"{model_name}.pkl"
            with open(model_path, 'wb') as f:
                pickle.dump(model, f)
            
            self.models[model_name] = model
            print(f"✅ Model {model_name} antrenat și salvat")
            return model
        except Exception as e:
            print(f"⚠️ Eroare la antrenare model: {e}")
            return None
    
    def predict(self, model_name: str, X: np.ndarray) -> Optional[np.ndarray]:
        """Face predicții folosind un model"""
        if model_name not in self.models:
            self.load_model(model_name)
        
        if model_name in self.models:
            try:
                predictions = self.models[model_name].predict(X)
                return predictions
            except Exception as e:
                print(f"⚠️ Eroare la predicție: {e}")
        
        return None
