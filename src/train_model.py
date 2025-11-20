# Dummy ML training script (for demonstration only)

import random
import csv

def load_dataset(path='dataset/data.csv'):
    data = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({'value': float(row['value']), 'label': int(row['label'])})
    return data

def train(data):
    # Dummy "training" that computes average of positive vs negative labels
    pos = [d['value'] for d in data if d['label'] == 1]
    neg = [d['value'] for d in data if d['label'] == 0]
    avg_pos = sum(pos)/len(pos) if pos else 0
    avg_neg = sum(neg)/len(neg) if neg else 0
    accuracy = random.uniform(0.7, 0.99)  # placeholder accuracy
    return {'avg_pos': avg_pos, 'avg_neg': avg_neg, 'accuracy': accuracy}

if __name__ == '__main__':
    data = load_dataset()
    result = train(data)
    print("Training complete.")
    print(f"Avg positive value: {result['avg_pos']:.2f}")
    print(f"Avg negative value: {result['avg_neg']:.2f}")
    print(f"Reported accuracy (simulated): {result['accuracy']:.2f}")
