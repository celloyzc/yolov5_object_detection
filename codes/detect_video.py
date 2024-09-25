import cv2
import torch
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def detect_objects_in_video(video_path, model_path, output_path):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Modeli yükle
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
    model.to(device).eval()

    # Video aç
    cap = cv2.VideoCapture(video_path)

    # Video yazıcıyı ayarla
    video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (video_width, video_height))

    with torch.no_grad():
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = model(frame)  # Modeli doğrudan frame üzerine uygula

            # Detections sonucunu al
            detections = results.pred[0].detach().cpu().numpy()

            for det in detections:
                x_min, y_min, x_max, y_max, confidence, class_id = det
                label = f'{model.names[int(class_id)]} {confidence:.2f}'
                color = (0, 255, 0)  # Yeşil renkli kutu çizelim (BGR formatında)

                # Kareyi çizelim
                cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), color, 2)

                # Etiketi yazalım
                cv2.putText(frame, label, (int(x_min), int(y_min - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # Frame'i BGR formatına dönüştürelim ve videoya yazalım
            out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

        cap.release()
        out.release()
        cv2.destroyAllWindows()

def select_video_file():
    file_path = filedialog.askopenfilename(title="Bir video seciniz:", filetypes=[("Video files", "*.mp4 *.avi")])
    if file_path:
        model_path = filedialog.askopenfilename(title="Yolov5 model dosyasini seciniz:", filetypes=[("Model files", "*.pt")])
        if model_path:
            output_dir = "D:/pyton_temel/out"
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            output_path = f"{output_dir}/output_video.avi"  # Sonuç videonun dosya yolu
            detect_objects_in_video(file_path, model_path, output_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Pencereyi gösterme

    select_video_file()
