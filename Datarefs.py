import matplotlib.pyplot as plt
import xpc
from numpy import random

roll_electric_dref = "sim/cockpit2/gauges/indicators/roll_electric_deg_pilot"
pitch_electric_dref = "sim/cockpit2/gauges/indicators/pitch_electric_deg_pilot"

roll_dref = "sim/joystick/yoke_roll_ratio" # Yoke roll
pitch_dref = "sim/joystick/yoke_pitch_ratio" # Yoke pitch

def take_action():

    action1, action2 = random.randint(50, size=(2)) #big value so we can see the change

    with xpc.XPlaneConnect() as client:
        try:
            roll = client.getDREF(roll_electric_dref)[0]
            pitch = client.getDREF(pitch_electric_dref)[0]

            client.sendDREFs([roll_dref, pitch_dref],
                [roll+action1, pitch+action2])

        except:
            print("Error establishing connection to X-Plane.")
            print("Exiting...")
            return


def get_dref():

    with xpc.XPlaneConnect() as client:
        try:
            r = client.getDREF(roll_electric_dref)[0]
            p = client.getDREF(pitch_electric_dref)[0]
        except:
            print("Error establishing connection to X-Plane.")
            print("Exiting...")
            return

    return r,p


def ex():

    roll, pitch = [], []

    print("Connecting to X-plane")
    with xpc.XPlaneConnect() as client:
        try:
            for i in range(40):
                r, p = get_dref()
                roll.append(r)
                pitch.append(p)
                take_action()

        except:
            print("Error establishing connection to X-Plane.")
            print("Exiting...")
            return
    return roll, pitch


if __name__ == "__main__":
    roll, pitch = ex()
    print('roll', roll)
    print('pitch', pitch)

    plt.subplot(1, 2, 1)
    plt.plot(roll)
    plt.title('pitch and roll')
    plt.ylabel('roll value')

    plt.subplot(1, 2, 2)
    plt.plot(pitch)
    plt.ylabel('pitch value')

    plt.tight_layout()
    plt.show()
