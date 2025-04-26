# Image to Pencil Sketch Converter

**Assignment Submission for**  
[![StrataScratch](https://platform.stratascratch.com/static/images/stratascratch-logo.svg)](https://platform.stratascratch.com/data-projects/image-pencil-sketch/your-solution)

A Python implementation to convert images to pencil sketches, completing the [StrataScratch Data Project Assignment](https://platform.stratascratch.com/data-projects/image-pencil-sketch).

## Assignment Requirements
✅ Convert RGB images to grayscale  
✅ Invert the grayscale image  
✅ Blend with Gaussian blur for sketch effect  
✅ Output resembles hand-drawn pencil sketch  

## Technical Implementation
```python
import cv2

def convert_to_sketch(image_path):
    gray = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    return cv2.divide(gray, 255 - blurred, scale=256)
