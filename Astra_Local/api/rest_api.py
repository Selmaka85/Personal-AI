# -*- coding: utf-8 -*-
"""
🔌 REST API pentru ASTRA - API endpoints pentru integrare externă
"""

try:
    from flask import Flask, request, jsonify
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False

import sys
from pathlib import Path

BASE_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_PATH))


if FLASK_AVAILABLE:
    app = Flask(__name__)
    
    @app.route('/api/v1/chat', methods=['POST'])
    def api_chat():
        """Endpoint pentru chat"""
        try:
            from nexus_efe_core_engine import NexusEFE
            from llm_modules.mistral import MistralLLM
            from llm_modules.qwen import QwenLLM
            
            data = request.json
            message = data.get('message', '')
            user_id = data.get('user_id', 'api_user')
            
            llm_pool = {
                "mistral": MistralLLM(),
                "qwen": QwenLLM(),
                "default": MistralLLM()
            }
            
            config = {"thresholds": {"accept": 0.75}}
            efe = NexusEFE(config, llm_pool)
            response = efe.process(message, user_id=user_id)
            
            return jsonify({
                'success': True,
                'response': response,
                'user_id': user_id
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/v1/status', methods=['GET'])
    def api_status():
        """Endpoint pentru status"""
        return jsonify({
            'status': 'online',
            'version': '1.0.0',
            'components': {
                'routing': True,
                'scoring': True,
                'efe_engine': True,
                'learning': True
            }
        })
    
    @app.route('/api/v1/models', methods=['GET'])
    def api_models():
        """Endpoint pentru lista modele"""
        return jsonify({
            'models': [
                'mistral',
                'qwen',
                'deepseek',
                'wizardcoder',
                'codestral',
                'mythomax',
                'mixtral',
                'gpt4all'
            ]
        })
    
    def run(host='127.0.0.1', port=8000):
        """Pornește API server"""
        print(f"\nASTRA REST API - http://{host}:{port}")
        app.run(host=host, port=port, debug=False)
