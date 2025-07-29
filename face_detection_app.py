import cv2
import streamlit as st
import numpy as np
import datetime
import os

# Load the Haar Cascade Classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Streamlit Interface
def app():
    st.title("📸 Face Detection using Viola-Jones Algorithm")
    st.markdown("""
    ## Instructions:
    1. Click **"Start Webcam Detection"** to begin detecting faces.
    2. Use the sliders to fine-tune detection settings.
    3. Use the color picker to choose the rectangle color.
    4. Click **'Save Image'** to save the current frame with detected faces.
    5. Press **'q'** in the webcam window to stop the detection.
    """)

    # Rectangle Color Picker
    rect_color = st.color_picker("🎨 Choose rectangle color", "#00FF00")
    # Convert hex color to BGR tuple
    color_bgr = tuple(int(rect_color.lstrip('#')[i:i+2], 16) for i in (4, 2, 0))

    # Sliders for scaleFactor and minNeighbors
    scale_factor = st.slider("🔍 Adjust scaleFactor", 1.05, 2.0, 1.3, 0.05)
    min_neighbors = st.slider("🧠 Adjust minNeighbors", 1, 10, 5)

    # Start Face Detection
    if st.button("📷 Start Webcam Detection"):
        detect_faces(scale_factor, min_neighbors, color_bgr)

# Face Detection Function
def detect_faces(scale_factor, min_neighbors, color_bgr):
    cap = cv2.VideoCapture(0)
    saved_frame = None

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("🚫 Failed to access webcam.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=scale_factor,
            minNeighbors=min_neighbors
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), color_bgr, 2)

        cv2.imshow("Face Detection - Press 'q' to quit", frame)
        saved_frame = frame.copy()  # Save latest frame with rectangles

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Save frame if user chooses to
    if saved_frame is not None:
        if st.button("💾 Save Image with Detected Faces"):
            save_path = f"detected_faces_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(save_path, saved_frame)
            st.success(f"✅ Image saved as: `{save_path}`")

if __name__ == "__main__":
    app()
