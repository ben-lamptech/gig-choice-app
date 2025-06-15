# Gig Offer Evaluator (v0.1)

A lightweight tool to evaluate gig economy delivery offers based on distance, time estimate, and payout. Helps determine whether a gig is worth accepting using a simple rules-based system.

## 🎯 Goal

Make real-time decisions easier by calculating whether a delivery offer meets your payout expectations.

## 💡 Core Logic

1. **Expected Payout Calculation**  
   Uses time and mileage to estimate expected fair pay.
expected = max(
payout_floor,
(time_minutes × TIME_RATE) + (miles × (MILE_RATE + modifier))
)

2. **Modifiers**  
Modifiers: Add $0.25 per mile beyond key thresholds:
- +$0.25 if miles > 2
- +$0.25 more if miles > 10

3. **Payout Floors (Hard Minimums)**  
Ensures you’re not underpaid:
- $3.00 for trips < 1 mile
- $5.00 for trips ≥ 1 mile

4. **Tier Assignment**  
Based on ratio of offered payout to expected:
- ✅ **Green**: Ratio ≥ 1.0
- ⚠️ **Yellow**: 0.85 ≤ Ratio < 1.0
- ❌ **Red**: Ratio < 0.85

5. **Confidence Score**  
Based on how long the offer will take:
- Grows with time, capped at 1.0
- Formula: `min(1.0, time_minutes / 10)`

---

## 📁 File Overview
| File               | Responsibility                          |
|--------------------|------------------------------------------|
| `config.py`        | Constants and thresholds                 |
| `utils.py`         | Modifier and floor logic                 |
| `calculator.py`    | Expected payout, ratio logic             |
| `decision.py`      | Tier, confidence, and decision output    |
| `test_gig_helper.py`| Sample cases and orchestration (main)  |

## ▶️ How to Run

```bash
python main.py
``` 

## ✅ Example Output
--- Gig Decision ---
Estimated Time: 15 min
Total Miles: 5.2
Offered Pay: $9.5

Tier: Green
Confidence: 100%
Expected Pay: $9.5
Ratio: 1.0

🧪 Testing

Run all built-in test cases with:
 
```bash 
python test_gig_helper.py
``` 
Tests include:

- Short low-mileage trips
- High-distance offers
- Underpaid and overpaid scenarios
- Floor enforcement edge cases

## Future Ideas

These are not in v1 but may be explored later:

- Separate distance_from_rest vs. total_miles
- CLI tool or web UI for real-time use
- CSV/JSON logging of evaluations
- Debug mode for tracing decisions
- Integration with delivery app APIs

## Author note 
Built with clarity and pragmatism. This is just version 0.1, any feedback is welcome.
