from ultralytics import YOLO

def main():
  
    model = YOLO("yolov8s.pt") 
  
    results = model.train(
        data="data.yaml",     # Path to your dataset config
        epochs=30,           
        imgsz=512,            
        batch=8,            
        name="dental_caries_model" # Name of the output folder
    )

if __name__ == "__main__":
    main()
