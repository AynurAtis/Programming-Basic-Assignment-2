# 250201092

import math


def user_input(number):

    # Get the circles location

    circles = {}
    counter = 0
    for a in range(number):
        circle = input("Enter circle " + str(counter) + ": ").split(" ")
        circle[0] = float(circle[0])
        circle[1] = float(circle[1])
        circles[a] = circle
        counter += 1
    return circles


def two_circle_solution():

    # Part I

    intersection = 0
    union = 0
    intersection_over_union = 0

    radius = float(input("Enter radius:")) # Get the radius from the user
    circle_list = user_input(2) # Get the 2 circles location from the user

    # distance_radius is the distance between two circles's location
    distance_radius = (((circle_list[1][0]) - (circle_list[0][0])) ** 2
                       + ((circle_list[1][1]) - (circle_list[0][1])) ** 2) ** 0.5

    if distance_radius >= 2 * radius: # situation that two circles discrete from each other

        intersection = 0
        union = (math.pi * radius) * 2
        intersection_over_union = 0  # intersection_over_union = intersection / union

    elif (radius * 2) > distance_radius > radius: # situation that two circles's centers out of the intersection area

        # distance_intersection points = find the distance between two points of two circles that are intersection
        distance_intersection_points = (((radius ** 2) - ((distance_radius / 2) ** 2)) ** 0.5) * 2
        # angle = find the angle using cosine theorem
        angle = math.degrees(math.acos(((2 * (radius ** 2)) - (distance_intersection_points ** 2)) / (2 * radius ** 2)))
        # intersection = find the intersection area between two circles
        intersection = (((math.pi * (radius ** 2) * (angle / 360)) * 2) -
                        ((((distance_radius / 2) * (distance_intersection_points / 2)) / 2) * 4))
        # union = find the union area between two circles
        union = ((math.pi * radius ** 2) * 2) - intersection
        # intersection_over_union = intersection / union
        intersection_over_union = intersection / union

    elif distance_radius <= radius: # situation that two circles's centers inside of the intersection area

        # distance_intersection points = find the distance between two points of two circles that are intersection
        distance_intersection_points = abs((radius ** 2) - (distance_radius / 2) ** 2) ** 0.5
        # angle = find the angle using cosine theorem
        angle = math.degrees(math.acos(distance_radius / (2 * radius)))
        # intersection = find the intersection area between two circles
        intersection = (math.pi * (radius ** 2) * (angle / 90)) - (distance_radius * distance_intersection_points)
        # union = find the union area between two circles
        union = ((math.pi * radius ** 2) * 2) - intersection
        # intersection_over_union = intersection / union
        intersection_over_union = intersection / union

    print(intersection)
    print(union)
    print(intersection_over_union * 100, "%")


def multiple_circle_solution():

    # Part II

    intersection_over_union = 0
    strong_overlap_list = []
    radius = float(input("Enter the radius: ")) # Get the radius from the user
    num_of_circles = int(input("Enter the number of circles: ")) # Get the number of  circles from the user
    list_of_circles = user_input(num_of_circles) # Get the circles location that users write
    threshold = float(input("Enter threshold: "))

    for j in range(len(list_of_circles)):
        for k in range(j + 1, len(list_of_circles)):

            # distance_radius is the distance between two circles's location
            distance_radius = (((list_of_circles[j][0]) - (list_of_circles[k][0])) ** 2
                               + ((list_of_circles[j][1]) - (list_of_circles[k][1])) ** 2) ** 0.5

            if distance_radius >= 2 * radius: # situation that two circles discrete from each other
                # intersection_over_union = intersection / union
                intersection_over_union = 0 # it is not intersection area, so intersection area is 0.
                print(j, "and", k, ": No overlap")

                # situation that two circles's centers out of the intersection area
            elif (radius * 2) > distance_radius > radius:

                # distance_intersection points =
                # find the distance between two points of two circles that are intersection
                distance_intersection_points = (((radius ** 2) - ((distance_radius / 2) ** 2)) ** 0.5) * 2
                # angle = find the angle using cosine theorem
                angle = math.degrees(
                    math.acos(((2 * (radius ** 2)) - (distance_intersection_points ** 2)) / (2 * radius ** 2)))
                # intersection = find the intersection area between two circles
                intersection = (((math.pi * (radius ** 2) * (angle / 360)) * 2) -
                                ((((distance_radius / 2) * (distance_intersection_points / 2)) / 2) * 4))
                # union = find the union area between two circles
                union = ((math.pi * radius ** 2) * 2) - intersection
                # intersection_over_union = intersection / union
                intersection_over_union = intersection / union

            elif distance_radius < radius: # situation that two circles's centers inside of the intersection area

                # distance_intersection points =
                # find the distance between two points of two circles that are intersection
                distance_intersection_points = abs((radius ** 2) - (distance_radius / 2) ** 2) ** 0.5
                # angle = find the angle using cosine theorem
                angle = math.degrees(math.acos(distance_radius / (2 * radius)))
                # intersection = find the intersection area between two circles
                intersection = ((math.pi * (radius ** 2) * (angle / 90))
                                - (distance_radius * distance_intersection_points))
                # union = find the union area between two circles
                union = ((math.pi * radius ** 2) * 2) - intersection
                # intersection_over_union = intersection / union
                intersection_over_union = intersection / union
            if intersection_over_union >= threshold:
                print(j, "and", k, ": Strong overlap")
                tmp = [j, k]
                strong_overlap_list.append(tmp)

            elif threshold > intersection_over_union > 0:
                print(j, "and", k, ": Weak overlap")

    deleted_list = [] # list of the circles that deleted strong overlap
    for overlap in strong_overlap_list:
        print(overlap)
        if len(deleted_list) == 0:
            deleted = overlap[1]
            deleted_list.append(deleted)
        # if after elements in the deleted list including overlap first index, continue
        elif overlap[0] in deleted_list:
            continue
        # if after elements in the deleted list including overlap second index, continue
        elif overlap[1] in deleted_list:
            continue
        else: # add the deleting elements inside deleted list
            deleted = overlap[1]
            deleted_list.append(deleted)
    print("Circles after elimination: ")
    # Circles after elimination
    for i in range(num_of_circles):
        if i in deleted_list:
            continue
        else:
            print(i)


def menu():

    print("Menu:")
    print("[1] Two Circles")
    print("[2] Many Circles")
    print("[3] Exit Program")


while True:

    menu()
    option = input("Please enter an option: ")

    if option.isnumeric() and int(option) == 1:
        two_circle_solution()

    elif option.isnumeric() and int(option) == 2:

        multiple_circle_solution()
    elif option.isnumeric() and int(option) == 3:
        break
    else:
        print("Wrong Input. Please enter your choice correctly.")
        cont = input("Please enter to continue")
