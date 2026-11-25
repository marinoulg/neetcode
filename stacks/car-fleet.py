class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        ""
        def one_round_passes(position, speed):
            tmp = []
            for pos, spe in zip(position, speed):
                tmp.append(pos+spe)
            return tmp

        def arrive_at_destination_yet(tmp, target):
            target_achieved = 0
            for elem in (tmp):
                if elem >= target:
                    target_achieved += 1
            return target_achieved

        round = 0
        tmp = one_round_passes(position, speed)
        print(f"round {round}: {tmp}")
        target_achieved = arrive_at_destination_yet(tmp, target)

        while target_achieved <= 0:
            round += 1
            tmp = one_round_passes(tmp, speed)
            print(f"round {round}: {tmp}")
            target_achieved = arrive_at_destination_yet(tmp, target)

        return len(set(tmp))







print(Solution().carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]))

"""
position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)

The destination is at position target miles.

A car can not pass another car ahead of it.
It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed.
A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination,
then the car is considered to be part of the fleet.



Return the number of different car fleets that will arrive at the destination.

"""


# Test 1
"""
# Input
target = 10,
position = [1,4],
speed = [3,2]


round0:
B at 1, R at 4

round1:
B at 4, R at 6

round2:
B at 7, R at 8

round3:
B at 10, R at 10
--> they arrive at the same time
--> 1 car fleet
--> return 1

"""

# Test 2
"""
# Input
target = 10
position = [4,1,0,7]
speed = [2,2,1,1]

round0:
B at 4, R at 1, Y at 0, G at 7

round1:
B at 6, R at 3, Y at 1, G at 8

round2:
B at 8, R at 5, Y at 2, G at 9

round3:
B at 10, R at 7, Y at 3, G at 10
--> B & G arrive at the same time, while R and Y constitute 2 different car fleets
--> 3 car fleet
--> return 3

"""
