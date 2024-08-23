import cv2
import face_recognition
import time

def load_known_faces():
    # Load a known face image and encode it
    known_image = face_recognition.load_image_file("YOUR_SAMPLE_PHOTO_HERE")
    known_encoding = face_recognition.face_encodings(known_image)[0]
    return [known_encoding]

def recognize_face():
    # Load known face encodings
    known_face_encodings = load_known_faces()

    # Open the camera
    video_capture = cv2.VideoCapture(0)

    # Set a timer duration (5 seconds)
    start_time = time.time()
    timer_duration = 5  # in seconds

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Loop over each face found in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            
            if True in matches:
                # If a match is found, proceed with the further code
                print("Face recognized! Proceeding...")
                video_capture.release()
                cv2.destroyAllWindows()
                return True

        # Check if 5 seconds have elapsed
        elapsed_time = time.time() - start_time
        if elapsed_time > timer_duration:
            print("No face detected within 5 seconds.")
            break

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    video_capture.release()
    cv2.destroyAllWindows()

    return False

# Main function
if __name__ == "__main__":
    if recognize_face():
        # Proceed with further code if the face is recognized
        print("Welcome Sir")
    else:
        print("Face not recognized.")