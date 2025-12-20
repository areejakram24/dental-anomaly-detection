from ultralytics import YOLO
import sys

def run_prediction(image_path):
   
    model = YOLO("weights/best.pt")

    results = model.predict(source=image_path, conf=0.25, save=True)

    for r in results:
        print(f"Prediction saved to: {r.save_dir}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_prediction(sys.argv[1])
    else:
        print("Please provide an image path. Example: python predict.py sample.jpg")
