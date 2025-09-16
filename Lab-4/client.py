import cv2
import socket
import numpy as np

# --- Configuration ---
LISTEN_IP = '127.0.0.1' # IP address to listen on (localhost)
LISTEN_PORT = 9999      # Port to bind the socket to
BUFFER_SIZE = 2**16     # Buffer size for receiving data (65536 bytes)

def main():
    """
    Receives video frame chunks over UDP, reassembles, and displays them.
    """
    # 1. Create a UDP socket and bind to the listening port
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind((LISTEN_IP, LISTEN_PORT))
    print(f"UDP Client listening on {LISTEN_IP}:{LISTEN_PORT}")

    frame_data = b"" # Buffer to store incoming frame chunks

    # 2. Receive packets continuously
    while True:
        try:
            # Receive a packet from the server
            packet, _ = client_socket.recvfrom(BUFFER_SIZE)

            # Check for the end-of-stream signal
            if packet == b'END_OF_STREAM':
                print("End of stream signal received. Exiting.")
                break

            # Extract the payload and the marker bit
            payload = packet[:-1]
            marker = packet[-1]

            # 3. Append data until the last packet of a frame is received
            frame_data += payload
            
            if marker == 1: # If it's the last packet of the frame
                # 4. Decode the complete frame data and display it
                frame = cv2.imdecode(np.frombuffer(frame_data, dtype=np.uint8), cv2.IMREAD_COLOR)
                
                if frame is not None:
                    cv2.imshow("Received Video Stream", frame)
                
                # Reset buffer for the next frame
                frame_data = b""

            # 5. Stop when the user presses 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        except Exception as e:
            print(f"An error occurred: {e}")
            break
            
    # Clean up
    print("Closing client...")
    client_socket.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()