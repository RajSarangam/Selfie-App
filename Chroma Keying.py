# Enter your code here
import cv2
import numpy as np

# Open the video file
video_path = "greenscreen-demo.mp4"  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read the first frame to select the green screen patch
ret, frame = cap.read()
if not ret:
    print("Error: Could not read frame.")
    cap.release()
    exit()

# Load the background replacement image
#bg_image = cv2.imread("background_image.jpg")  # Replace with your background image path
bg_image = cv2.imread("background.png")  # Replace with your background image path

# Resize the background image to match the video frame size
bg_image = cv2.resize(bg_image, (frame.shape[1], frame.shape[0]))

# Function to select the green background patch and determine its HSV range
def select_bg_color(image):
    patch = image.copy()
    cv2.putText(patch, "Select green area & press Enter", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    r = cv2.selectROI("Select Green Screen", patch, showCrosshair=True)
    patch = image[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    patch_hsv = cv2.cvtColor(patch, cv2.COLOR_BGR2HSV)
    h, _, _ = cv2.split(patch_hsv)

    cv2.destroyWindow("Select Green Screen")

    return int(np.mean(h))

# Get the background color from user selection
bg_color = select_bg_color(frame)

# Initial values for sliders
tolerance = 10  # Default value for green removal
blur_amount = 1  # Default value for Gaussian blur
green_cast_removal = 0  # Default value for green spill correction

# Function to update tolerance
def update_tolerance(val):
    global tolerance
    tolerance = val

# Function to update Gaussian blur
def update_blur(val):
    global blur_amount
    blur_amount = max(1, val * 2 + 1)  # Ensures only odd values

# Function to update Green Cast Removal
def update_green_cast(val):
    global green_cast_removal
    green_cast_removal = val

# Create a window with trackbars
cv2.namedWindow("Chroma Keying")
cv2.createTrackbar("Tolerance", "Chroma Keying", tolerance, 100, update_tolerance)
cv2.createTrackbar("Blur", "Chroma Keying", blur_amount // 2, 100, update_blur)
cv2.createTrackbar("Green Cast", "Chroma Keying", green_cast_removal, 100, update_green_cast)

# Process the video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize bg_image to ensure it matches current frame size in case of resolution change
    background = cv2.resize(bg_image, (frame.shape[1], frame.shape[0]))

    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range for green screen detection with adjustable tolerance
    lower_green = np.array([bg_color - tolerance, 50, 50])
    upper_green = np.array([bg_color + tolerance, 255, 255])

    # Create mask for green screen
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Invert mask for foreground
    mask_inv = cv2.bitwise_not(mask)

    # Extract foreground and background areas
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    bg = cv2.bitwise_and(background, background, mask=mask)

    # Improved Green Cast Removal
    if green_cast_removal > 0:
        green_channel = fg[:, :, 1]  # Extract green channel
        avg_green = np.mean(green_channel[mask_inv > 0])  # Get avg green value in foreground
        reduction_amount = (green_cast_removal / 100) * avg_green  # Scale removal dynamically
        fg[:, :, 1] = np.clip(fg[:, :, 1] - reduction_amount, 0, 255).astype(np.uint8)

    # Combine foreground and new background image
    final_output = cv2.add(fg, bg)

    # Apply Gaussian Blur
    final_output = cv2.GaussianBlur(final_output, (blur_amount, blur_amount), 0)

    # Display result
    cv2.imshow("Chroma Keying", final_output)

    # Exit when 'ESC' is pressed
    if cv2.waitKey(30) & 0xFF == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()