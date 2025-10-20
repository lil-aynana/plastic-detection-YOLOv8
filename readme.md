# 🌊 Plastic Detection in the Ocean using YOLOv8

This mini-project detects plastic debris in ocean and coastal images using YOLOv8 with transfer learning.

## 🚀 Project Overview
Model: YOLOv8n (Ultralytics)  
Task: Object Detection (Plastic)  
Dataset Sources:  
  -TACO Dataset  
  -Roboflow Marine Debris  
  -MARIDA (optional satellite)    

## 🛠 Installation
#Clone the repository  
git clone https://github.com/lil-aynana/plastic-detection-YOLOv8.git  
cd plastic-detection-YOLOv8  
#Create a virtual environment (optional but recommended)  
python -m venv venv  
#Activate venv  
venv\Scripts\activate  
#Install dependencies  
pip install -r requirements.txt  

## 🏃‍♂️ Usage  
python train.py --data data.yaml --epochs 50 --img 640  

## Inference
python detect.py --weights best.pt --source path/to/images_or_videos  

## 📊 Results
Detects plastic in images from coastal, drone, and satellite sources.  
Lightweight YOLOv8n allows fast inference.  
Metrics like Precision, Recall, and mAP can be logged during training.  




