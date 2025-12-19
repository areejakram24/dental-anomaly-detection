# CV1-Log[README.md](https://github.com/user-attachments/files/23388309/README.md)
<div align="center">
  <img src="https://img.shields.io/badge/YOLOv8-Dental%20Anomaly%20Detection-brightgreen?style=for-the-badge&logo=ultralytics&logoColor=white" alt="YOLOv8 Badge">
  <br><br>
  <h1>🦷 Dental Anomaly Detection System</h1>
  <p><i>Multimodal YOLOv8 detector for caries, fillings, implants, and impacted teeth across X-rays and clinical photos</i></p>
</div>


[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-orange?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Ultralytics](https://img.shields.io/badge/YOLOv8-Ultralytics-blueviolet)](https://github.com/ultralytics/ultralytics)
[![Hardware](https://img.shields.io/badge/Hardware-Apple%20M2-silver?logo=apple&logoColor=white)](https://www.apple.com/silicon/)
[![Backend](https://img.shields.io/badge/Backend-MPS/Metal-grey)](https://developer.apple.com/metal/pytorch/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project leverages the YOLOv8s (Small) architecture to automate the detection of dental caries from both clinical and radiographic images. Designed as a diagnostic assistant for dental students and practitioners, the model identifies dental pathologies in real time — helping to reduce diagnostic oversight and improve clinical accuracy.

----------------------------------------------------

## Features

* **Multimodal Detection:** Single model detects 4 classes across X-ray radiographs + intraoral photos.
* **Medical-Relevant Classes:** caries (cavity), filling, impacted_tooth, implant.
* **Clinical Utility:** High recall on caries for early detection support.
*  **Hardware Optimized:** Successfully trained on MacBook Air M2 (16GB RAM) using Apple's Metal Performance Shaders (MPS) for GPU acceleration.
* **Medical Focus:** Prioritizes detection of subtle enamel caries and interproximal lesions.
------------------------------------------------------




## Clinical Motivation
Dental caries detection shows high inter-observer variability among general dentists. This system:

* Distinguishes caries from restorations/implants (reduces false positives)

* Works on both radiographic + photographic inputs

* Designed as teaching aid for pre-clinical dental students



## 🧮 Model Architecture

This project is built on the **YOLOv8s (Small)** architecture by Ultralytics, chosen for its balance between detection accuracy and real‑time inference efficiency on lightweight hardware.

### ⚙️ Training Setup
| Parameter | Description | Value |
|------------|-------------|-------|
| **Model Variant** | YOLOv8s (Small) | ✅ |
| **Input Image Size** | Image resolution used during training (`imgsz`) | 512×512 |
| **Batch Size** | Number of images per iteration | 8 |
| **Epochs** | Total training cycles | *[fill in]* |
| **Device** | Trained on MacBook Air M2 (16 GB RAM, Apple MPS backend) | MPS |
| **Optimizer** | Default YOLOv8 AdamW | — |

### 🔁 Data Augmentation
To improve generalization across modalities, standard YOLOv8 augmentations were applied:
- Random horizontal/vertical flips  
- Hue, saturation, and brightness shifts  
- Mosaic and mixup combinations  
- Rotation and scaling within ±10°

### 🧩 Multimodal Data Integration
Radiographic and intraoral clinical datasets were:
- Converted to the **YOLO format** with consistent class indices (`caries`, `filling`, `impacted_tooth`, `implant`).  
- Merged using a unified label schema (class 0 = `caries` across all datasets).  
- Normalized and resized to maintain cross‑modality consistency.  

> 🧠 *Result:* A single YOLOv8s model capable of detecting anomalies across both X‑ray radiographs and photographic inputs.


## 📁 Dataset Details

| Modality | Source | Classes | Images |
|----------|--------|---------|--------|
| **X-ray** | [Roboflow Dental X-ray](https://universe.roboflow.com/gozdes-projects/dental-x-ray-1imfs) | 4 classes | ~4k |
| **Clinical** | [Zenodo Intraoral](https://zenodo.org/records/14827784) | caries only | ~1k |
| **Combined** | Merged YOLOv8 format | 4 classes | **5,154 train** |

**Label Schema** (class 0 consistent across both):
0 x_center y_center width height # caries/cavity
1 ... # filling
2 ... # impacted_tooth
3 ... # implant

## Performance Metrics

The model was trained for 30 epochs with an image size of 512px.
