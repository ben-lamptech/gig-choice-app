from geopy.distance import geodesic
from datetime import datetime

def calc_miles(location1, location2): 
    return geodesic(location1, location2).miles


    """
    Compute the order score based on distance and location.
    
    Parameters:
    - total_miles_from_restaurant: Total miles from the restaurant to the customer.
    - total_miles_from_customer: Total miles from the customer to the restaurant.
    - restaurant_location: Tuple (lat, lon) of the restaurant's location.
    - customer_location: Tuple (lat, lon) of the customer's location.
    

    Returns:
    - score: Computed score based on the defined rules.

    test cases: 
    - orders ending within 2 miles of restaurant = 0.75 per mile
    - every mile over 2 miles = add $0.25 per mile
    - Sweetspots $12 for 6 miles, $10 for 5 miles, $8 for 4 miles, $6 for 3 miles or more 
    - Over 10 miles increase by 0.25 per mile up to 0.50 per mile 
    - minimum $5 per mile OR 1 mile distance from restaurant to customer

    HOW DO I CALCULATE THE SCORE?
    - timestamp: datetime object of when the order was placed.
    - from datetime import datetime
     - score: float representing the computed score for the order.
     - payout: float representing the payout for the order.
     - estimated_time_minutes: float representing the estimated time in minutes for the order.
     - start_location: Tuple (lat, lon) of the starting location.
     - restaurant_location: Tuple (lat, lon) of the restaurant's location.         
    """
def compute_order_score(order):
    order["miles_to_restaurant"] = calc_miles(order["start_location"], order["restaurant_location"])
    order["miles_restaurent_to_customer"] = calc_miles(order["restaurant_location"], order["customer_location"])
    order["miles_customer_to_restaurant"] = calc_miles(order["customer_location"], order["restaurant_location"])
    order["total_miles"] = (order["miles_to_restaurant"] + order["miles_restaurent_to_customer"])

    score = 0
    #rule 1: near restaurant drop off $0.75 per mile
    




