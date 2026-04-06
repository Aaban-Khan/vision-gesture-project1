<h1 align="center">🤖Vision Gesture Project1</h1>

<p align="center">
A real-time hand gesture recognition system using OpenCV and MediaPipe.
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>Real-time hand tracking using webcam</li>
  <li>Finger counting system</li>
  <li>Gesture-based mode detection</li>
  <li>Index finger tracking (Move mode)</li>
  <li>Basic interaction system (Move, Select, Stop, Reset)</li>
</ul>

<hr>

<h2>🧠 How It Works</h2>
<ul>
  <li>Captures video using OpenCV</li>
  <li>Uses MediaPipe to detect hand landmarks</li>
  <li>Analyzes which fingers are up</li>
  <li>Maps gestures to different modes</li>
</ul>

<hr>

<h2>🎮 Gesture Controls</h2>
<table border="1" cellpadding="8">
  <tr>
    <th>Gesture</th>
    <th>Mode</th>
  </tr>
  <tr>
    <td>Index Finger</td>
    <td>Move</td>
  </tr>
  <tr>
    <td>Index + Middle</td>
    <td>Select</td>
  </tr>
  <tr>
    <td>All Fingers</td>
    <td>Reset</td>
  </tr>
  <tr>
    <td>Others</td>
    <td>Stop</td>
  </tr>
</table>

<hr>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li>Python</li>
  <li>OpenCV</li>
  <li>MediaPipe</li>
</ul>

<hr>

<h2>⚙️ Setup</h2>
<pre>
pip install opencv-python mediapipe
</pre>

<h2>▶️ Run</h2>
<pre>
python main.py
</pre>

<hr>

<h2>📂 Project Structure</h2>
<pre>
gesture-control-system/
│── main.py
│── hand_landmarker.task
│── README.md
</pre>

<hr>

<h2>📌 Note</h2>
<p>
This project is built for learning computer vision concepts like hand tracking,
gesture detection, and real-time processing.
</p>

<hr>

<h2>🔥 Future Improvements</h2>
<ul>
  <li>Gesture stability improvement</li>
  <li>Mouse control using hand gestures</li>
  <li>Drawing system using index finger</li>
</ul>

<hr>

<p align="center">Made by Aaban 💻</p>
