import os
import random

def getRandom():
    measurements = []
    with open(os.path.join(os.path.dirname(__file__), 'test.txt'), 'r') as f:
        x = f.readlines()
        for line in x:
            if "," in line:
                values = line.replace("\n", "").split(",")
                values = [float(i) for i in values]
                measurements.append(values)

    if len(measurements) > 0:
        return random.choice(measurements)

    return None