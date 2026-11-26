class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        ""
        def ordering_cars_closer_to_target(position, speed):
            ordering_cars = {}
            for pos, spe in zip(position, speed):
                if pos not in ordering_cars: ordering_cars[pos] = [spe]
                else: ordering_cars[pos].append(spe)

            # print(ordering_cars)
            ordered_cars = sorted(list(ordering_cars.keys()), reverse=True)

            ordered_speeds = []
            for pos in list(ordering_cars.keys())[::-1]:
                spe = ordering_cars[pos]
                if len(ordering_cars[pos]) == 1:
                    spe = spe[0]
                    # print(pos,"+", spe)
                    # print(pos, spe)
                    ordered_speeds.append(spe)
                else:
                    for elem in (ordering_cars[pos]):
                        # print(pos,"+", elem)
                        ordered_speeds.append(elem)

            # print("os:", )

            return ordering_cars, ordered_cars, ordered_speeds

        def one_round_passes(ordering_cars, ordered_speeds, reverse=True):
            tmp = []
            if reverse == False:
                for car in list(ordering_cars.keys())[::-1]:
                    for speed in ordering_cars[car]:
                        # print(car, speed)
                        tmp.append(car+speed)

            else:
                # print(len(ordered_speeds), len(list(ordering_cars.keys())))
                for car in list(ordering_cars.keys()):
                    for speed in ordering_cars[car]:
                        # print(car, speed)
                        tmp.append(car+speed)


            # print("tp:", tmp)
            return tmp

        def arrive_at_destination_yet(tmp, target):
            target_achieved = 0
            for elem in (tmp):
                if elem >= target:
                    target_achieved += 1
            return target_achieved

        def prevent_fleets(tmp, ordered_speeds):
            # if len(tmp) != len(set(tmp)):
            #     car_fleets = len(set(tmp))
            # print("nb of car_fleets is", car_fleets, ":\n" + "; ".join([f"{i+1} car{"s" if (i+1)>1 else ""} at {tmp[i]} coord" for i in range(len(set(tmp)))]))

            ordering_cars_bis = {}
            for car_pos, spe in zip(tmp, ordered_speeds):
                if car_pos not in ordering_cars_bis: ordering_cars_bis[car_pos] = [spe]
                else: ordering_cars_bis[car_pos].append(spe)
            # print("ordering_cars_bis:",ordering_cars_bis)
            # print()

            mini = 10000
            for pos in list(ordering_cars_bis.keys())[::-1]:
                spe = ordering_cars_bis[pos]
                # print(pos, spe)
                if len(ordering_cars_bis[pos]) > 1:
                    poping = len(ordering_cars_bis[pos])
                    for elem in (ordering_cars_bis[pos]):
                        if elem <= mini:
                            mini = elem
                            ordering_cars_bis[pos] = [mini]*poping
                else:
                    ordering_cars_bis[pos] = ordering_cars_bis[pos]


            # print("ordering_cars_bis:",ordering_cars_bis)

            ordered_speeds_bis = []
            for elem in (list(ordering_cars_bis.values())):
                if len(elem) == 1:
                    ordered_speeds_bis.append(elem[0])
                else:
                    for n in elem:
                        ordered_speeds_bis.append(n)

            # print("ordered_speeds_bis:",ordered_speeds_bis)
            return ordering_cars_bis, ordered_speeds_bis







        round = 0
        ordering_cars, ordered_cars, ordered_speeds = ordering_cars_closer_to_target(position, speed)
        print(f"round {round}: {ordered_cars}")
        tmp = one_round_passes(ordering_cars, ordered_speeds)
        target_achieved = arrive_at_destination_yet(tmp, target)
        # print("target_achieved:", target_achieved)


        round += 1
        print(f"round {round}: {tmp}")
        tmp = one_round_passes(ordering_cars, ordered_speeds)
        ordering_cars, ordered_speeds = prevent_fleets(tmp, ordered_speeds)
        # print(tmp)

        # print(f"round {round}: {tmp}")
        # round += 1
        # tmp = one_round_passes(ordering_cars, ordered_speeds, reverse=False)
        # ordering_cars, ordered_speeds = prevent_fleets(tmp, ordered_speeds)
        # print(tmp)

        # print(f"round {round}: {tmp}")
        # # round += 1
        # # tmp = one_round_passes(ordering_cars, ordered_speeds, reverse=False)
        # # ordering_cars, ordered_speeds = prevent_fleets(tmp, ordered_speeds)
        # print(tmp)



        while target_achieved <= 0:
            round += 1
            tmp = one_round_passes(ordering_cars, ordered_speeds)
            ordering_cars, ordered_speeds = prevent_fleets(tmp, ordered_speeds)
            print(f"round {round}: {tmp}")
            target_achieved = arrive_at_destination_yet(ordering_cars, target)
            # print("target:", target_achieved)

        return len(set(tmp))







# print(Solution().carFleet(target=100,
# position=[0,2,4],
# speed=[4,2,1]))

# print(Solution().carFleet(target=100,
# position=[0,2,4],
# speed=[4,2,1]))

print(Solution().carFleet(target=10,
position=[1,4],
speed=[3,2]))



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
