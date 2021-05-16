# Parse the trajnet data into usable data

import json
import matplotlib.pyplot as plt
import numpy as np


dataset = {}
scenes = {}

path = "data/TrajNet++/train/train/real_data/biwi_hotel.ndjson"
f = open(path, 'r')
for line in f:
    data = json.loads(line)
    if "track" in data.keys():
        pedestrian_id = data["track"]["p"]
        x = data["track"]["x"]
        y = data["track"]["y"]
        if pedestrian_id in dataset.keys():
            dataset[pedestrian_id].append( (x, y) )
        else:
            dataset[pedestrian_id] = [ (x, y) ]

    elif "scene" in data.keys():
        pedestiran_id = data["scene"]["p"]

for key in dataset.keys():
    dataset[key] = np.array(dataset[key])


print(dataset[20])
plt.scatter(dataset[20][:,0], dataset[20][:,1])
plt.show()


