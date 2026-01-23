# 🚀 ASTRA - Quick Installation Guide

## For Recruiters & Technical Reviewers

This guide provides a simple way to set up and run the ASTRA project for evaluation.

---

## 📋 Prerequisites

- **Python 3.8+** (Python 3.9+ recommended)
- **pip** (Python package manager)
- **Git** (optional, for cloning repository)
- **8GB+ RAM** (for running models)
- **Windows/Linux/Mac** (cross-platform compatible)

---

## ⚡ Quick Start (5 minutes)

### Step 1: Navigate to Project
```bash
cd Astra_Local
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run Setup
```bash
python setup.py
```

### Step 4: Test Installation
```bash
python test_functionality_complete.py
```

### Step 5: Run ASTRA
```bash
python astra_entrypoint.py
```

---

## 📦 What Gets Installed

### Core Dependencies:
- **Standard Libraries**: json, pathlib, typing, datetime, etc.
- **ML Libraries**: numpy (for ML models)
- **Optional**: flask (for web UI), transformers (for real LLM models)

### Note:
- The project works with **mock LLM models** by default (no external APIs needed)
- For real LLM models, additional setup is required (see `INSTALL_GUIDE.md`)

---

## ✅ Verification

After installation, you should see:
```
✅ TOATE TESTELE AU TRECUT!
✅ Teste trecute: 35
❌ Teste eșuate: 0
📈 Rata de succes: 100.0%
```

---

## 🎯 Running the System

### Interactive Mode:
```bash
python astra_entrypoint.py
```

### Demo Mode:
```bash
python demo_final.py
```

### Test Mode:
```bash
python test_complet.py
```

---

## 🔧 Troubleshooting

### Issue: Import errors
**Solution**: Make sure you're in the `Astra_Local` directory
```bash
cd Astra_Local
python -c "import sys; print(sys.path)"
```

### Issue: Missing dependencies
**Solution**: Reinstall requirements
```bash
pip install -r requirements.txt --upgrade
```

### Issue: Python version
**Solution**: Check Python version
```bash
python --version  # Should be 3.8+
```

---

## 📊 System Requirements

### Minimum:
- **RAM**: 4GB
- **Storage**: 500MB
- **Python**: 3.8+

### Recommended:
- **RAM**: 8GB+
- **Storage**: 2GB+
- **Python**: 3.9+

### For Real LLM Models:
- **RAM**: 16GB+ (for larger models)
- **GPU**: Optional but recommended
- **Storage**: 10GB+ (for model files)

---

## 🎓 For Technical Interviews

### What to Show:
1. **Code Structure**: Walk through the modular architecture
2. **Key Features**: Demonstrate routing, scoring, learning
3. **Testing**: Show test results and coverage
4. **Documentation**: Point to comprehensive docs

### Key Files to Review:
- `core_router/routing_manager.py` - Intelligent routing
- `scoring_module.py` - Multi-criteria scoring
- `nexus_efe_core_engine.py` - EFE pipeline
- `test_functionality_complete.py` - Test suite

---

## 📞 Support

For questions or issues:
- Check `INSTALL_GUIDE.md` for detailed instructions
- Review `README.md` for project overview
- See `VERIFICATION_REPORT_FINAL.md` for verification results

---

**The system is designed to work out-of-the-box with mock models for easy evaluation.**
