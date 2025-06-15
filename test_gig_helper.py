# test_gig_helper.py
from decision import decide_offer

def run_tests():
    test_cases = [
        {'time': 10, 'miles': 0.5, 'payout': 4.00},
        {'time': 5,  'miles': 0.8, 'payout': 3.00},
        {'time': 30, 'miles': 2.0, 'payout': 10.20},
        {'time': 15, 'miles': 1.2, 'payout': 4.50},  # Yellow
        {'time': 10, 'miles': 2.1, 'payout': 6.00},  # +0.25 modifier
        {'time': 25, 'miles': 9.9, 'payout': 12.00},
        {'time': 7,  'miles': 1.1, 'payout': 5.00},  # Exact floor
        {'time': 30, 'miles': 10.0,'payout': 6.00},  # Red
        {'time': 20, 'miles': 4.0, 'payout': 25.00}, # High ratio
    ]

    for i, case in enumerate(test_cases, 1):
        result = decide_offer(case['time'], case['miles'], case['payout'])
        print(f"\nTest Case {i}: {case}")
        print(f"→ Result: {result}")

if __name__ == "__main__":
    run_tests()
