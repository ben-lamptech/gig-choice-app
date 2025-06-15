from config import TIERS
from calculator import compute_expected_payout, compute_ratio


def assign_tier(payout_ratio):
    """Assign an efficiency tier based on payout ratio thresholds."""
    for threshold, label in TIERS:
        if payout_ratio >= threshold:
            return label
    return 'Red'


def compute_confidence(payout_ratio):
    """Cap confidence at 1.0 (100%)."""
    return min(payout_ratio, 1.0)


def decide_offer(time_estimate, total_miles, actual_payout):
    """Evaluate a delivery offer and return tier, confidence and metrics."""
    expected = compute_expected_payout(time_estimate, total_miles)
    ratio = compute_ratio(actual_payout, expected)
    tier = assign_tier(ratio)
    confidence = compute_confidence(ratio)

    return {
        'tier': tier,
        'confidence': round(confidence, 2),
        'expected': round(expected, 2),
        'actual': round(actual_payout, 2),
        'ratio': round(ratio, 2)
    }

