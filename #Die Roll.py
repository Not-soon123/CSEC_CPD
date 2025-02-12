import math

def probability_to_visit_transylvania(Y, W):
    # Find the maximum of Yakko's and Wakko's rolls
    M = max(Y, W)
    
    # The number of favorable outcomes for Dot is from M to 6
    favorable_outcomes = 6 - M + 1
    
    # The total number of outcomes is always 6
    total_outcomes = 6
    
    # Simplify the fraction using GCD
    gcd_value = math.gcd(favorable_outcomes, total_outcomes)
    
    # Simplified numerator and denominator
    numerator = favorable_outcomes // gcd_value
    denominator = total_outcomes // gcd_value
    
    # Return the result in the form "A/B"
    return f"{numerator}/{denominator}"

# Input reading
Y, W = map(int, input().split())

# Output the result
print(probability_to_visit_transylvania(Y, W))
