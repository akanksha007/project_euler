"""
How many distinct terms are in the sequence generated by a**power_array for 2 ≤ a ≤ 100 and 2 ≤ power_array ≤ 100?
"""
power_array=[i**j for i in range(2,101) for j in range(2,101)]
print len(list(set(power_array)))