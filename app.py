# app.py
# app.py
from flask import Flask, render_template, Response, jsonify
import cv2
from detect import detect_frame  # your detect.py must implement this
import state
import time
import threading
import winsound  # Windows beep

app = Flask(__name__, template_folder="../templates", static_folder="../static")

camera = None
output_frame = None
lock = threading.Lock()

def camera_loop():
    """Continuously capture frames and detect drowsiness."""
    global camera, output_frame
    while camera is not None:
        success, frame = camera.read()
        if not success:
            continue

        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (640, 480))

        try:
            frame = detect_frame(frame)
        except Exception as e:
            print("Detection error:", e)

        # Play beep if drowsy
        if getattr(state, "current_status", "Awake") == "Drowsy":
            winsound.Beep(2500, 500)  # Frequency 2500Hz, duration 500ms

        with lock:
            output_frame = frame

        time.sleep(0.03)  # ~30 FPS

def generate_frames():
    """Yield frames to browser for streaming."""
    global output_frame
    while True:
        if output_frame is None:
            time.sleep(0.1)
            continue

        with lock:
            ret, buffer = cv2.imencode('.jpg', output_frame)
            frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start')
def start():
    """Start camera capture and detection thread."""
    global camera
    if camera is None:
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not camera.isOpened():
            camera = None
            return "Failed to start camera"

        # Start camera thread
        thread = threading.Thread(target=camera_loop)
        thread.daemon = True
        thread.start()

    return "Camera Started"

@app.route('/stop')
def stop():
    global camera
    if camera is not None:
        camera.release()
        camera = None
        with lock:
            global output_frame
            output_frame = None
        state.current_status = "Awake"
    return "Camera Stopped"

@app.route('/status')
def status():
    return jsonify({"status": getattr(state, "current_status", "Unknown")})

if __name__ == "__main__":
    print("🔥 Server Running on http://127.0.0.1:5000")
    app.run(debug=True, host="0.0.0.0", port=5000)