# ✋ Hand Gesture Recognition with OpenCV & Mediapipe

## 📌 Overview

Welcome to Hand Gesture Recognition, a real-time computer vision project that detects hand gestures using OpenCV and Mediapipe!
Wave your hand in front of the camera, and it can recognize common gestures like OK, Thumbs Up, and finger counts from 1 to 5 — all in real-time. 🚀

---

## 🎯 Project Highlights

- ✅ Real-time hand tracking using **MediaPipe**
- ✅ Real-time Gesture Detection
- ✅ Finger Counting (0-5 Fingers)
- ✅ Custom Gestures: OK, Thumbs Up (Best of Luck)
- ✅ Live Webcam Feed with Annotations
- ✅ Lightweight & Fast (Optimized for Speed)
- ✅ Extendable for Custom Gestures

---

## 🛠️ Technologies Used
- Python 🐍
- OpenCV 🎥
- MediaPipe 🤖 (pre-trained hand landmarks model)
- Math 📐

---

## ✨ How it Works

- Hand Detection: **Mediapipe detects 21 hand landmarks with high accuracy.**
- Finger State Calculation:
              1. **If the fingertip landmark is above the middle joint landmark → Finger is open.**
              2. **For the thumb, x-axis comparison is used instead of y-axis.**
- Gesture Recognition: **Based on the number and position of open fingers, predefined gestures are recognized.**
- Display: **Detected gesture text is overlayed onto the live video frame beautifully!**

---

## 📸 Sample Outputs

| ✋ Gesture         | 🏷️ Detected Label                      |
|:------------------|:--------------------------------------|
| 👌 OK Sign         | `Detected Gesture: OK`                |
| 👍 Thumbs Up       | `Detected Gesture: Thumbs Up (Best of Luck)` |
| ☝️ One Finger      | `Detected Gesture: 1`                 |
| ✌️ Two Fingers     | `Detected Gesture: 2`                 |
| 🤟 Three Fingers   | `Detected Gesture: 3`                 |
| 🖖 Four Fingers    | `Detected Gesture: 4`                 |
| 🖐️ Five Fingers    | `Detected Gesture: 5`                 |

---

## 🚀 Quick Start
1. **1. Clone the Repository**
   ```bash
   git clone https://github.com/your-username/hand-gesture-recognition.git
   cd hand-gesture-recognition

2. **Install Dependencies**
   ```bash
   pip install opencv-python mediapipe
   (Make sure Python 3.7+ is installed)

4. **Run the Script**
   ```bash
   python gesture.py

5. **Instructions**
- Show your hand inside the green box.
- Try different gestures — numbers, OK, Thumbs Up.
- Press Esc to exit.

---

## 📦 Folder Structure
![image](https://github.com/user-attachments/assets/c3de0203-2ea0-47cb-b2ef-552cf8d9d03a)

---

## 📚 How It Works

- Capture video from webcam.
- Detect hand landmarks using MediaPipe.
- Analyze finger positions and angles.
- Count fingers or recognize gestures.
- Display result on screen.

---

## 🎯 Future Enhancements

- Add custom gestures (like "rock", "love", "peace").
- Voice output for recognized gestures.
- Use deep learning models for gesture classification.

---

## 🙌 Acknowledgements

- **Google MediaPipe** - for Hand Landmarks.
- **OpenCV** - for computer vision magic.

---

## 🌟 Future Plans

- 🔮 **Add recognition for more advanced gestures (e.g., "Rock & Roll", "Peace Sign").**
- 🎵 **Integrate sound or haptic feedback on gesture detection.**
- 📈 **Build a dashboard showing gesture detection statistics.**
- 🧠 **Integrate AI/ML models for complex gesture classifications.**

---

## 💖 Feel Free to Contribute!
- If you like the project, give it a ⭐!
- Pull requests and ideas are always welcome!

---

## 🔥 Made with Passion by [Nikita Karmakar]
## Developed with ❤️ using OpenCV and Mediapipe.

If you need any more tweaks, just let me know! 😊
