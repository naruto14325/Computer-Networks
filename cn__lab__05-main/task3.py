import random
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')

def tcp_congestion_control(rounds, loss_prob):
    cwnd = 1
    ssthresh = 16
    cwnd_history = []
    phase = "Slow Start"
    
    for i in range(rounds):
        cwnd_history.append(cwnd)
        if random.random() < loss_prob:
            ssthresh = max(cwnd // 2, 1)
            cwnd = 1
            phase = "Slow Start"
        else:
            if phase == "Slow Start":
                cwnd *= 2
                if cwnd >= ssthresh:
                    phase = "Congestion Avoidance"
            elif phase == "Congestion Avoidance":
                cwnd += 1

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, rounds + 1), cwnd_history, marker='o', linestyle='-', color='b')
    plt.title("TCP Congestion Control Simulation")
    plt.xlabel("Transmission Round")
    plt.ylabel("Congestion Window (cwnd)")
    plt.grid(True)
    plt.savefig("cwnd-plot.png")
    print("Plot saved as 'cwnd-plot.png'.")
rounds = int(input("Enter number of transmission rounds: "))
loss_prob = float(input("Enter packet loss probability (0–1): "))
tcp_congestion_control(rounds, loss_prob)

