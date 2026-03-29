# detect.py
import cv2
import state

def detect_frame(frame):
    # Dummy detection: eyes closed detection logic here
    # For testing, flip status randomly
    import random
    if random.randint(0, 50) == 1:  # simulate drowsiness
        state.current_status = "Drowsy"
    else:
        state.current_status = "Awake"

    # Optional: draw status on frame
    cv2.putText(frame, state.current_status, (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255) if state.current_status=="Drowsy" else (0,255,0), 2)
    return frame