import os
import cv2
import pickle
import numpy as np

DATA_PATH = 'dataset'

images = []

for pokemon in sorted(os.listdir(DATA_PATH)):
    print("Currently stored " + str(len(images)) + " images")
    print("Getting : " + str(pokemon))
    for image in sorted(os.listdir(os.path.join(DATA_PATH, pokemon))):
        img = cv2.imread(os.path.join(DATA_PATH, pokemon, image))
        img = cv2.resize(img, (100, 100))
        images.append(np.array(img))
        # print("pokemon: " + str(pokemon))
        # print(image)
        # break
    # break

print(len(images))

file = open('pokemon_arrays.pkl', 'wb')
pickle.dump(images, file)
file.close()
