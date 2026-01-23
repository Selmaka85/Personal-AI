# -*- coding: utf-8 -*-
"""
💓 Astra Heartbeat - Pulsul intern al sistemului
"""

import time
import threading
from datetime import datetime
from pathlib import Path


class AstraHeartbeat:
    """Sistem de heartbeat pentru monitorizare"""
    
    def __init__(self, interval: int = 30):
        self.interval = interval  # secunde
        self.is_running = False
        self.heartbeat_log = Path("storage/logs/heartbeat.log")
        self.heartbeat_log.parent.mkdir(parents=True, exist_ok=True)
    
    def start(self):
        """Pornește heartbeat-ul"""
        self.is_running = True
        
        while self.is_running:
            try:
                self._beat()
                time.sleep(self.interval)
            except Exception as e:
                print(f"⚠️ Eroare heartbeat: {e}")
                time.sleep(self.interval)
    
    def _beat(self):
        """Execută un beat"""
        timestamp = datetime.now().isoformat()
        beat_data = {
            "timestamp": timestamp,
            "status": "alive",
            "interval": self.interval
        }
        
        try:
            with open(self.heartbeat_log, 'a', encoding='utf-8') as f:
                f.write(f"{timestamp} - Heartbeat OK\n")
        except Exception:
            pass  # Nu bloca dacă log-ul nu funcționează
    
    def stop(self):
        """Oprește heartbeat-ul"""
        self.is_running = False
