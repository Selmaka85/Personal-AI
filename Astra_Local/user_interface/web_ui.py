# -*- coding: utf-8 -*-
"""
🌐 Web UI - Interfață web pentru ASTRA
"""

import sys
from pathlib import Path

# Adăugă path-ul de bază
BASE_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_PATH))

from flask import Flask, render_template_string, request, jsonify
from nexus_efe_core_engine import NexusEFE
from core_router.routing_manager import RoutingManager
from llm_modules.mistral import MistralLLM
from llm_modules.qwen import QwenLLM
from llm_modules.deepseek import DeepSeekLLM
from llm_modules.wizardcoder import WizardCoderLLM
from llm_modules.codestral import CodestralLLM
from llm_modules.mythomax import MythoMaxLLM
from llm_modules.mixtral import MixtralLLM
from llm_modules.gpt4all import GPT4AllLLM

app = Flask(__name__)

# Inițializare ASTRA
llm_pool = {
    "mistral": MistralLLM(),
    "qwen": QwenLLM(),
    "deepseek": DeepSeekLLM(),
    "wizardcoder": WizardCoderLLM(),
    "codestral": CodestralLLM(),
    "mythomax": MythoMaxLLM(),
    "mixtral": MixtralLLM(),
    "gpt4all": GPT4AllLLM(),
    "default": MistralLLM(),
    "backup": QwenLLM()
}

config = {
    "thresholds": {
        "accept": 0.75
    }
}

efe_engine = NexusEFE(config, llm_pool)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>ASTRA Locală</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            width: 100%;
            max-width: 800px;
            padding: 30px;
        }
        h1 {
            color: #667eea;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
        }
        .chat-container {
            height: 400px;
            overflow-y: auto;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            background: #f9f9f9;
        }
        .message {
            margin-bottom: 15px;
            padding: 12px;
            border-radius: 10px;
            max-width: 80%;
        }
        .user-message {
            background: #667eea;
            color: white;
            margin-left: auto;
            text-align: right;
        }
        .astra-message {
            background: #764ba2;
            color: white;
        }
        .input-container {
            display: flex;
            gap: 10px;
        }
        input[type="text"] {
            flex: 1;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
        }
        button {
            padding: 15px 30px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        }
        button:hover {
            background: #764ba2;
        }
        .status {
            text-align: center;
            color: #666;
            margin-top: 20px;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>💠 ASTRA Locală</h1>
        <div class="chat-container" id="chat">
            <div class="message astra-message">
                Bun venit! Sunt ASTRA. Cu ce te pot ajuta astăzi?
            </div>
        </div>
        <div class="input-container">
            <input type="text" id="userInput" placeholder="Scrie mesajul tău..." onkeypress="if(event.key==='Enter') sendMessage()">
            <button onclick="sendMessage()">Trimite</button>
        </div>
        <div class="status" id="status">Gata</div>
    </div>
    
    <script>
        function addMessage(text, isUser) {
            const chat = document.getElementById('chat');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message ' + (isUser ? 'user-message' : 'astra-message');
            messageDiv.textContent = text;
            chat.appendChild(messageDiv);
            chat.scrollTop = chat.scrollHeight;
        }
        
        async function sendMessage() {
            const input = document.getElementById('userInput');
            const message = input.value.trim();
            if (!message) return;
            
            addMessage(message, true);
            input.value = '';
            
            const status = document.getElementById('status');
            status.textContent = 'ASTRA gândește...';
            
            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: message})
                });
                
                const data = await response.json();
                addMessage(data.response, false);
                status.textContent = 'Gata';
            } catch (error) {
                addMessage('Eroare la comunicare cu ASTRA', false);
                status.textContent = 'Eroare';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Pagină principală"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint pentru chat"""
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Mesaj gol'}), 400
        
        # Procesează prin EFE Engine
        response = efe_engine.process(user_message, user_id="web_user")
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/api/status', methods=['GET'])
def status():
    """API endpoint pentru status"""
    return jsonify({
        'status': 'online',
        'models': list(llm_pool.keys())
    })

def run_web_ui(host='127.0.0.1', port=5000, debug=False):
    """Pornește interfața web"""
    print(f"\n🌐 ASTRA Web UI pornit la http://{host}:{port}")
    print("   Deschide browser-ul și accesează adresa de mai sus\n")
    app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    run_web_ui()
