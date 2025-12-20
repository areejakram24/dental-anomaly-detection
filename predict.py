from ultralytics import YOLO
model = YOLO('weights/best.pt')
results = model.predict(source='inference/test_image.jpg', save=True, conf=0.5)
