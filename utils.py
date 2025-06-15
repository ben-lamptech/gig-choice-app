
# utils.py

from config import STACK_MODIFIER, STACK_THRESHOLDS


def calculate_modifier(total_miles):
    """Calculate additional distance-based payout modifier."""
    modifier = 0.0
    # +$0.25 for >2 miles
    if total_miles > STACK_THRESHOLDS['distance_from_rest']:
        modifier += STACK_MODIFIER
    # +$0.25 more for >10 miles
    if total_miles > STACK_THRESHOLDS['total_distance']:
        modifier += STACK_MODIFIER
    return modifier


def apply_payout_floor(total_miles):
    """Return minimum payout floor based on distance."""
    return SHORT_TRIP_FLOOR if total_miles < 1 else MIN_PAYOUT
