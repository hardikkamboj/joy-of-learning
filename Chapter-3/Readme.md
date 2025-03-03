# Chapter-3: Intensity Transformations and Spatial Filtering

- [3.1 Basics of Intensity Transformation and Spatial Filtering](https://youtu.be/VN6Mf-teABM?list=PL8J6S0Vzbb2sDU7IXnLW6eNl-NgVRxOjY)
- [3.2 Some Basic Intensity Transformation Functions](https://youtu.be/5Q0PaLiSUDg?list=PL8J6S0Vzbb2sDU7IXnLW6eNl-NgVRxOjY)
- [3.2 Bit Plane Slicing (Digital Image Processing)](https://youtu.be/5d_U-A3c3Zc?list=PL8J6S0Vzbb2sDU7IXnLW6eNl-NgVRxOjY)
- [3.3 Histogram Equalisation](https://youtu.be/rchZ4plRYMI?list=PL8J6S0Vzbb2sDU7IXnLW6eNl-NgVRxOjY)


# Some Findings - 

1. ## Difference between Box blurring and Gaussian blurring:
   Although, box blurring and Gaussian blurring are both low pass filters used to blur an image. There are some difference in the two approaches. Both of them are averaging the values. In box blurring, all pixel values are given equal weight for averaging. Gaussian blurring performs a weighted average in which the central pixels gets the maximum weight, and the weight decreases uniformly as one moves away from the center.

   The other difference is that, in box blurring as the size of the kernel increases, the blurring also increases. This is not true for Gaussian blurring. For a given value of sigma, the blurring effect increases upto a certain kernel size, after that there is no effect in increasing the kernel size. This can be experimented using [this script](box_and_gaussian_blurring_difference.py). 
   

# Exercises
- [Problem - 1](https://youtu.be/U0rKkpJVjvc?list=PL8J6S0Vzbb2srOVcsUrKuXOONNLq8o6co) (video)
- [Problem - 2](https://youtu.be/3Pk5Da7iyr4?list=PL8J6S0Vzbb2srOVcsUrKuXOONNLq8o6co) (video)
- [Problem - 3](Exercises/3_3.ipynb) (notebook)
- [Problem - 4](Exercises/3_4.ipynb) (notebook)
- [Problem - 5](Exercises/3_5.ipynb) (notebook)
