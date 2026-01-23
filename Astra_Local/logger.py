# -*- coding: utf-8 -*-
"""
📝 Logger - Sistem de logging pentru ASTRA
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional


class Logger:
    """Sistem de logging pentru ASTRA"""
    
    def __init__(self, log_dir: str = "storage/logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        self.main_log = self.log_dir / "astra_main.log"
        self.security_log = self.log_dir / "security_events.log"
        self.learning_log = self.log_dir / "learning_history.json"
    
    def save_logs(self, input_data: str, output: str, score: Dict[str, Any]):
        """
        Salvează log-uri principale
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "input": input_data[:200],  # Limitează lungimea
            "output": output[:500],
            "score": score
        }
        
        try:
            with open(self.main_log, 'a', encoding='utf-8') as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"⚠️ Eroare la salvare log: {e}")
    
    def monitor_usage(self):
        """
        Monitorizează utilizarea sistemului
        """
        # Placeholder pentru monitorizare avansată
        pass
    
    def flag_anomalies(self, anomaly_type: str, details: str):
        """
        Marchează anomalii în log-ul de securitate
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "type": anomaly_type,
            "details": details
        }
        
        try:
            with open(self.security_log, 'a', encoding='utf-8') as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"⚠️ Eroare la log securitate: {e}")
