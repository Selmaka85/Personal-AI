# -*- coding: utf-8 -*-
"""
💾 Database Integration - Integrare bază de date pentru ASTRA
"""

import sqlite3
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional


class AstraDatabase:
    """Bază de date pentru ASTRA"""
    
    def __init__(self, db_path: str = "storage/astra.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = None
        self._init_database()
    
    def _init_database(self):
        """Inițializează baza de date"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        
        # Creează tabele
        cursor = self.conn.cursor()
        
        # Tabel conversații
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                timestamp TEXT,
                input_text TEXT,
                output_text TEXT,
                model_used TEXT,
                scores TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Tabel memorie
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE,
                value TEXT,
                category TEXT,
                importance REAL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Tabel învățare
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS learning (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT,
                model_used TEXT,
                scores TEXT,
                success BOOLEAN,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.conn.commit()
    
    def save_conversation(self, user_id: str, input_text: str, output_text: str,
                         model_used: str, scores: Dict[str, Any]):
        """Salvează o conversație"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO conversations (user_id, timestamp, input_text, output_text, model_used, scores)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            datetime.now().isoformat(),
            input_text,
            output_text,
            model_used,
            json.dumps(scores)
        ))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_conversations(self, user_id: Optional[str] = None, limit: int = 100) -> List[Dict[str, Any]]:
        """Obține conversații"""
        cursor = self.conn.cursor()
        
        if user_id:
            cursor.execute("""
                SELECT * FROM conversations 
                WHERE user_id = ? 
                ORDER BY created_at DESC 
                LIMIT ?
            """, (user_id, limit))
        else:
            cursor.execute("""
                SELECT * FROM conversations 
                ORDER BY created_at DESC 
                LIMIT ?
            """, (limit,))
        
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    
    def save_memory(self, key: str, value: Any, category: str = "general", importance: float = 0.5):
        """Salvează în memorie"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO memory (key, value, category, importance, updated_at)
            VALUES (?, ?, ?, ?, ?)
        """, (
            key,
            json.dumps(value),
            category,
            importance,
            datetime.now().isoformat()
        ))
        self.conn.commit()
    
    def get_memory(self, key: str) -> Optional[Any]:
        """Obține din memorie"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT value FROM memory WHERE key = ?", (key,))
        row = cursor.fetchone()
        if row:
            return json.loads(row['value'])
        return None
    
    def close(self):
        """Închide conexiunea"""
        if self.conn:
            self.conn.close()


# Instanță globală
database = AstraDatabase()
