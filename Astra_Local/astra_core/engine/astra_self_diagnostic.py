# -*- coding: utf-8 -*-
"""
🔍 Astra Self Diagnostic - Sistem de auto-diagnosticare
"""

import os
from pathlib import Path
from typing import Dict, Any


class AstraSelfDiagnostic:
    """Sistem de auto-diagnosticare pentru Astra"""
    
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent
        self.critical_files = [
            "astra_entrypoint.py",
            "core_router/routing_manager.py",
            "scoring_module.py",
            "nexus_efe_core_engine.py"
        ]
    
    def run_check(self) -> Dict[str, Any]:
        """
        Rulează verificarea completă a sistemului
        """
        results = {
            "critical_ok": True,
            "files_check": {},
            "directories_check": {},
            "modules_check": {}
        }
        
        # Verificare fișiere critice
        for file in self.critical_files:
            file_path = self.base_path / file
            exists = file_path.exists()
            results["files_check"][file] = exists
            
            if not exists and file in self.critical_files[:2]:  # Primele 2 sunt critice
                results["critical_ok"] = False
        
        # Verificare directoare
        critical_dirs = [
            "llm_modules",
            "core_router",
            "meta_layer",
            "storage"
        ]
        
        for dir_name in critical_dirs:
            dir_path = self.base_path / dir_name
            exists = dir_path.exists() and dir_path.is_dir()
            results["directories_check"][dir_name] = exists
            
            if not exists:
                results["critical_ok"] = False
        
        # Verificare module Python
        try:
            import sys
            sys.path.insert(0, str(self.base_path))
            
            # Test import-uri critice
            from core_router.routing_manager import RoutingManager
            from scoring_module import ScoringModule
            from nexus_efe_core_engine import NexusEFE
            
            results["modules_check"]["routing_manager"] = True
            results["modules_check"]["scoring_module"] = True
            results["modules_check"]["nexus_efe"] = True
            
        except ImportError as e:
            results["modules_check"]["error"] = str(e)
            results["critical_ok"] = False
        
        return results
