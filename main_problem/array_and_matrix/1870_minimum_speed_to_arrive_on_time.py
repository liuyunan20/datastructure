from typing import List
import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def get_time(speed):
            time = 0
            for i in range(len(dist) - 1):
                r = dist[i] % speed
                d = dist[i] // speed
                time += d if r == 0 else d + 1
            time += dist[-1] / speed
            return time

        if len(dist) >= hour + 1:
            return -1
        spd = math.floor(sum(dist) / hour)
        spd = spd if spd != 0 else 1
        pre = spd
        while True:
            time = get_time(spd)
            if time == hour:
                return spd
            elif time < hour:
                while pre < spd:
                    cur_spd = math.ceil((pre + spd) / 2)
                    if cur_spd == spd:
                        return spd
                    time = get_time(cur_spd)
                    if time == hour:
                        return cur_spd
                    elif time < hour:
                        spd = cur_spd
                    else:
                        pre = cur_spd
                return pre
            else:
                pre = spd
                spd *= 2


