from string import ascii_lowercase

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
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

        def ordering_cars_closer_to_target(position, speed):
            ordering_cars = {}
            for pos, spe, letter in zip(position, speed, ascii_lowercase):
                if letter not in ordering_cars: ordering_cars[letter] = (pos, spe)
                if letter+letter in ordering_cars: ordering_cars[letter+letter] = (pos, spe)
                if letter+letter in ordering_cars: ordering_cars[letter+letter+letter] = (pos, spe)

            ordered_cars = [(letter, elem[0]) for letter, elem in zip(ordering_cars.keys(), ordering_cars.values())]
            sorted_cars = []

            i = 0
            for letter, v in ordered_cars:
                sorted_cars.append((v, letter))
                i+=1

            sorted_cars = (sorted(sorted_cars, reverse=True))
            return sorted_cars, ordering_cars

        def one_round_passes(sorted_cars, ordering_cars):
            for pos, letter in sorted_cars:
                ordering_cars[letter] = (ordering_cars[letter][0] + ordering_cars[letter][1], ordering_cars[letter][1])

            return ordering_cars

        def arrive_at_destination_yet(pos, target):
            target_achieved = 0
            for elem in (pos):
                if elem >= target:
                    target_achieved += 1
            return target_achieved

        # def arrive_at_destination_yet(target, position, speed):


            target_achieved = 0
            tmp_speed = []

            for pos, spe in zip(position, speed):
                print(pos, spe)
                depassement = pos+spe-target
                if depassement*spe == 0:
                    former = (pos, spe)
                else:
                    X = depassement/spe
                    print("xx", X, depassement)
                    if X == spe:
                        """
                        je depasse de 1 quand je suis en vitesse 2 pour 1 round
                        --> je roule en vitesse 1

                        spe (miles/hour) * depassement (miles) = X (hour)
                        X = depassement / spe

                        """
                        print(former, "is the same speed as", (pos, spe), "which is", X)

                    else:
                        print("here")
                        next


                    # if (pos+(test*spe)-target)/(spe) == test:
                    #     print(former, "is the same speed as", (pos, spe), "which is", test)


            # for letter in ordering_cars:
            #     pos, spe = ordering_cars[letter]
            #     print(pos, spe, "(target-pos):",(target-pos)/spe)
            #     if pos >= target: target_achieved += 1
            #     tmp_speed.append(((target-pos)/spe))

            # for i in range(len(pos)):
            #     elem = pos[i]
            #     # spe = speed[i]
            #     if elem >= target:
            #         target_achieved += 1
            #     # tmp_speed.append((target-elem))
            return target_achieved, tmp_speed

        def result_one_round(sorted_cars, ordering_cars, round):
            ordering_cars = one_round_passes(sorted_cars, ordering_cars)
            pos = [ordering_cars[letter][0] for letter in ordering_cars]
            speed = [ordering_cars[letter][1] for letter in ordering_cars]
            sorted_cars, ordering_cars = ordering_cars_closer_to_target(pos, speed)

            return ordering_cars, pos, speed


        round = 0
        sorted_cars, ordering_cars = ordering_cars_closer_to_target(position, speed)
        print(f"round {round}: (target = {target}) {position} - {speed}")
        target_achieved = arrive_at_destination_yet(position, target)
        # print("tmp_speed:", tmp_speed)
        # print("ordering_cars:", ordering_cars)

        if len(set(position)) != len(position): car_fleet = len(set(position))
        else:
            car_fleet = 0

        target_tmp = {}
        c = 0
        while sorted_cars != [] and round <=10:
            ordering_cars, pos, speed = result_one_round(sorted_cars, ordering_cars, round)
            sorted_cars, ordering_cars = ordering_cars_closer_to_target(pos, speed)
            print(f"round {round}: {pos} - {speed}")

            target_achieved = arrive_at_destination_yet(pos, target)
            # print("tmp_speed:", tmp_speed)
            # print()
            if len(pos) != len(set(pos)):
                tmp = {}
                dup = int()
                for spe, letter in sorted_cars:
                    if spe not in tmp: tmp[spe] = [letter]
                    else:
                        tmp[spe].append(letter)
                        dup = (spe)

                tmp_speed = []
                for letter in tmp[dup]:
                    print(letter)
                    tmp_speed.append(ordering_cars[letter][1])

                tmp_speed = (sorted(tmp_speed))[0]
                # print("tmp_speed:", tmp_speed)

                for letter in tmp[dup]:
                    ordering_cars[letter] = (dup, tmp_speed)



            if len(position) != len(set(position)) and len(speed) != len(set(speed)):
              for elem in sorted_cars:
                if elem[0] >= target:
                    # speed_ =
                    ""
                    # print(elem)
                    # print(ordering_cars)
                    # letter = elem[1]
                    # sorted_cars.remove(elem)
                    # sorted_cars.append((target, letter))

            to_del = []
            for elem in sorted_cars[::-1]:
                if elem[0] >= target:
                    sorted_cars.remove(elem)
                    to_del.append(elem[1])
                    if round not in target_tmp: target_tmp[round] = [elem]
                    else: target_tmp[round].append(elem)

            for elem in to_del:
                del ordering_cars[elem]

            round+=1


        for elem in target_tmp:
            tmp_c = set()
            for el in target_tmp[elem]:
                tmp_c.add(el[0])
            c += len(tmp_c)
            print(tmp_c, c)

        return c

# # ------------------------

# print(Solution().carFleet(target=100,
# position=[0,2,4],
# speed=[4,2,1]))
# print()
# # #True should be 1

# print(Solution().carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]))
# print()
# # #True should be 3

# print(Solution().carFleet(target = 10, position = [1,4], speed = [3,2]))
# print()
# # #True should be 1

# print(f"{Solution().carFleet(target=10,
# position=[1,4],
# speed=[3,2])}")
# print()
# # #True should be 1

print(Solution().carFleet(target=20,
position=[6,2,17],
speed=[3,9,2]))
print()
# should be 2

print(Solution().carFleet(target=10,
position=[8,3,7,4,6,5],
speed=[4,4,4,4,4,4]))
#True should be 6
print()
