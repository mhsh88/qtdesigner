import numpy as np
from math import exp
import math
from scipy.optimize import fsolve



class Gas():
    T = 300
    P = 5000
    R = 8.314510  # kJ/(kmol.K)

    tableD2 = [[1.0, 'nitrogen', 28.0135, 99.73778, 0.4479153, 0.027815, 0.0, 0.0, 0.0, 0.0],
               [2.0, 'carbon dioxide', 44.01, 241.9606, 0.4557489, 0.189065, 0.69, 0.0, 0.0, 0.0],
               [3.0, 'methane', 16.043, 151.3183, 0.4619255, 0.0, 0.0, 0.0, 0.0, 0.0],
               [4.0, 'ethane', 30.07, 244.1667, 0.5279209, 0.0793, 0.0, 0.0, 0.0, 0.0],
               [5.0, 'propane', 44.097, 298.1183, 0.583749, 0.141239, 0.0, 0.0, 0.0, 0.0],
               [6.0, 'n-butane', 58.123, 337.6389, 0.6341423, 0.281835, 0.0, 0.0, 0.0, 0.0],
               [7.0, 'iso-butane', 58.123, 324.0689, 0.6406937, 0.256692, 0.0, 0.0, 0.0, 0.0],
               [8.0, 'n-pentane', 72.15, 370.6823, 0.6798307, 0.366911, 0.0, 0.0, 0.0, 0.0],
               [9.0, 'iso-pentane', 72.15, 365.5999, 0.6738577, 0.332267, 0.0, 0.0, 0.0, 0.0],
               [10.0, 'n-hexane', 86.177, 402.636293, 0.7175118, 0.289731, 0.0, 0.0, 0.0, 0.0],
               [11.0, 'n-heptane', 100.204, 427.72263, 0.7525189, 0.337542, 0.0, 0.0, 0.0, 0.0],
               [12.0, 'n-octane', 114.231, 450.325022, 0.784955, 0.383381, 0.0, 0.0, 0.0, 0.0],
               [13.0, 'n-nonane', 128.258, 470.840891, 0.8152731, 0.427354, 0.0, 0.0, 0.0, 0.0],
               [14.0, 'n-decane', 142.285, 489.558373, 0.8437826, 0.469659, 0.0, 0.0, 0.0, 0.0],
               [15.0, 'hydrogen', 2.0159, 26.95794, 0.3514916, 0.034369, 0.0, 1.0, 0.0, 0.0],
               [16.0, 'oxygen', 31.9988, 122.7667, 0.4186954, 0.021, 0.0, 0.0, 0.0, 0.0],
               [17.0, 'carbon monoxide', 28.01, 105.5348, 0.4533894, 0.038953, 0.0, 0.0, 0.0, 0.0],
               [18.0, 'water', 18.0153, 514.0156, 0.3825868, 0.3325, 1.06775, 0.0, 1.5822, 1.0],
               [19.0, 'hydrogen sulfide', 34.082, 296.355, 0.4618263, 0.0885, 0.633276, 0.0, 0.39, 0.0],
               [20.0, 'helium', 4.0026, 2.610111, 0.3589888, 0.0, 0.0, 0.0, 0.0, 0.0],
               [21.0, 'argon', 39.948, 119.6299, 0.4216551, 0.0, 0.0, 0.0, 0.0, 0.0]]
    tableD1 = [[1.0, 0.1538326, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [2.0, 1.341953, 1.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0],
               [3.0, -2.998583, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [4.0, -0.04831228, 1.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0],
               [5.0, 0.3757965, 1.0, 0.0, 0.0, -0.5, 1.0, 0.0, 0.0, 0.0, 0.0],
               [6.0, -1.589575, 1.0, 0.0, 0.0, 4.5, 1.0, 0.0, 0.0, 0.0, 0.0],
               [7.0, -0.05358847, 1.0, 0.0, 0.0, 0.5, 0.0, 1.0, 0.0, 0.0, 0.0],
               [8.0, 0.88659463, 1.0, 0.0, 0.0, 7.5, 0.0, 0.0, 0.0, 1.0, 0.0],
               [9.0, -0.71023704, 1.0, 0.0, 0.0, 9.5, 0.0, 0.0, 0.0, 1.0, 0.0],
               [10.0, -1.471722, 1.0, 0.0, 0.0, 6.0, 0.0, 0.0, 0.0, 0.0, 1.0],
               [11.0, 1.32185035, 1.0, 0.0, 0.0, 12.0, 0.0, 0.0, 0.0, 0.0, 1.0],
               [12.0, -0.78665925, 1.0, 0.0, 0.0, 12.5, 0.0, 0.0, 0.0, 0.0, 1.0],
               [13.0, 2.2912900000000003e-09, 1.0, 1.0, 3.0, -6.0, 0.0, 0.0, 1.0, 0.0, 0.0],
               [14.0, 0.1576724, 1.0, 1.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [15.0, -0.4363864, 1.0, 1.0, 2.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [16.0, -0.04408159, 1.0, 1.0, 2.0, 2.0, 0.0, 1.0, 0.0, 0.0, 0.0],
               [17.0, -0.003433888, 1.0, 1.0, 4.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [18.0, 0.03205905, 1.0, 1.0, 4.0, 11.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [19.0, 0.02487355, 2.0, 0.0, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0],
               [20.0, 0.07332279, 2.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0],
               [21.0, -0.001600573, 2.0, 1.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [22.0, 0.6424706, 2.0, 1.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [23.0, -0.4162601, 2.0, 1.0, 2.0, 6.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [24.0, -0.06689957, 2.0, 1.0, 4.0, 21.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [25.0, 0.2791795, 2.0, 1.0, 4.0, 23.0, 1.0, 0.0, 0.0, 0.0, 0.0],
               [26.0, -0.6966051, 2.0, 1.0, 4.0, 22.0, 0.0, 1.0, 0.0, 0.0, 0.0],
               [27.0, -0.002860589, 2.0, 1.0, 4.0, -1.0, 0.0, 0.0, 1.0, 0.0, 0.0],
               [28.0, -0.008098836, 3.0, 0.0, 0.0, -0.5, 0.0, 1.0, 0.0, 0.0, 0.0],
               [29.0, 3.150547, 3.0, 1.0, 1.0, 7.0, 1.0, 0.0, 0.0, 0.0, 0.0],
               [30.0, 0.007224479, 3.0, 1.0, 1.0, -1.0, 0.0, 0.0, 1.0, 0.0, 0.0],
               [31.0, -0.7057529, 3.0, 1.0, 2.0, 6.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [32.0, 0.5349792, 3.0, 1.0, 2.0, 4.0, 1.0, 0.0, 0.0, 0.0, 0.0],
               [33.0, -0.07931491, 3.0, 1.0, 3.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
               [34.0, -1.418465, 3.0, 1.0, 3.0, 9.0, 1.0, 0.0, 0.0, 0.0, 0.0],
               [35.0, -5.999050000000001e-17, 3.0, 1.0, 4.0, -3.0, 0.0, 0.0, 1.0, 0.0, 0.0],
               [36.0, 0.1058402, 3.0, 1.0, 4.0, 21.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [37.0, 0.03431729, 3.0, 1.0, 4.0, 8.0, 0.0, 1.0, 0.0, 0.0, 0.0],
               [38.0, -0.007022847, 4.0, 0.0, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0, 0.0],
               [39.0, 0.02495587, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [40.0, 0.04296818, 4.0, 1.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [41.0, 0.7465453, 4.0, 1.0, 2.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [42.0, -0.2919613, 4.0, 1.0, 2.0, 9.0, 0.0, 1.0, 0.0, 0.0, 0.0],
               [43.0, 7.294616, 4.0, 1.0, 4.0, 22.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [44.0, -9.936757, 4.0, 1.0, 4.0, 23.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [45.0, -0.005399808, 5.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [46.0, -0.2432567, 5.0, 1.0, 2.0, 9.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [47.0, 0.04987016, 5.0, 1.0, 2.0, 3.0, 0.0, 1.0, 0.0, 0.0, 0.0],
               [48.0, 0.003733797, 5.0, 1.0, 4.0, 8.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [49.0, 1.874951, 5.0, 1.0, 4.0, 23.0, 0.0, 1.0, 0.0, 0.0, 0.0],
               [50.0, 0.002168144, 6.0, 0.0, 0.0, 1.5, 0.0, 0.0, 0.0, 0.0, 0.0],
               [51.0, -0.6587164, 6.0, 1.0, 2.0, 5.0, 1.0, 0.0, 0.0, 0.0, 0.0],
               [52.0, 0.000205518, 7.0, 0.0, 0.0, -0.5, 0.0, 1.0, 0.0, 0.0, 0.0],
               [53.0, 0.009776195, 7.0, 1.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [54.0, -0.02048708, 8.0, 1.0, 1.0, 7.0, 1.0, 0.0, 0.0, 0.0, 0.0],
               [55.0, 0.01557322, 8.0, 1.0, 2.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [56.0, 0.006862415, 8.0, 1.0, 2.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
               [57.0, -0.001226752, 9.0, 1.0, 2.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
               [58.0, 0.002850908, 9.0, 1.0, 2.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]]

    tableB1 = [
        [1.0, 'nitrogen', 23.2653, -2801.72907, 3.50031, 0.13732, 662.738, -0.1466, 680.562, 0.90066, 1740.06, 0.0,
         0.0],
        [2.0, 'carbon dioxide', 26.35604, -4902.17152, 3.50002, 2.04452, 919.306, -1.06044, 865.07, 2.03366, 483.553,
         0.01393, 341.109],
        [3.0, 'methane', 35.53603, -15999.69151, 4.00088, 0.76315, 820.659, 0.0046, 178.41, 8.74432, 1062.82, -4.46921,
         1090.53],
        [4.0, 'ethane', 42.42766, -23639.65301, 4.00263, 4.33939, 559.314, 1.23722, 223.284, 13.1974, 1031.38, -6.01989,
         1071.29],
        [5.0, 'propane', 50.40669, -31236.63551, 4.02939, 6.60569, 479.856, 3.197, 200.893, 19.1921, 955.312, -8.37267,
         1027.29],
        [6.0, 'n-butane', 42.22997, -38957.80933, 4.33944, 9.44893, 468.27, 6.89406, 183.636, 24.4618, 1914.1, 14.7824,
         903.185],
        [7.0, 'iso-butane', 39.9994, -38525.50276, 4.06714, 8.97575, 438.27, 5.25156, 198.018, 25.1423, 1905.02,
         16.1388, 893.765],
        [8.0, 'n-pentane', 48.37597, -45215.83, 4.0, 8.95043, 178.67, 21.836, 840.538, 33.4032, 1774.25, 0.0, 0.0],
        [9.0, 'iso-pentane', 48.86978, -51198.30946, 4.0, 11.7618, 292.503, 20.1101, 910.237, 33.1688, 1919.37, 0.0,
         0.0],
        [10.0, 'n-hexane', 52.69477, -52746.83318, 4.0, 11.6977, 182.326, 26.8142, 859.207, 38.6164, 1826.59, 0.0, 0.0],
        [11.0, 'n-heptane', 57.77391, -57104.81056, 4.0, 13.7266, 169.789, 30.4707, 836.195, 43.5561, 1760.46, 0.0,
         0.0],
        [12.0, 'n-octane', 62.95591, -60546.76385, 4.0, 15.6865, 158.922, 33.8029, 815.064, 48.1731, 1693.07, 0.0, 0.0],
        [13.0, 'n-nonane', 67.79407, -66600.12837, 4.0, 18.0241, 156.854, 38.1235, 814.882, 53.3415, 1693.79, 0.0, 0.0],
        [14.0, 'n-decane', 71.63669, -74131.45483, 4.0, 21.0069, 164.947, 43.4931, 836.264, 58.3657, 1750.24, 0.0, 0.0],
        [15.0, 'hydrogen', 18.7728, -5836.9437, 2.47906, 0.95806, 228.734, 0.45444, 326.843, 1.56039, 1651.71, -1.3756,
         1671.69],
        [16.0, 'oxygen', 22.49931, -2318.32269, 3.50146, 1.07558, 2235.71, 1.01334, 1116.69, 0.0, 0.0, 0.0, 0.0],
        [17.0, 'carbon monoxide', 23.15547, -2635.24412, 3.50055, 1.02865, 1550.45, 0.00493, 704.525, 0.0, 0.0, 0.0,
         0.0],
        [18.0, 'water', 27.27642, -7766.73308, 4.00392, 0.01059, 268.795, 0.98763, 1141.41, 3.06904, 2507.37, 0.0, 0.0],
        [19.0, 'hydrogen sulfide', 27.28069, -6069.03587, 4.0, 3.11942, 1833.63, 1.00243, 847.181, 0.0, 0.0, 0.0, 0.0],
        [20.0, 'helium', 15.74399, -745.375, 2.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [21.0, 'argon', 15.74399, -745.375, 2.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]


    E_star_ij = np.array([[1.0, 1.02274, 0.97164, 0.97012, 0.945939, 0.973384, 0.946914, 0.94552, 0.95934, 1.0, 1.0,
                           1.0, 1.0, 1.0, 1.08632, 1.021, 1.00571, 0.746954, 0.902271, 1.0, 1.0],
                          [1.02274, 1.0, 0.960644, 0.925053, 0.960237, 0.897362, 0.906849, 0.859764, 0.726255, 0.855134,
                           0.831229, 0.80831, 0.786323, 0.765171, 1.28179, 1.0, 1.5, 0.849408, 0.955052, 1.0, 1.0],
                          [0.97164, 0.960644, 1.0, 1.0, 0.994635, 0.989844, 1.01953, 0.999268, 1.00235, 1.107274,
                           0.88088, 0.880973, 0.881067, 0.881161, 1.17052, 1.0, 0.990126, 0.708218, 0.931484, 1.0, 1.0],
                          [0.97012, 0.925053, 1.0, 1.0, 1.02256, 1.01306, 1.0, 1.00532, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.16446, 1.0, 1.0, 0.693168, 0.946871, 1.0, 1.0],
                          [0.945939, 0.960237, 0.994635, 1.02256, 1.0, 1.0049, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.034787, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [0.973384, 0.897362, 0.989844, 1.01306, 1.0049, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [0.946914, 0.906849, 1.01953, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.3, 1.0,
                           1.0, 1.0, 1.0, 1.0, 1.0],
                          [0.94552, 0.859764, 0.999268, 1.00532, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [0.95934, 0.726255, 1.00235, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.0, 1.0, 1.0, 1.0, 1.0],
                          [1.0, 0.855134, 1.107274, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.0, 1.0, 1.008692, 1.0, 1.0],
                          [1.0, 0.831229, 0.88088, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.0, 1.010126, 1.0, 1.0],
                          [1.0, 0.80831, 0.880973, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.0, 1.011501, 1.0, 1.0],
                          [1.0, 0.786323, 0.881067, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.0, 1.0, 1.012821, 1.0, 1.0],
                          [1.0, 0.765171, 0.881161, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.0, 1.0, 1.014089, 1.0, 1.0],
                          [1.08632, 1.28179, 1.17052, 1.16446, 1.034787, 1.3, 1.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.0, 1.0, 1.1, 1.0, 1.0, 1.0, 1.0],
                          [1.021, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.0, 1.0, 1.0],
                          [1.00571, 1.5, 0.990126, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1, 1.0, 1.0,
                           1.0, 1.0, 1.0, 1.0],
                          [0.746954, 0.849408, 0.708218, 0.693168, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [0.902271, 0.955052, 0.931484, 0.946871, 1.0, 1.0, 1.0, 1.0, 1.0, 1.008692, 1.010126,
                           1.011501, 1.012821, 1.014089, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.0, 1.0, 1.0],
                          [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                           1.0, 1.0, 1.0]])

    G_star_ij = np.array(
        [[1.0, 0.982746, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [0.982746, 1.0, 0.807653, 0.370296, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.67309,
          1.0, 1.0, 1.0],
         [1.0, 0.807653, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.95731, 1.0, 1.0, 1.0, 1.0, 1.0,
          1.0],
         [1.0, 0.370296, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.95731, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.67309, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
         [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]])
    V_ij = np.array([[1.0, 0.835058, 0.886106, 0.816431, 0.915502, 0.993556, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      0.408838, 1.0, 1.0, 1.0, 0.993476, 1.0, 1.0],
                     [0.835058, 1.0, 0.963827, 0.96987, 1.0, 1.0, 1.0, 1.0, 1.0, 1.066638, 1.077634, 1.088178, 1.098291,
                      1.108021, 1.0, 1.0, 0.9, 1.0, 1.04529, 1.0, 1.0],
                     [0.886106, 0.963827, 1.0, 1.0, 0.990877, 0.992291, 1.0, 1.00367, 1.0, 1.302576, 1.191904, 1.205769,
                      1.219634, 1.233498, 1.15639, 1.0, 1.0, 1.0, 0.736833, 1.0, 1.0],
                     [0.816431, 0.96987, 1.0, 1.0, 1.065173, 1.25, 1.25, 1.25, 1.25, 1.0, 1.0, 1.0, 1.0, 1.0, 1.61666,
                      1.0, 1.0, 1.0, 0.971926, 1.0, 1.0],
                     [0.915502, 1.0, 0.990877, 1.065173, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0, 1.0, 1.0, 1.0],
                     [0.993556, 1.0, 0.992291, 1.25, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0, 1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.25, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0],
                     [1.0, 1.0, 1.00367, 1.25, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.25, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0],
                     [1.0, 1.066638, 1.302576, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.028973, 1.0, 1.0],
                     [1.0, 1.077634, 1.191904, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.033754, 1.0, 1.0],
                     [1.0, 1.088178, 1.205769, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.038338, 1.0, 1.0],
                     [1.0, 1.098291, 1.219634, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.042735, 1.0, 1.0],
                     [1.0, 1.108021, 1.233498, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.046966, 1.0, 1.0],
                     [0.408838, 1.0, 1.15639, 1.61666, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0, 1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0],
                     [1.0, 0.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0],
                     [0.993476, 1.04529, 0.736833, 0.971926, 1.0, 1.0, 1.0, 1.0, 1.0, 1.028973, 1.033754, 1.038338,
                      1.042735, 1.046966, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0]])

    K_ij = np.array([[1.0, 0.982361, 1.00363, 1.00796, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.03227, 1.0,
                      1.0, 1.0, 0.942596, 1.0, 1.0],
                     [0.982361, 1.0, 0.995933, 1.00851, 1.0, 1.0, 1.0, 1.0, 1.0, 0.910183, 0.895362, 0.881152, 0.86752,
                      0.854406, 1.0, 1.0, 1.0, 1.0, 1.00779, 1.0, 1.0],
                     [1.00363, 0.995933, 1.0, 1.0, 1.007619, 0.997596, 1.0, 1.002529, 1.0, 0.982962, 0.983565, 0.982707,
                      0.981849, 0.980991, 1.02326, 1.0, 1.0, 1.0, 1.00008, 1.0, 1.0],
                     [1.00796, 1.00851, 1.0, 1.0, 0.986893, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.02034, 1.0,
                      1.0, 1.0, 0.999969, 1.0, 1.0],
                     [1.0, 1.0, 1.007619, 0.986893, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0, 1.0, 1.0],
                     [1.0, 1.0, 0.997596, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0],
                     [1.0, 1.0, 1.002529, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0],
                     [1.0, 0.910183, 0.982962, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 0.96813, 1.0, 1.0],
                     [1.0, 0.895362, 0.983565, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 0.96287, 1.0, 1.0],
                     [1.0, 0.881152, 0.982707, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 0.957828, 1.0, 1.0],
                     [1.0, 0.86752, 0.981849, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      0.952441, 1.0, 1.0],
                     [1.0, 0.854406, 0.980991, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 0.948338, 1.0, 1.0],
                     [1.03227, 1.0, 1.02326, 1.02034, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0, 1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0],
                     [0.942596, 1.00779, 1.00008, 0.999969, 1.0, 1.0, 1.0, 1.0, 1.0, 0.96813, 0.96287, 0.957828,
                      0.952441, 0.948338, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0],
                     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0, 1.0]])
    component = [[1.0, 'nitrogen', 0.057, 0.057, 4.22, 4.97, 0.003, 0.057],
                 [2.0, 'carbon dioxide', 0.076, 0.076, 0.39, 0.87, 0.006, 0.076],
                 [3.0, 'methane', 0.812, 0.812, 88.72, 90.65, 0.965, 0.812],
                 [4.0, 'ethane', 0.043, 0.043, 2.94, 3.64, 0.018, 0.043],
                 [5.0, 'propane', 0.009, 0.009, 0.77, 1.29, 0.0045, 0.009],
                 [6.0, 'n-butane', 0.0015, 0.0015, 0.17, 0.255, 0.001, 0.0015],
                 [7.0, 'iso-butane', 0.0015, 0.0015, 0.17, 0.255, 0.001, 0.0015],
                 [8.0, 'n-pentane', 0.0, 0.0, 0.06999999999999999, 0.09000000000000001, 0.0003, 0.0],
                 [9.0, 'iso-pentane', 0.0, 0.0, 0.06999999999999999, 0.09000000000000001, 0.0005, 0.0],
                 [10.0, 'n-hexane', 0.0, 0.0, 0.06999999999999999, 0.09000000000000001, 0.0007, 0.0],
                 [11.0, 'n-heptane', 0.0, 0.0, '', '', '', 0.0], [12.0, 'n-octane', 0.0, 0.0, '', '', '', 0.0],
                 [13.0, 'n-nonane', 0.0, 0.0, '', '', '', 0.0], [14.0, 'n-decane', 0.0, 0.0, '', '', '', 0.0],
                 [15.0, 'hydrogen', 0.0, 0.0, '', '', '', 0.0], [16.0, 'oxygen', 0.0, 0.0, '', '', '', 0.0],
                 [17.0, 'carbon monoxide', 0.0, 0.0, '', '', '', 0.0], [18.0, 'water', 0.0, 0.0, '', '', '', 0.0],
                 [19.0, 'hydrogen sulfide', 0.0, 0.0, '', '', '', 0.0], [20.0, 'helium', 0.0, 0.0, '', '', '', 0.0],
                 [21.0, 'argon', 0.0, 0.0, '', '', '', 0.0]]


    def __init__(self):
        componentMin = np.array(self.returnCol(self.component, 2))
        componentMax = np.array(self.returnCol(self.component, 3))
        self.component = (componentMin + componentMax) / 2

        self.Uinit()

    def Uinit(self):

        T = self.T
        returnCol = self.returnCol
        tableD1 = self.tableD1
        tableD2 = self.tableD2
        tableB1 = self.tableB1
        E_star_ij = self.E_star_ij
        G_star_ij = self.G_star_ij
        V_ij = self.V_ij
        K_ij = self.K_ij
        component = self.component

        a_n = np.array(returnCol(tableD1, 1))
        self.b_n = np.array(returnCol(tableD1, 2))
        b_n = self.b_n
        self.c_n = np.array(returnCol(tableD1, 3))
        c_n = self.c_n
        self.k_n = np.array(returnCol(tableD1, 4))
        k_n = self.k_n
        self.u_n = np.array(returnCol(tableD1, 5))
        u_n = self.u_n
        g_n = np.array(returnCol(tableD1, 6))
        q_n = np.array(returnCol(tableD1, 7))
        f_n = np.array(returnCol(tableD1, 8))
        s_n = np.array(returnCol(tableD1, 9))
        w_n = np.array(returnCol(tableD1, 10))
        # items.amount()

        Xi = component / np.sum(component)
        N = len(component)

        M_i = np.array(returnCol(tableD2, 2))
        E_i = np.array(returnCol(tableD2, 3))
        K_i = np.array(returnCol(tableD2, 4))
        G_i = np.array(returnCol(tableD2, 5))
        Q_i = np.array(returnCol(tableD2, 6))
        F_i = np.array(returnCol(tableD2, 7))
        S_i = np.array(returnCol(tableD2, 8))
        W_i = np.array(returnCol(tableD2, 9))

        Ao1_i = np.array(returnCol(tableB1, 2))
        Ao2_i = np.array(returnCol(tableB1, 3))
        Bo_i = np.array(returnCol(tableB1, 4))
        Co_i = np.array(returnCol(tableB1, 5))
        Do_i = np.array(returnCol(tableB1, 6))
        Eo_i = np.array(returnCol(tableB1, 7))
        Fo_i = np.array(returnCol(tableB1, 8))
        Go_i = np.array(returnCol(tableB1, 9))
        Ho_i = np.array(returnCol(tableB1, 10))
        Io_i = np.array(returnCol(tableB1, 11))
        Jo_i = np.array(returnCol(tableB1, 12))

        M = np.sum(np.multiply(Xi, M_i))
        self.M = M
        F = np.sum(np.multiply(Xi, F_i))
        Q = np.sum(np.multiply(Xi, Q_i))

        G = []

        for i in range(20):
            _G = []
            for j in range(i + 1, 21):
                _G.append(Xi[i] * Xi[j] * (G_star_ij[i][j] - 1) * (G_i[i] + G_i[j]))
            G.append(_G)
        G = np.sum(np.multiply(Xi, G_i)) + np.sum(np.sum(np.array(G)))
        V = []
        for i in range(20):
            _V = []
            for j in range(i + 1, 21):
                _V.append(Xi[i] * Xi[j] * (V_ij[i][j] ** 5 - 1) * ((E_i[i] * E_i[j]) ** (5 / 2)))
            V.append(_V)

        V = ((np.sum(np.multiply(Xi, E_i ** (5 / 2)))) ** 2 + 2 * np.sum(np.sum(np.array(V)))) ** (1 / 5)

        K = []

        for i in range(20):
            _K = []
            for j in range(i + 1, 21):
                _K.append(Xi[i] * Xi[j] * (K_ij[i][j] ** 5 - 1) * ((K_i[i] * K_i[j]) ** (5 / 2)))
            K.append(_K)

        K = ((np.sum(np.multiply(Xi, K_i ** (5 / 2)))) ** 2 + 2 * np.sum(np.sum(np.array(K)))) ** (1 / 5)
        self.K = K

        self.tau = 1 / self.T
        tau = self.tau

        B_star_n = []
        Bn = []
        for n in range(18):
            B_star_n1 = []
            for i in range(21):
                B_star_n2 = []
                for j in range(21):
                    e_ij = E_star_ij[i][j] * ((E_i[i] * E_i[j]) ** 0.5)
                    g_ij = G_star_ij[i][j] * ((G_i[i] + G_i[j]) / 2)

                    B_star_nij = ((g_ij + 1 - g_n[n]) ** g_n[n]) * ((Q_i[i] * Q_i[j] + 1 - q_n[n]) ** q_n[n]) * (
                    ((F_i[i] * F_i[j]) ** 0.5 + 1 - f_n[n]) ** f_n[n]) * ((S_i[i] * S_i[j] + 1 - s_n[n]) ** s_n[n]) * (
                                 (W_i[i] * W_i[j] + 1 - w_n[n]) ** w_n[n])

                    b_star_n = a_n[n] * Xi[i] * Xi[j] * B_star_nij * (e_ij ** u_n[n]) * ((K_i[i] * K_i[j]) ** (3 / 2))

                    B_star_n2.append(b_star_n)
                B_star_n1.append(B_star_n2)
            B_star_n.append(np.sum(B_star_n1))
            Bn.append(B_star_n[n] * tau ** u_n[n])
        self.B = np.sum(Bn)
        B = self.B

        p11 = []
        for n in range(12, 18):
            C_n = a_n[n] * ((G + 1 - g_n[n]) ** g_n[n]) * ((Q ** 2 + 1 - q_n[n]) ** q_n[n]) * (
            (F + 1 - f_n[n]) ** f_n[n]) * (V ** u_n[n])
            p11.append(C_n * (tau ** u_n[n]))
        self.p1 = np.sum(p11)

        C_n = []
        for m in range(12, 58):
            _C_n = a_n[m] * ((G + 1 - g_n[m]) ** g_n[m]) * ((Q ** 2 + 1 - q_n[m]) ** q_n[m]) * (
            (F + 1 - f_n[m]) ** f_n[m]) * (V ** u_n[m])
            C_n.append(_C_n)
        self.C_n = C_n

        soldelta = fsolve(self.mydeltafun, 1)

        self.Z = (self.P * tau * K ** 3) / (soldelta * self.R * 1)
        Z = self.Z

        self.T_theta = 298.15
        tau_theta = 1 / self.T_theta
        self.p_theta = 0.101325 * 1000
        rou_theta = self.p_theta / (self.R * self.T_theta)
        delta_theta = rou_theta * K ** 3

        cop_i_R = []
        phi_o_i = []
        phi_o_tau_i = []

        for i in range(N):
            try:
                cop_i_R.append(Bo_i[i] +  # cop_i_R = cop_i_R/R
                               Co_i[i] * (Do_i[i] * tau / np.sinh(Do_i[i] * tau)) ** 2 +
                               Eo_i[i] * (Fo_i[i] * tau / np.cosh(Fo_i[i] * tau)) ** 2 +
                               Go_i[i] * (Ho_i[i] * tau / np.sinh(Ho_i[i] * tau)) ** 2 +
                               Io_i[i] * (Jo_i[i] * tau / np.cosh(Jo_i[i] * tau)) ** 2)
                if np.isnan(cop_i_R[i]):
                    cop_i_R[i] = 0

            except:
                cop_i_R.append(0)

            try:
                phi_o_i.append(Xi[i] * (Ao1_i[i] + Ao2_i[i] * tau + Bo_i[i] * math.log(tau) +
                                        Co_i[i] * math.log(np.sinh(Do_i[i] * tau)) -
                                        Eo_i[i] * math.log(np.cosh(Fo_i[i] * tau)) +
                                        Go_i[i] * math.log(np.sinh(Ho_i[i] * tau)) -
                                        Io_i[i] * math.log(np.cosh(Jo_i[i] * tau)) + math.log(Xi[i])))
                if np.isnan(phi_o_i[i]):
                    phi_o_i[i] = 0
            except:
                phi_o_i.append(0)

            try:
                phi_o_tau_i.append(Xi[i] * (Ao2_i[i] + (Bo_i[i] - 1) / tau +
                                            Co_i[i] * Do_i[i] * ((np.cosh(Do_i[i] * tau)) / np.sinh(Do_i[i] * tau)) -
                                            Eo_i[i] * Fo_i[i] * ((np.sinh(Fo_i[i] * tau)) / np.cosh(Fo_i[i] * tau)) +
                                            Go_i[i] * Ho_i[i] * ((np.cosh(Ho_i[i] * tau)) / np.sinh(Ho_i[i] * tau)) -
                                            Io_i[i] * Jo_i[i] * ((np.sinh(Jo_i[i] * tau)) / np.cosh(Jo_i[i] * tau))))
                if np.isnan(phi_o_tau_i[i]):
                    phi_o_tau_i[i] = 0
            except:
                phi_o_tau_i.append(0)

        np.isnan(cop_i_R)
        cop_R = np.sum(np.multiply(Xi, cop_i_R))
        phi_o = np.sum(phi_o_i) + math.log(soldelta / delta_theta) + math.log(tau_theta / tau)
        phi_o_tau = np.sum(phi_o_tau_i)
        phi_o_tau_tau = (-tau ** (-2)) * (cop_R - 1);

        tauphi_tau_1 = []
        tau2_phi_tautau_1 = []
        phi_2_1 = []

        for i in range(18):
            tauphi_tau_1.append(u_n[i] * B_star_n[i] * tau ** u_n[i])
            tau2_phi_tautau_1.append(((u_n[i]) ** 2 - u_n[i]) * (B_star_n[i]) * (tau ** u_n[i]))
            phi_2_1.append((1 - u_n[i]) * B_star_n[i] * tau ** u_n[i])

        phi1 = []
        tauphi_tau_2 = []
        tau2_phi_tautau_2 = []
        delta_phi_delta_1 = []
        phi_1_1 = []
        phi_2_2 = []
        for i in range(12, 18):
            phi1.append(C_n[i - 12] * tau ** u_n[i])
            tauphi_tau_2.append(u_n[i] * C_n[i - 12] * tau ** u_n[i])
            tau2_phi_tautau_2.append((u_n[i] ** 2 - u_n[i]) * C_n[i - 12] * tau ** u_n[i])
            delta_phi_delta_1.append(C_n[i - 12] * tau ** u_n[i])
            phi_1_1.append(C_n[i - 12] * tau ** u_n[i])
            phi_2_2.append((1 - u_n[i]) * C_n[i - 12] * tau ** u_n[i])

        phi2 = []
        tauphi_tau_3 = []
        tau2_phi_tautau_3 = []
        delta_phi_delta_2 = []
        phi_1_2 = []
        phi_2_3 = []
        for i in range(12, 58):
            phi2.append(C_n[i - 12] * (tau ** u_n[i]) * (soldelta ** b_n[i]) * exp(-c_n[i] * soldelta ** k_n[i]))
            tauphi_tau_3.append(u_n[i] * C_n[i - 12] *
                                tau ** u_n[i] * (soldelta ** b_n[i]) *
                                exp(-c_n[i] * soldelta ** k_n[i]))
            tau2_phi_tautau_3.append((u_n[i] ** 2 - u_n[i]) * C_n[i - 12] *
                                     (tau ** u_n[i]) * (soldelta ** b_n[i]) *
                                     exp(-c_n[i] * soldelta ** k_n[i]))
            delta_phi_delta_2.append((C_n[i - 12] * (tau ** u_n[i])) * soldelta ** b_n[i] *
                                     (b_n[i] - c_n[i] * k_n[i] * (soldelta ** k_n[i])) *
                                     exp(-c_n[i] * (soldelta ** k_n[i])))

            phi_1_2.append(C_n[i - 12] * tau ** u_n[i] * soldelta ** b_n[i] *
                           (b_n[i] - (1 + k_n[i]) * c_n[i] * k_n[i] * soldelta ** k_n[i] +
                            (b_n[i] - c_n[i] * k_n[i] * soldelta ** k_n[i]) ** 2) *
                           exp(-c_n[i] * (soldelta ** k_n[i])))

            phi_2_3.append((1 - u_n[i]) * C_n[i - 12] * tau ** u_n[i] * soldelta ** b_n[i] *
                           (b_n[i] - c_n[i] * k_n[i] * soldelta ** k_n[i]) *
                           exp(-c_n[i] * (soldelta ** k_n[i])))

        phi = phi_o + B * soldelta / K ** 3 - soldelta * np.sum(phi1) + np.sum(phi2)
        tau_phi_tau = tau * phi_o_tau + (soldelta / K ** 3) * np.sum(tauphi_tau_1) - soldelta * np.sum(
            tauphi_tau_2) + np.sum(tauphi_tau_3)
        tau2_phi_tautau = tau ** 2 * phi_o_tau_tau + (soldelta / K ** 3) * np.sum(
            tau2_phi_tautau_1) - soldelta * np.sum(tau2_phi_tautau_2) + np.sum(tau2_phi_tautau_3)
        delta_phi_delta = 1 + B * soldelta / (K ** 3) - soldelta * np.sum(delta_phi_delta_1) + np.sum(delta_phi_delta_2)
        phi_1 = 1 + 2 * B * (soldelta / (K ** 3)) - 2 * soldelta * np.sum(phi_1_1) + np.sum(phi_1_2)
        phi_2 = 1 + (soldelta / K ** 3) * np.sum(phi_2_1) - soldelta * np.sum(phi_2_2) + np.sum(phi_2_3)

        self.D = M * soldelta / K ** 3
        self.rou = soldelta / K ** 3
        self.U = self.R * self.T / M * tau_phi_tau
        self.H = self.R * self.T / M * (tau_phi_tau + delta_phi_delta)
        self.S = (tau_phi_tau - phi) * self.R / M
        self.C_v = self.R / M * (-tau2_phi_tautau)
        self.C_p = self.R / M * (-tau2_phi_tautau + phi_2 ** 2 / phi_1)
        self.mu = (phi_2 / phi_1 - 1) / self.C_p / M / self.rou * 1000
        self.kappa = phi_1 / Z * self.C_p / self.C_v
        self.w = math.sqrt(phi_1 * self.C_p / self.C_v * self.R * T / M * 1000)

    def returnCol(self, matrix, colindex):
        col = []
        for list in matrix:
            col.append(list[colindex])
        return col


    def mydeltafun(self, delta):

        _C_n = []
        delta = delta
        C_n = self.C_n
        tau = self.tau
        u_n = self.u_n
        b_n = self.b_n
        c_n = self.c_n
        k_n = self.k_n

        for n in range(12, 58):
            _C_n.append(C_n[n - 12] * tau ** u_n[n] \
                        * delta ** b_n[n] * (b_n[n] - c_n[n] * k_n[n] * delta ** k_n[n]) \
                        * exp(-c_n[n] * delta ** k_n[n]))
        _C_n = np.sum(_C_n)

        return ((delta * self.R) / (tau * self.K ** 3)) * (
        1 + self.B * delta / self.K ** 3 - delta * self.p1 + _C_n) - self.P

    def calculate(self, P, T):
        self.P = P
        self.T = T
        self.Uinit()
        pass