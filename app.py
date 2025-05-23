from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load the model
with open('fraud_detection_model.pkl', 'rb') as f:
    model_data = pickle.load(f)

model = model_data['model']
scaler = model_data['scaler']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])
        input_df['scaled_amount'] = scaler.transform(input_df['Amount'].values.reshape(-1, 1))
        input_df['scaled_time'] = scaler.transform(input_df['Time'].values.reshape(-1, 1))
        input_df.drop(['Time', 'Amount'], axis=1, inplace=True)
        cols = [f'V{i}' for i in range(1, 29)] + ['scaled_amount', 'scaled_time']
        input_df = input_df[cols]
        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)[0, 1]
        return jsonify({
            'prediction': int(prediction[0]),
            'probability': float(probability),
            'is_fraud': bool(prediction[0])
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=7860)
