def getMinimumHours(deliveryHours, preparationTimes):
    # Write your code here
    time_hours = sorted(zip(preparationTimes, deliveryHours), key=lambda x: x[1])
    print(time_hours)
    time_left = list(map(lambda y: (y[0], list(filter(lambda x: x - y[0] > 0, y[1]))), time_hours))
    print(time_left)

    if any(map(lambda x: not len(x[1]), time_left)):
        return -1

    hour = 0
    total_time = 0
    for time, hours in time_left:
        for hour in hours:
            if total_time + time < hour:
                total_time += time
                break
        else:
            return -1
    return hour


print(getMinimumHours([[3, 9], [1, 7], [1, 5]], [1, 1, 4]))