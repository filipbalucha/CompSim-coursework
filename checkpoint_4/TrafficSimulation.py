import numpy as np
from random import random


class TrafficSimulation(object):
    def __init__(self):
        pass

    def steady_state_avg_speed(self, density, size):
        num_cars = int(density * size)
        num_empty = size - num_cars
        # create an array of integers where one represents a segment which has a car
        arr = np.array([0] * num_empty + [1] * num_cars)
        # shuffle the array in place to simulate traffic
        np.random.shuffle(arr)
        print(arr)
        for _ in range(5):
            arr = self.traffic_step(arr)
            print(arr)

    def traffic_step(self, arr):
        # create a new 1D array the size of the previous one and fill it with empty segments
        new_arr = np.full(arr.size, 0)
        for i, has_car in enumerate(arr):
            # the following three lines abuse the fact that 1 == True and 0 == False
            next_full = arr[(i+1) % arr.size]
            previous_full = arr[(i-1) % arr.size]
            if (has_car and next_full) or (not has_car and previous_full):
                # this segment will have a car after this iteration if:
                  # it has a car now and the next segment is full
                  # it is empty and the previous segment has a car
                new_arr[i] = 1
        return new_arr
