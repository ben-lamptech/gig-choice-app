# main.py
from decision import decide_offer

def main():
    # Sample manual input
    time_estimate = 15  # in minutes
    total_miles = 5.2
    actual_payout = 9.50

    result = decide_offer(time_estimate, total_miles, actual_payout)

    print("\n--- Gig Decision ---")
    print(f"Estimated Time:   {time_estimate} min")
    print(f"Total Miles:      {total_miles}")
    print(f"Offered Pay:      ${actual_payout}")
    print(f"\nTier:             {result['tier']}")
    print(f"Confidence:       {result['confidence'] * 100:.0f}%")
    print(f"Expected Pay:     ${result['expected']}")
    print(f"Ratio:            {result['ratio']}")

if __name__ == "__main__":
    main()
