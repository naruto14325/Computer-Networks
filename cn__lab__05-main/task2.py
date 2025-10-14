import random
import time
def go_back_n_arq(total_frames, window_size, loss_prob, timeout):
    base = 0
    next_frame = 0
    while base < total_frames:
        end = min(base + window_size, total_frames)
        print(f"Sending frames {base} to {end - 1}")
        frame_lost = None
        for frame in range(base, end):
            if random.random() < loss_prob:
                frame_lost = frame
                print(f"Frame {frame} lost, retransmitting frames {frame} to {end - 1}...")
                time.sleep(timeout)
                break
        if frame_lost is not None:
            next_frame = frame_lost
            continue
        if random.random() < loss_prob:
            print(f"ACK lost, retransmitting frames {base} to {end - 1}...")
            time.sleep(timeout)
            continue
        else:
            ack = end - 1
            print(f"ACK {ack} received")
            base = end
            print(f"Window slides to {base} to {min(base + window_size - 1, total_frames - 1)}")
            time.sleep(1)
tf = int(input("Enter total number of frames: "))
ws = int(input("Enter window size (N): "))
lp = float(input("Enter loss probability (0–1): "))
t = float(input('Timeout (seconds): '))
go_back_n_arq(tf, ws, lp,t)
