def cheap_travels():
    inp = [int(num) for num in input().split(' ')]
    total_trip, m_ride, single_ride_cost, m_ride_cost = inp[0], inp[1], inp[2], inp[3]

    if m_ride * single_ride_cost > m_ride_cost:
        total_m_ride_trip = total_trip // m_ride
        single_rides = total_trip % m_ride

        return (total_m_ride_trip * m_ride_cost) + min((single_rides * single_ride_cost), m_ride_cost)
    else:
        return total_trip * single_ride_cost


if __name__ == '__main__':
    print(cheap_travels())
