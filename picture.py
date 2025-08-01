import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("tsumiki.png")
image = cv2.cvtColor(image , cv2.COLOR_RGB2BGR)

def image_show(image , title):
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()

image_show(image , 'tsumiki')