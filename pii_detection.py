import torch
from flask import Flask, request, jsonify

from transformers import BertTokenizer, BertForTokenClassification

app = Flask(__name__)

# Load the Bert model and tokenizer
model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name)

# Function to extract PII from the input text
def extract_pii(text):
    tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        output = model(**tokens)
    predictions = output.logits.argmax(2).tolist()[0]

    pii_detected = []
    current_pii = ""
    
    for token, label_id in zip(tokens['input_ids'][0], predictions):
        token = tokenizer.decode([token])
        label = model.config.id2label[label_id]

        if label != "O":
            current_pii += " " + token
        else:
            if current_pii:
                pii_detected.append(current_pii.strip())
            current_pii = ""
    
    if current_pii:
        pii_detected.append(current_pii.strip())
    
    return pii_detected

@app.route('/identify', methods=['POST'])
def analyze_pii():
    try:
        data = request.json
        text = data['body']

        pii_detected = extract_pii(text)

        response = {
            "pii_detected": pii_detected,
            "error": "nil"
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
