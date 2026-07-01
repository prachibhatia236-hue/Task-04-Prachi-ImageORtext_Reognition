# ==========================================
# Project 4: Image/Text Recognition (OCR)

import cv2
import pytesseract

# Set the path to Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read the image
image = cv2.imread("sample.png")

# Check whether image exists
if image is None:
    print("Error: sample.png not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Extract text using OCR
text = pytesseract.image_to_string(thresh)

# Display extracted text
print("\n===================================")
print("      RECOGNIZED TEXT")
print("===================================\n")
print(text)

# Show original image
cv2.imshow("Original Image", image)

# Show processed image
cv2.imshow("Processed Image", thresh)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()