from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


i = Image.open('images/dotndot.png')
iar = np.asarray(i)

plt.imshow(iar)
plt.show()
