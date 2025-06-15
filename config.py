# config.py

# --- Payout Floors ---
MIN_PAYOUT = 5.00         # Hard floor for all trips ≥ 1 mile
SHORT_TRIP_FLOOR = 3.00   # Special floor for trips under 1 mile

# --- Time & Distance Valuation ---
TIME_VALUE = 0.34         # Dollars per minute (goal: $20/hr)
BASE_DISTANCE_VALUE = 0.75 # Dollars per mile baseline

# --- Stacking Modifiers ---
STACK_MODIFIER = 0.25      # Extra per mile beyond thresholds
STACK_THRESHOLDS = {
    'distance_from_rest': 2.0,  # Modifier starts after 2 miles away from restaurant
    'total_distance': 10.0      # Extra modifier after 10+ miles total
}

# --- Tier Thresholds ---
TIERS = [
    (1.0, 'Green'),   # Meets or exceeds target
    (0.8, 'Yellow'),  # Acceptable
    (0.6, 'Orange'),  # Marginal
    (0.0, 'Red'),     # Below minimum threshold
]