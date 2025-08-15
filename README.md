# Face Detection-Open CV

A real-time face detection application using OpenCV's Haar Cascade classifier. This project captures video from your webcam and detects faces in real-time, drawing green rectangles around detected faces.

## Author
**naakaarafr**

## Features

- ✨ Real-time face detection using webcam
- 🎯 Haar Cascade classifier for accurate face detection
- 🟢 Visual feedback with green rectangles around detected faces
- ⚡ Optimized for performance with adjustable detection parameters
- 🛡️ Robust error handling for common issues
- 🔧 Easy to customize and extend

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.6 or higher
- OpenCV (cv2)
- A working webcam/camera

## Installation

### Step 1: Clone or Download the Project
```bash
git clone https://github.com/naakaarafr/Face-Detection-Open-CV.git
cd Face-Detection-Open-CV
```

### Step 2: Install Required Dependencies
```bash
pip install opencv-python
```

### Step 3: Verify Installation
Run this command to verify OpenCV is installed correctly:
```bash
python -c "import cv2; print(cv2.__version__)"
```

## Project Structure

```
Face-Detection-Open-CV/
│
├── face_reco.py              # Main face detection script
├── README.md                 # This file
└── requirements.txt          # Python dependencies
```

## Usage

### Running the Application

1. **Navigate to the project directory:**
   ```bash
   cd path/to/your/project
   ```

2. **Run the script:**
   ```bash
   python face_reco.py
   ```

3. **Using the application:**
   - The webcam window will open automatically
   - Position yourself in front of the camera
   - Green rectangles will appear around detected faces
   - Press `ESC` key to exit the application

### Controls
- **ESC Key**: Exit the application
- **Window Close Button**: Alternative way to close (may require pressing ESC first)

## How It Works

1. **Initialization**: The script loads the Haar Cascade classifier for frontal face detection
2. **Camera Setup**: Opens the default camera (usually webcam)
3. **Frame Processing**: 
   - Captures frames from the webcam
   - Converts each frame to grayscale for better detection
   - Applies the Haar Cascade classifier to detect faces
4. **Visualization**: Draws green rectangles around detected faces
5. **Display**: Shows the processed frame with face detections

## Technical Details

### Haar Cascade Parameters
The `detectMultiScale` function uses these parameters:
- **Scale Factor (1.3)**: How much the image size is reduced at each scale
- **Min Neighbors (5)**: How many neighbors each candidate rectangle should have to retain it
- **Min Size**: Minimum possible object size, smaller objects are ignored

### File Structure Explanation
```python
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
```
This line automatically finds the correct path to the Haar Cascade file installed with OpenCV.

## Troubleshooting

### Common Issues and Solutions

#### 1. "Can't open file: 'haarcascade_frontalface_default.xml'"
**Solution**: The code now uses the full path to the cascade file:
```python
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
```

#### 2. "Could not open webcam"
**Possible causes and solutions**:
- Webcam is being used by another application → Close other camera applications
- No webcam connected → Connect a webcam or use a different camera index
- Permission issues → Grant camera permissions to your terminal/IDE

#### 3. "Could not read frame"
**Solutions**:
- Check webcam connection
- Try different camera index (0, 1, 2, etc.)
- Restart the application

#### 4. Poor Detection Performance
**Optimization tips**:
- Ensure good lighting
- Position face directly toward camera
- Adjust detection parameters in the code
- Clean webcam lens

### Advanced Troubleshooting

#### Finding Camera Index
If your default camera doesn't work, try different indices:
```python
# Try different camera indices
webcam = cv2.VideoCapture(1)  # or 2, 3, etc.
```

#### Manual Cascade File Installation
If the automatic path doesn't work:
1. Download from: https://github.com/opencv/opencv/tree/master/data/haarcascades
2. Place `haarcascade_frontalface_default.xml` in your project folder
3. Update the code to use the local file

## Customization

### Adjusting Detection Sensitivity
Modify these parameters in the `detectMultiScale` function:

```python
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,      # Smaller = more thorough (slower)
    minNeighbors=3,       # Lower = more detections (more false positives)
    minSize=(30, 30),     # Minimum face size in pixels
    maxSize=(300, 300)    # Maximum face size in pixels
)
```

### Changing Rectangle Appearance
Modify the rectangle drawing:
```python
cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)  # Blue, thicker border
```

### Adding Face Labels
Add text labels to detected faces:
```python
cv2.putText(img, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
```

## Performance Tips

1. **Optimize for Speed**: Use smaller scale factors and fewer minimum neighbors
2. **Optimize for Accuracy**: Use larger scale factors and more minimum neighbors
3. **Lighting**: Ensure good, even lighting for better detection
4. **Camera Quality**: Higher resolution cameras generally provide better detection

## Future Enhancements

Potential improvements you could add:

- [ ] Face recognition (identifying specific people)
- [ ] Multiple face detection algorithms
- [ ] Face landmark detection
- [ ] Age and gender detection
- [ ] Save detected faces to files
- [ ] GUI interface with controls
- [ ] Video file input support
- [ ] Performance metrics display

## Dependencies

Create a `requirements.txt` file with:
```
opencv-python>=4.5.0
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Ensure all dependencies are correctly installed
3. Verify your webcam is working with other applications
4. Check OpenCV installation: `python -c "import cv2; print('OpenCV version:', cv2.__version__)"`

## Acknowledgments

- OpenCV community for the excellent computer vision library
- Haar Cascade algorithm developers
- Python community for making computer vision accessible

---

**Created by naakaarafr** | Last updated: August 2025
