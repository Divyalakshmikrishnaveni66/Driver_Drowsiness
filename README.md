# Driver Drowsiness Detection System

## Overview
The Driver Drowsiness Detection System is designed to **monitor a driver’s alertness** in real-time and provide an **instant warning** if the driver shows signs of drowsiness. This helps prevent accidents caused by fatigue or sleepiness while driving.

---

## How It Works
1. A **webcam captures video** of the driver’s face.  
2. Each frame is analyzed using a **YOLOv8 deep learning model** trained to detect two states:
   - **Drowsy 😴**  
   - **Awake 👀**  
3. If drowsiness is detected:
   - The system shows a **red alert label** on the video.  
   - A **beep sound** is played to warn the driver.  
4. If the driver is awake, the system shows a **green label**.

---

## Key Components
- **YOLOv8 Model** – Detects drowsiness from facial features.  
- **OpenCV** – Captures and processes video frames.  
- **Flask Web App** – Displays the live video feed and status.  
- **Alert Mechanism** – Beep sound for warning.

---

## Applications
- Prevent road accidents due to driver fatigue.  
- Can be integrated into smart cars or driver assistance systems.  
- Useful in long-haul transportation and fleet management.

---

## Advantages
- Real-time monitoring and alert system.  
- Easy to use with webcam input.  
- Works cross-platform (Windows, Linux, Mac).  

---

## Limitations
- Accuracy depends on the quality of the training dataset.  
- Only a prototype; not meant for commercial deployment without further validation.  

---

## Conclusion
This system provides a **simple and effective way** to monitor driver alertness and warn against drowsiness, enhancing road safety.
