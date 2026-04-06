# 🌱 Multimodal Predictive Crop Intelligence System

### *IoT Time-Series + Vision-Based Learning for Early Crop Stress Prediction*

---

## 📌 Overview

This project presents a **multimodal AI system** that predicts **crop stress and disease before visible symptoms appear** by combining:

* 📡 IoT sensor data (time-series)
* 🌿 Leaf image analysis (CNN-based)
* 🧠 Temporal modeling (LSTM / Transformer)
* 🔗 Multimodal feature fusion

Unlike traditional systems that detect diseases **after symptoms appear**, this system focuses on **early-stage prediction**, enabling proactive agricultural intervention.

---

## 🎯 Objectives

* Predict crop stress **in advance (t+1, t+3 days)**
* Combine **environmental conditions + visual cues**
* Simulate **real-time IoT data ingestion**
* Provide **actionable recommendations**
* Build a **research-grade, publishable system**

---

## 🚀 Key Features

* 🔮 Predictive disease modeling (not reactive detection)
* 🧠 Multimodal learning (IoT + Vision)
* ⏱️ Time-series forecasting using LSTM/Transformer
* 🌿 CNN-based leaf disease feature extraction
* 📊 Real-time data simulation (no hardware required)
* 📈 Interactive dashboard (Streamlit)
* 🧪 Research-ready evaluation pipeline

---

## 🧩 System Architecture

```
IoT Time-Series Data (Simulated / Dataset)
                +
Leaf Images (PlantVillage / Custom)
                ↓
     Data Preprocessing
                ↓
   ┌──────────────────────┐
   │  CNN (Image Model)   │
   └──────────────────────┘
                +
   ┌──────────────────────┐
   │ LSTM / Transformer   │
   │ (Time-Series Model)  │
   └──────────────────────┘
                ↓
        Feature Fusion
                ↓
   Disease Prediction (Future)
                ↓
 Dashboard + Recommendations
```

---

## 📡 IoT Data Handling (Without Hardware)

Since no physical IoT devices are used, we simulate real-time data using:

### ✅ Approach

* Public datasets (agriculture/weather)
* Synthetic data generation
* Streaming simulation

### 🔁 Real-Time Simulation

```python
import time

while True:
    sample = dataset.sample(1)
    process(sample)
    time.sleep(5)
```

---

## 🌿 Image Model (CNN)

We use and extend:

👉 FarmBud

### Enhancements:

* Extract intermediate **feature embeddings**
* Use CNN outputs as **input to fusion model**
* Improve generalization with transfer learning

---

## 🧠 Model Architecture

### 1. Time-Series Model

* Model: LSTM / Transformer
* Input: Past 24–72 time steps
* Features:

  * Temperature
  * Humidity
  * Soil Moisture
  * pH
  * Light Intensity

---

### 2. CNN Model

* Input: Leaf Image
* Output:

  * Disease class probabilities
  * Feature embeddings

---

### 3. Multimodal Fusion

```
Z = concat(CNN_features, LSTM_features)
Z → Dense Layers → Prediction
```

---

### 4. Output

* 🌡️ Stress Probability (%)
* 🌿 Disease Risk Level
* 📊 Future Prediction (t+1, t+3)
* 💡 Recommendations (JSON)

---

## 📊 Dataset Design

### 1. IoT Time-Series Data

| Time | Temp | Humidity | Soil | pH | Light |
| ---- | ---- | -------- | ---- | -- | ----- |

---

### 2. Image Dataset

* PlantVillage Dataset
* Custom leaf images

---

### 3. Training Input

```
X = {
  time_series_window,
  image
}

Y = future_disease_label
```

---

## 🧪 Synthetic Label Generation

Since real labeled IoT → disease data is scarce:

### Strategy:

* Use CNN predictions
* Apply environmental thresholds

```python
if humidity > 80 and temp > 30:
    label = "high_risk"
```

---

## 📈 Evaluation Metrics

* Accuracy
* Precision / Recall / F1-score
* AUC-ROC
* RMSE (prediction error)
* ⏱️ Early Prediction Gain (key contribution)

---

## 🔬 Experimental Setup

### Models Compared:

| Model                 | Input | Purpose     |
| --------------------- | ----- | ----------- |
| CNN Only              | Image | Baseline    |
| LSTM Only             | IoT   | Baseline    |
| Multimodal (Proposed) | Both  | Final Model |

---

## 💻 Tech Stack

### Machine Learning

* PyTorch / TensorFlow

### Data Processing

* Pandas, NumPy

### Visualization

* Matplotlib, Seaborn

### Dashboard

* Streamlit

---

## 📊 Dashboard Features

* 📡 Real-time IoT stream simulation
* 🌿 Leaf image upload
* 📈 Prediction graphs
* 🚨 Risk alerts
* 💡 Smart recommendations

---

## 🔥 Advanced Features

### 1. Explainable AI (XAI)

* Grad-CAM for image model
* SHAP for IoT features

---

### 2. Forecast Visualization

* Future disease probability trends

---

### 3. Recommendation Engine

```json
{
  "risk": "high",
  "action": "increase irrigation"
}
```

---

## 📄 Research Contribution

### 🔍 Problem Statement

> Traditional crop monitoring systems detect diseases after symptoms appear, limiting preventive action.

---

### 💡 Proposed Solution

A **multimodal predictive framework** that integrates:

* IoT time-series data
* Visual leaf analysis
* Temporal learning

---

### 🧠 Novel Contributions

* Predictive modeling (future disease forecasting)
* Multimodal fusion (IoT + vision)
* Synthetic labeling strategy
* Real-time simulation without hardware

---

## 🧪 Research Question

> Can multimodal IoT + vision-based models predict crop stress earlier and more accurately than unimodal systems?

---

## ⚙️ Installation

```bash
git clone <repo-url>
cd project
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

For dashboard:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
├── data/
├── models/
│   ├── cnn_model.py
│   ├── lstm_model.py
│   └── fusion_model.py
├── utils/
├── app.py
├── main.py
└── README.md
```

---

## 🔮 Future Work

* 🌍 Geo-aware predictions using GPS
* 🤖 Automated irrigation control
* ☁️ Cloud deployment with live APIs
* 🔗 Federated learning for scalability

---

## 👨‍💻 Authors

* Shashvat Rajora & Team

---

## 📜 License

This project is for academic and research purposes.

---

## ⭐ Final Note

This project is designed to bridge the gap between **AI research and real-world agriculture**, enabling **early intervention, resource optimization, and improved crop yield**.

---
