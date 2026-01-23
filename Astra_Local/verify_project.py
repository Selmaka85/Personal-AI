#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 ASTRA Project Verification Script
Verifică: naming consistency, importuri, erori, case sensitivity, funcționalitate
"""

import sys
import os
import ast
import importlib.util
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
import re

# Setare encoding pentru Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_PATH = Path(__file__).parent
sys.path.insert(0, str(BASE_PATH))

class ProjectVerifier:
    """Verificător complet pentru proiectul ASTRA"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
        self.imports_checked = set()
        self.classes_found = {}
        self.functions_found = {}
        self.modules_found = {}
        
    def log_error(self, file: str, line: int, message: str):
        """Loghează o eroare"""
        self.errors.append(f"❌ {file}:{line} - {message}")
        
    def log_warning(self, file: str, line: int, message: str):
        """Loghează un warning"""
        self.warnings.append(f"⚠️ {file}:{line} - {message}")
        
    def log_info(self, message: str):
        """Loghează informație"""
        self.info.append(f"ℹ️ {message}")
        
    def check_file_syntax(self, file_path: Path) -> bool:
        """Verifică sintaxa unui fișier Python"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                source = f.read()
            ast.parse(source, filename=str(file_path))
            return True
        except SyntaxError as e:
            self.log_error(str(file_path), e.lineno or 0, f"Syntax error: {e.msg}")
            return False
        except Exception as e:
            self.log_error(str(file_path), 0, f"Error parsing: {e}")
            return False
    
    def check_naming_consistency(self, file_path: Path):
        """Verifică consistența numelor"""
        # Verifică dacă numele fișierului respectă convențiile
        name = file_path.stem
        
        # Verifică case sensitivity
        if name != name.lower() and not name.startswith('__'):
            # Permite excepții pentru clase (PascalCase)
            if not re.match(r'^[A-Z][a-zA-Z0-9]*$', name):
                self.log_warning(str(file_path), 0, 
                    f"Naming inconsistency: '{name}' - ar trebui să fie lowercase sau PascalCase")
        
        # Verifică dacă folosește underscore corect
        if '_' in name and not name.startswith('__'):
            # Verifică dacă are multiple underscore-uri consecutive
            if '__' in name and not name.startswith('__'):
                self.log_warning(str(file_path), 0, 
                    f"Multiple underscores in filename: '{name}'")
    
    def extract_imports(self, file_path: Path) -> List[Tuple[str, str, int]]:
        """Extrage toate importurile dintr-un fișier"""
        imports = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            for i, line in enumerate(lines, 1):
                # Verifică import statements
                if line.strip().startswith('import '):
                    module = line.strip().replace('import ', '').split(' as ')[0].strip()
                    imports.append(('import', module, i))
                elif line.strip().startswith('from '):
                    parts = line.strip().replace('from ', '').split(' import ')
                    if len(parts) == 2:
                        module = parts[0].strip()
                        imports.append(('from', module, i))
        except Exception as e:
            self.log_error(str(file_path), 0, f"Error extracting imports: {e}")
        
        return imports
    
    def check_imports(self, file_path: Path):
        """Verifică importurile"""
        imports = self.extract_imports(file_path)
        
        for import_type, module, line in imports:
            # Verifică dacă modulul există
            if module.startswith('.'):
                # Relative import
                continue
            
            # Verifică case sensitivity în importuri
            if module != module.lower() and not any(c.isupper() for c in module if c.isalpha()):
                # Verifică dacă este un modul standard
                if not self.is_standard_module(module):
                    self.log_warning(str(file_path), line, 
                        f"Case sensitivity in import: '{module}'")
            
            # Verifică importuri către modulele ASTRA
            if module.startswith('llm_modules') or module.startswith('astra_') or \
               module.startswith('core_router') or module.startswith('meta_layer') or \
               module.startswith('protection') or module.startswith('storage') or \
               module.startswith('api') or module.startswith('user_interface'):
                # Verifică dacă modulul există
                module_path = module.replace('.', '/')
                possible_paths = [
                    BASE_PATH / f"{module_path}.py",
                    BASE_PATH / f"{module_path}/__init__.py",
                ]
                
                if not any(p.exists() for p in possible_paths):
                    self.log_error(str(file_path), line, 
                        f"Import not found: '{module}'")
    
    def is_standard_module(self, module: str) -> bool:
        """Verifică dacă este un modul standard Python"""
        standard_modules = {
            'sys', 'os', 'json', 'pathlib', 'typing', 'datetime', 'time',
            'threading', 'abc', 're', 'difflib', 'sqlite3', 'pickle',
            'numpy', 'flask', 'subprocess', 'io', 'random'
        }
        return module.split('.')[0] in standard_modules
    
    def extract_classes_and_functions(self, file_path: Path):
        """Extrage clasele și funcțiile dintr-un fișier"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                source = f.read()
            
            tree = ast.parse(source, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_name = node.name
                    self.classes_found[class_name] = str(file_path)
                    
                    # Verifică naming convention pentru clase (PascalCase)
                    if not re.match(r'^[A-Z][a-zA-Z0-9]*$', class_name):
                        self.log_warning(str(file_path), node.lineno, 
                            f"Class naming: '{class_name}' - ar trebui să fie PascalCase")
                
                elif isinstance(node, ast.FunctionDef):
                    func_name = node.name
                    self.functions_found[func_name] = str(file_path)
                    
                    # Verifică naming convention pentru funcții (snake_case)
                    if not re.match(r'^[a-z_][a-z0-9_]*$', func_name):
                        # Permite excepții pentru metode speciale
                        if not func_name.startswith('__') or not func_name.endswith('__'):
                            self.log_warning(str(file_path), node.lineno, 
                                f"Function naming: '{func_name}' - ar trebui să fie snake_case")
        except Exception as e:
            self.log_error(str(file_path), 0, f"Error extracting classes/functions: {e}")
    
    def check_case_sensitivity_issues(self, file_path: Path):
        """Verifică probleme de case sensitivity"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verifică importuri cu case sensitivity
            import_pattern = r'(?:from|import)\s+([a-zA-Z_][a-zA-Z0-9_.]*)'
            matches = re.findall(import_pattern, content)
            
            for match in matches:
                # Verifică dacă modulul local există cu case diferit
                if match.startswith('Astrax2') or match.startswith('astrax2'):
                    # Verifică dacă fișierul există cu case diferit
                    possible_names = [
                        'Astrax2_Learning_Core',
                        'Astrax2_LLM_Engine',
                        'astrax2_learning_core',
                        'astrax2_llm_engine',
                    ]
                    # Log warning dacă există inconsistență
                    if 'Astrax2' in match and 'astrax2' in str(file_path).lower():
                        self.log_warning(str(file_path), 0, 
                            f"Case sensitivity issue: '{match}' vs filename")
        except Exception as e:
            self.log_error(str(file_path), 0, f"Error checking case sensitivity: {e}")
    
    def check_duplicate_names(self):
        """Verifică duplicate de nume"""
        # Verifică clase duplicate
        class_counts = {}
        for class_name, file_path in self.classes_found.items():
            if class_name not in class_counts:
                class_counts[class_name] = []
            class_counts[class_name].append(file_path)
        
        for class_name, files in class_counts.items():
            if len(files) > 1:
                self.log_warning(files[0], 0, 
                    f"Duplicate class name '{class_name}' in: {', '.join(files)}")
    
    def test_imports_functionality(self):
        """Testează dacă importurile funcționează"""
        critical_modules = [
            'nexus_efe_core_engine',
            'core_router.routing_manager',
            'scoring_module',
            'Astrax2_Learning_Core',
            'Astrax2_LLM_Engine',
            'llm_modules.mistral',
            'llm_modules.qwen',
            'llm_modules.deepseek',
            'meta_layer.meta_reflector',
            'meta_layer.coherence_validator',
        ]
        
        for module_name in critical_modules:
            try:
                # Încearcă să importe modulul
                if '.' in module_name:
                    parts = module_name.split('.')
                    mod = __import__(parts[0])
                    for part in parts[1:]:
                        mod = getattr(mod, part)
                else:
                    mod = __import__(module_name)
                self.log_info(f"✅ Import successful: {module_name}")
            except ImportError as e:
                self.log_error(module_name, 0, f"Import failed: {e}")
            except Exception as e:
                self.log_warning(module_name, 0, f"Import warning: {e}")
    
    def verify_file(self, file_path: Path):
        """Verifică un fișier complet"""
        if not file_path.exists():
            self.log_error(str(file_path), 0, "File does not exist")
            return
        
        # Verifică sintaxă
        if not self.check_file_syntax(file_path):
            return
        
        # Verifică naming
        self.check_naming_consistency(file_path)
        
        # Verifică importuri
        self.check_imports(file_path)
        
        # Verifică case sensitivity
        self.check_case_sensitivity_issues(file_path)
        
        # Extrage clase și funcții
        self.extract_classes_and_functions(file_path)
    
    def verify_project(self):
        """Verifică întregul proiect"""
        print("\n" + "="*70)
        print("🔍 ASTRA Project Verification - Verificare Completă")
        print("="*70 + "\n")
        
        # Găsește toate fișierele Python
        python_files = list(BASE_PATH.rglob("*.py"))
        
        print(f"📁 Găsite {len(python_files)} fișiere Python\n")
        
        # Verifică fiecare fișier
        for file_path in python_files:
            if file_path.name.startswith('verify_'):
                continue  # Skip verificatorul însuși
            self.verify_file(file_path)
        
        # Verifică duplicate
        self.check_duplicate_names()
        
        # Testează importuri
        print("\n" + "="*70)
        print("🧪 Testare Importuri Critice")
        print("="*70 + "\n")
        self.test_imports_functionality()
        
        # Afișează rezultate
        self.print_results()
    
    def print_results(self):
        """Afișează rezultatele"""
        print("\n" + "="*70)
        print("📊 REZULTATE VERIFICARE")
        print("="*70 + "\n")
        
        if self.errors:
            print(f"❌ ERORI ({len(self.errors)}):\n")
            for error in self.errors:
                print(f"  {error}")
            print()
        else:
            print("✅ Nu s-au găsit erori!\n")
        
        if self.warnings:
            print(f"⚠️ WARNING-URI ({len(self.warnings)}):\n")
            for warning in self.warnings[:20]:  # Limitează la primele 20
                print(f"  {warning}")
            if len(self.warnings) > 20:
                print(f"  ... și încă {len(self.warnings) - 20} warning-uri")
            print()
        else:
            print("✅ Nu s-au găsit warning-uri!\n")
        
        if self.info:
            print(f"ℹ️ INFO ({len(self.info)}):\n")
            for info in self.info[:10]:  # Limitează la primele 10
                print(f"  {info}")
            if len(self.info) > 10:
                print(f"  ... și încă {len(self.info) - 10} mesaje info")
            print()
        
        # Statistici
        print("="*70)
        print("📈 STATISTICI")
        print("="*70)
        print(f"  Fișiere verificate: {len(list(BASE_PATH.rglob('*.py')))}")
        print(f"  Clase găsite: {len(self.classes_found)}")
        print(f"  Funcții găsite: {len(self.functions_found)}")
        print(f"  Erori: {len(self.errors)}")
        print(f"  Warning-uri: {len(self.warnings)}")
        print()
        
        # Verdict final
        print("="*70)
        if len(self.errors) == 0:
            print("✅ PROIECT VERIFICAT - FĂRĂ ERORI CRITICE")
        elif len(self.errors) < 5:
            print("⚠️ PROIECT VERIFICAT - CU CÂTEVA ERORI MINORE")
        else:
            print("❌ PROIECT VERIFICAT - CU ERORI CARE TREBUIE REZOLVATE")
        print("="*70 + "\n")


def main():
    """Funcție principală"""
    verifier = ProjectVerifier()
    verifier.verify_project()


if __name__ == "__main__":
    main()
