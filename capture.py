import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def capture_image(filename):
    
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    print(f"Press Enter to capture {filename}...")
    
    input()
    
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        cap.release()
        return None
    
    cv2.imwrite(filename, frame)
    print(f"Image saved as '{filename}'.")

    cap.release()
    cv2.destroyAllWindows()
    return frame

def compare_images(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    score, _ = ssim(gray1, gray2, full=True)
    return score

def main():
    print("Ready to capture the first image.")
    img1 = capture_image("image1.jpg")
    if img1 is None:
        return
    
    print("Ready to capture the second image.")
    img2 = capture_image("image2.jpg")
    if img2 is None:
        return

    score = compare_images(img1, img2)
    print(f"Image similarity score: {score:.2f}")

    threshold = 0.70
    if score > threshold:
        print("The images are similar.")
    else:
        print("The images are different.")

if __name__ == "__main__":
    main()
