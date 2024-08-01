from flask import Flask, request, jsonify, send_from_directory
import openai

app = Flask(__name__, static_url_path='', static_folder='static')

openai.api_key = 'your GPT key'  

consensus_keywords = ['agree', 'agreement', 'concurred', 'same opinion', 'identical thoughts', 'consensus']

conversation_history = []
stop_sequences = [".", "?", "!", "。"]  # 設置停止序列

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/start_chat', methods=['POST'])
def start_chat():
    global conversation_history
    data = request.get_json()
    topic = data['topic']
    conversation_history = [
        {"role": "system", "content": f"The discussion topic is: {topic}."},
        {"role": "system", "content": "Assistant try to present good and persuadable solutions for the topic to User on the other side."},
        {"role": "system", "content": "User is always strongly debateing with assistant until assistant come up with a persuadable explaination for the topic."}
    ]
    return initiate_chat("assistant")

@app.route('/continue_chat', methods=['GET'])
def continue_chat():
    global conversation_history
    
    if check_consensus():
        return finalize_consensus()
    else:
        next_role = "user" if conversation_history[-1]['role'] == "assistant" else "assistant"
        return initiate_chat(next_role)

def initiate_chat(role):
    global conversation_history
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        max_tokens=150,
        stop=stop_sequences
    )
    
    message_content = response.choices[0].message['content']
    formatted_message = f"{role.capitalize()}: {message_content.strip()}"
    conversation_history.append({"role": role, "content": message_content})
    
    return jsonify(message=formatted_message)

def check_consensus():
    global conversation_history
    last_message = conversation_history[-1]['content'].lower() if conversation_history else ""
    return any(keyword in last_message for keyword in consensus_keywords)

def finalize_consensus():
    global conversation_history
    last_message = conversation_history[-2]['content']
    #consensus_content = extract_consensus_content(last_message)
    return jsonify(message=f"{last_message}", end=True)

def extract_consensus_content(text):
    words = text.split()
    return words[-1] if words else "undetermined"

if __name__ == '__main__':
    app.run(debug=True)
