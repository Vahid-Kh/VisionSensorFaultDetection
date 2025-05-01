
from matplotlib import image
from matplotlib import pyplot as plt
import numpy as np

def plotRGBValues(meanR, meanG, meanB, moistureLevel, samples):
    x = np.linspace(0,samples,samples)
    plt.plot(x, meanR, color="red")
    plt.plot(x, meanG, color="green")
    plt.plot(x, meanB, color="blue")
    plt.plot(x, moistureLevel, color="black")
    plt.xlabel("Image number")
    plt.ylim([0, 270])
    plt.ylabel("RGB values")
    plt.savefig('MoistureLevel.png')
    plt.show()



def plotQuality(qualityPercentage, samples, plotNumber):
    x = np.linspace(0,samples,samples)
    plt.plot(x, qualityPercentage, color="black")
    plt.xlabel("Image number")
    plt.ylim([0, 100])
    plt.ylabel("Vapor Quality")
    plt.savefig('BubblePercentage' + str(plotNumber) + '.png')
    plt.show()
