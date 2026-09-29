# transformer-
# Python program for Transformer

V1 = float(input("Enter primary voltage (V): "))
N1 = float(input("Enter number of primary turns: "))
N2 = float(input("Enter number of secondary turns: "))
I1 = float(input("Enter primary current (A): "))

# Calculate secondary voltage
V2 = (V1 * N2) / N1

# For an ideal transformer: V1 * I1 = V2 * I2
I2 = (V1 * I1) / V2

print("\nTransformer Calculation")
print("Primary Voltage =", V1, "V")
print("Secondary Voltage =", round(V2, 2), "V")
print("Primary Current =", I1, "A")
print("Secondary Current =", round(I2, 2), "A")
