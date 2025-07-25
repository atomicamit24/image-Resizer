import cv2
import os

# Ask the user for the image file name and the new size
filename = input("Enter image filename (with extension, e.g., 'photo.jpg'): ")
width = int(input("Enter new width (pixels): "))
height = int(input("Enter new height (pixels): "))

# Print the current working directory to help locate your image file
print("Working directory is:", os.getcwd())

# Check if the file exists
if not os.path.exists(filename):
    print(f"File not found: {filename}")
else:
    # Try loading the image
    image = cv2.imread(filename)
    if image is None:
        print("Image found, but failed to load. The format may not be supported or the file might be corrupted.")
    else:
        print("Image loaded successfully.")

        # Resize the image
        resized_image = cv2.resize(image, (width, height))

        # Save the resized image
        output_name = "resized_" + filename
        cv2.imwrite(output_name, resized_image)
        print(f"Image resized and saved as {output_name}")

        # Display the resized image (window closes when any key is pressed)
        cv2.imshow("Resized Image", resized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
