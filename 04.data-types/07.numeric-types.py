# Floats with 4 or fewer decimal places print normally
# Floats with 5 or more decimal places may switch to scientific notation
# Using print(f"{float}:f") uses default formatter which is 6 decimal points
# You can force decimal formatting with :f and precision
# / returns a float result & type
# // is same as math.floor(numerator/divisor) , returns an int type

float1 = 0.0001  # Prints as 0.0001
float2 = 0.00001  # Prints as 1e-05 (scientific notation)
float3 = 0.0000001  # Prints as 1e-07 (scientific notation)


print(float1)  # 0.0001
print(float2)  # 1e-05
print(float3)  # 1e-07

# Using print(f"{float}:f") uses default formatter which is 6 decimal points
print(f"{float1:f}")
print(f"{float2:f}")  # 1e-05
print(f"{float3:f}")  # 1e-07

# you can force the formatting
print(f"{float3:.7f}")  # Forces float format with 7 decimal places


########

# / returns a float result & type

print(2 / 1)
print(1 / 2)

# // is same as math.floor(numerator/divisor) , returns an int type
print(2 // 1)
print(1 // 2)

print(type(2 / 1))
print(type(2 // 1))
