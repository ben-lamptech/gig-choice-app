# calculator.py

from config import TIME_VALUE, BASE_DISTANCE_VALUE
from utils import calculate_modifier, apply_payout_floor


def compute_expected_payout(time_estimate, total_miles):
    """Calculate the expected payout based on time and distance, enforcing floors."""
    modifier = calculate_modifier(total_miles)
    raw_expected = (time_estimate * TIME_VALUE) + \
                   (total_miles * (BASE_DISTANCE_VALUE + modifier))
    floor = apply_payout_floor(total_miles)
    return max(raw_expected, floor)


def compute_ratio(actual_payout, expected_payout):
    """Compute the ratio of actual payout to expected payout."""
    if expected_payout <= 0:
        return 0.0
    return actual_payout / expected_payout