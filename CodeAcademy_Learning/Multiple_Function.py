def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if city =="Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost_per_day = 40 * days
    if days>=7:
         cost_per_day = cost_per_day - 50
    elif days>=3:
        cost_per_day = cost_per_day - 20
    return cost_per_day

def trip_cost(city,days,spending_money):
    cost = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    print "Total Cost for %d days in city of %s is %d dollars" % (days , city, cost)

trip_cost("Los Angeles",5,600)
