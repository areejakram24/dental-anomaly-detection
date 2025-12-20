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

For this initial version, the model achieves solid detection performance with an mAP@50 of 0.91 and a caries recall of 0.88 on the validation set (see Results for details).

----------------------------------------------------

## Features

* **Multimodal Detection:** Single model detects 4 classes across X-ray radiographs + intraoral photos.
* **Medical-Relevant Classes:** caries (cavity), filling, impacted_tooth, implant.
*  **Hardware Optimized:** Successfully trained on MacBook Air M2 (16GB RAM) using Apple's Metal Performance Shaders (MPS) for GPU acceleration.
* **Clinical Utility:** High recall on caries for early detection support.
* **Medical Focus:** Prioritizes detection of subtle enamel caries and interproximal lesions.

## Clinical Motivation
## 🧬 Clinical Motivation

Dental caries detection shows high inter‑observer variability among general dentists, especially for subtle enamel and interproximal lesions. This diagnostic uncertainty can lead to missed early caries or over‑treatment, both of which negatively affect patient outcomes.

The goal of this project is to provide a reliable “second reader” that supports dental students and practitioners by flagging potential anomalies consistently, across both radiographic and photographic inputs.


## 🧮 Model Architecture

This project is built on the **YOLOv8s (Small)** architecture by Ultralytics, chosen for its optimal balance between detection accuracy and real‑time inference efficiency on lightweight hardware.

### ⚙️ Training Configuration
| Parameter       | Value     | Notes                          |
|-----------------|-----------|--------------------------------|
| **Model**       | YOLOv8s   | Small variant (~21.5M params)  |
| **Epochs**      | **30**    | Converged early on M2 hardware |
| **Image Size**  | **512px** | `imgsz=512` (square crop)      |
| **Batch Size**  | 8         | MPS memory optimized           |
| **Device**      | MPS       | MacBook Air M2 (16GB RAM)      |
| **Optimizer**   | AdamW     | Default YOLOv8 settings        |

### 🔁 Data Augmentation
The training pipeline leveraged YOLOv8’s native data augmentation suite to improve generalization and make model more robust across clinical and radiographic modalities. Key techniques included:

- Mosaic Augmentation: Combines four training images into one, forced the model to detect anomalies in different spatial scales.

- Color Space Shifting: Adjusted hue, saturation, and brightness to simulate different clinical lighting and X-ray exposure levels.

- Geometric Invariance: Applied random flips and rotations to account for various dental arch orientations.


### 🧩 Data Integration & Standardization
To create a robust detection system, data was consolidated from multiple sources to ensure multimodal coverage. The integration process involved:

-Unified Label Mapping: Synchronized disparate datasets into a consistent class schema (e.g., ensuring caries was indexed as Class 0 across both radiographic and clinical subsets).

-Multimodal Fusion: Curated a balanced mix of 2D X-rays and intraoral photographs, allowing the model to learn diagnostic features across different imaging spectrums.

-Format Verification: Validated that all annotations followed the PyTorch YOLO TXT standard, ensuring seamless integration into the Ultralytics training pipeline.

> *Result:* A single YOLOv8s model capable of detecting anomalies across both X‑ray radiographs and photographic inputs.


## 📁 Dataset Details

| Modality | Source | Classes | Images |
|----------|--------|---------|--------|
| **X-ray** | [Roboflow Dental X-ray](https://universe.roboflow.com/gozdes-projects/dental-x-ray-1imfs) | 4 classes | ~4k |
| **Clinical** | [Zenodo Intraoral](https://zenodo.org/records/14827784) | caries only | ~1k |
| **Combined** | Merged YOLOv8 format | 4 classes | **5,154 train** |

### 🏷️ Label Schema

| Class ID | Label           | Description                                                |
|-----------|-----------------|------------------------------------------------------------|
| **0**     | **Caries**      | Cavities, enamel lesions, and interproximal decay.         |
| **1**     | **Filling**     | Existing restorations (composite or amalgam).              |
| **2**     | **Impacted Tooth** | Teeth unable to erupt properly (e.g., wisdom teeth).    |
| **3**     | **Implant**     | Artificial tooth roots and prosthetic integrations.        |


## Installation

To run the Dental Anomaly Detector on your local machine, follow these steps:

git clone https://github.com/yourusername/dental-anomaly-detector.git
cd dental-anomaly-detector

I recommend using a virtual environment to manage dependencies

python3 -m venv dental_env
source dental_env/bin/activate

pip install ultralytics

pip install -r requirements.txt

The trained model weights (best.pt) are located in the weights/ directory. You do not need to download the 5GB dataset to test the model; you only need the weights and a test image.

## Usage

yolo predict model=best.pt source='test_images/' show=True
 
------------------------------------------
## Results

| Metric       | Value |
|--------------|-------|
| **mAP@50**  | **0.91** |
| **Caries Recall** | **0.88** |
| **Precision** | **0.82** |

> 🔬 *High caries recall (0.88) ensures early detection of cavities while maintaining strong overall performance.*
> Insight: Prioritizing caries recall means the model acts as a safety net for learners, catching most lesions that could otherwise be overlooked during training cases.

<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/826430a2-031c-47ae-afba-77268041e40a" />

## Clinical Relevance

This AI tool is intended to bridge the “diagnostic gap” in dental education by acting as a real‑time assistant during case review rather than replacing clinical judgment.

- **Visual Teaching Tool:** Provides instant feedback on suspected caries, fillings, implants, and impacted teeth, helping students correlate clinical photos with radiographic findings.  
- **Workflow Efficiency:** Automates the identification and charting of existing restorations, reducing manual annotation and freeing time for higher‑level clinical reasoning.  
- **Safety Net for Learners:** Encourages students to revisit regions flagged by the model, reinforcing systematic inspection habits.

## Future Scope

-3D Volumetric Integration: Expanding the model to support CBCT (Cone Beam CT) for advanced root canal and bone-loss analysis.

-Web Deployment: Developing a Streamlit dashboard for simple drag-and-drop clinical case reviews.



-------------------------------------

## Repository Structure

├── data/
│   ├── train/
│   └── val/
├── models/
├── runs/
├── app.py
├── README.md
└── requirements.txt

## Technical Stack

* YOLOv8 (Ultralytics)

* PyTorch

* OpenCV

* Roboflow / Zenodo datasets

  -------------------
  #Author

  **Developed by Areej Akram (https://www.linkedin.com/in/areej-akram-068447348/)**

# Acknowledgements

This project was made possible through the use of open-source datasets and frameworks that support the advancement of medical AI.

* Ultralytics YOLOv8: For providing the high-performance computer vision architecture and training engine.

* PyTorch: For the underlying deep learning framework and MPS (Metal Performance Shaders) support for Apple Silicon.

* Zenodo & Roboflow: For hosting the annotated multimodal dental datasets utilized in training.

* Open-Source Dental Research: Gratitude to the researchers and clinicians who contribute labeled radiographic data for the benefit of medical education.
