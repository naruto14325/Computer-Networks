import random
import time
def stop_and_wait_arq(num_frames, loss_prob, timeout):
    for frame in range(num_frames):
        acknowledged = False
        while not acknowledged:
            print(f"Sending Frame {frame}")
            if random.random() < loss_prob:
                print(f"Frame {frame} lost, retransmitting...")
                time.sleep(timeout)
                continue
            time.sleep(1)
            if random.random() < loss_prob:
                print(f"ACK {frame} lost, retransmitting frame...")
                time.sleep(timeout)
                continue
            else:
                print(f"ACK {frame} received")
                acknowledged = True
n = int(input('Number of frames: '))
l = float(input('Loss probability (0–1): '))
t = float(input('Timeout (seconds): '))
stop_and_wait_arq(num_frames=n, loss_prob=l, timeout=t)

