mkdir projai

cd projai

python3 -m venv projai

source projai/bin/activate

pip install ultralytics

git clone https://github.com/ultralytics/ultralytics.git

pip install --upgrade pip

pip3 install torch torchvision

cd ..
mkdir training
mkdir inference
mkdir data

touch modal_data.yaml

cd ~
cd training 
mkdir datasets
cd ~/training/datasets

curl -L -o intraoral_caries.zip "https://zenodo.org/records/14827784/files/Benchmarking%20Dataset.zip?download=1"

curl -L -C - -o intraoral_caries.zip "https://zenodo.org/records/14827784/files/Benchmarking%20Dataset.zip?download=1"

unzip intraoral_caries.zip -d intraoral_caries

ls -lh intraoral_caries.zip

ls ~/training/datasets/intraoral_caries

ls -R intraoral_caries | head -n 20

cd ~
mkdir -p data/images/train
mkdir -p data/images/val
mkdir -p data/labels/train
mkdir -p data/labels/val

mv training/datasets/intraoral_caries/Benchmarking\ Dataset/train/images/* data/images/train/
mv training/datasets/intraoral_caries/Benchmarking\ Dataset/train/yolo/* data/labels/train/
mv training/datasets/intraoral_caries/Benchmarking\ Dataset/valid/images/* data/images/val/
mv training/datasets/intraoral_caries/Benchmarking\ Dataset/valid/yolo/* data/labels/val/

mkdir -p data/images/train data/images/val data/labels/train data/labels/val

cd ~/Downloads
ls

mkdir -p ~/training/datasets
mv "Dental X-ray.v1.yolov8.zip" ~/training/datasets/dental_xray_yolo.zip

cd ~/training/datasets
unzip dental_xray_yolo.zip -d dental_xray_yolo
rm dental_xray_yolo.zip
ls dental_xray_yolo

cd ~/training/datasets
ls -lh

rm intraoral_caries.zip

ls -R ~/data

cat ~/training/datasets/dental_xray_yolo/train/labels/$(ls ~/training/datasets/dental_xray_yolo/train/labels | head -n 1)
cat ~/training/datasets/dental_xray_yolo/data.yaml

mv ~/training/datasets/dental_xray_yolo/train/images/* ~/data/images/train/
mv ~/training/datasets/dental_xray_yolo/valid/images/* ~/data/images/val/
mv ~/training/datasets/dental_xray_yolo/train/labels/* ~/data/labels/train/
mv ~/training/datasets/dental_xray_yolo/valid/labels/* ~/data/labels/val/

nano ~/data/data.yaml
#in yaml file
path: /Users/cheesecake/data
train: images/train
val: images/val

nc: 4
names: ['caries', 'filling', 'impacted_tooth', 'implant']

cat ~/data/data.yaml

echo "Total Training Images: $(ls ~/data/images/train | wc -l)"

yolo detect train \
  data=/Users/cheesecake/data/data.yaml \
  model=yolov8s.pt \
  epochs=25 \
  imgsz=512 \
  device=mps \
  batch=8


  yolo detect train resume model=/Users/cheesecake/data/runs/detect/train/weights/last.pt

