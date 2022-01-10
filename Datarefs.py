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

    #     for i in range(100):
            
    #         posi = [37.524, -122.06899, 2500, 0,    0,   0,  1]
    #         client.sendPOSI(posi)
            

    #         # Set angle of attack, velocity, and orientation using the DATA command
    #         # print "Setting orientation"
    #         data = [\
    #             [18,   0, -998,   0, -998, -998, -998, -998, -998],\
    #             [ 3, 130,  130, 130,  130, -998, -998, -998, -998],\
    #             [16,   0,    0,   0, -998, -998, -998, -998, -998]\
    #             ]
    #         client.sendDATA(data)

    #         # Set control surfaces and throttle of the player aircraft using sendCTRL
    #         # print "Setting controls"
    #         ctrl = [0.0, 0.0, 0.0, 0.8]
    #         client.sendCTRL(ctrl)

    #         # # Pause the sim
    #         # print "Pausing"
    #         # client.pauseSim(True)
    #         # sleep(2)

    #         # # Toggle pause state to resume
    #         # print "Resuming"
    #         # client.pauseSim(False)

    #         # Stow landing gear using a dataref
    #         # print "Stowing gear"
    #         # gear_dref = "sim/cockpit/switches/gear_handle_status"
    #         # client.sendDREF(gear_dref, 0)


    #         # Let the sim run for a bit.
    #         # sleep(4)

    #         # Make sure gear was stowed successfully
    #         # gear_status = client.getDREF(gear_dref)
    #         roll.append(client.getDREF(roll_electric_dref)[0])
    #         pitch.append(client.getDREF(pitch_electric_dref)[0])

    #         # if gear_status[0] == 0:
    #         #     print "Gear stowed"
    #         # else:
    #         #     print "Error stowing gear"

    # print ("End of Python client example")
    # raw_input("Press any key to exit...")


    # return roll, pitch
    # # print(roll)
    # # print(pitch)

if __name__ == "__main__":
    roll, pitch = ex()
    print('roll', roll)
    print('pitch', pitch)

    # plt.subplot(1, 2, 1)
    # plt.plot(roll)
    # plt.title('pitch and roll')
    # plt.ylabel('roll value')

    # plt.subplot(1, 2, 2)
    # plt.plot(pitch)
    # plt.ylabel('pitch value')

    # plt.tight_layout()
    # plt.show()
