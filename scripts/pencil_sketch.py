import cv2
import matplotlib.pyplot as plt
from pathlib import Path

def convert_to_sketch(image_path):
    """Convert an image at the given path to pencil sketch"""
    # Read image
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at: {image_path}")
    
    # Convert to sketch
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blurred, scale=256)
    
    return sketch

if __name__ == "__main__":
    # Use raw string for Windows paths
    input_path = r"C:\dataprojects\pencil-sketch-project\images\dog.jpg"
    output_path = r"C:\dataprojects\pencil-sketch-project\images\dog_sketch.jpg"
    
    try:
        # Process image
        sketch = convert_to_sketch(input_path)
        
        # Display comparison
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(cv2.imread(input_path), cv2.COLOR_BGR2RGB))
        plt.title('Original Image')
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.imshow(sketch, cmap='gray')
        plt.title('Pencil Sketch')
        plt.axis('off')
        
        plt.show()
        
        # Save output
        cv2.imwrite(output_path, sketch)
        print(f"Sketch saved to: {output_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Please verify:")
        print(f"1. The file exists at {input_path}")
        print("2. You have write permissions to the output directory")