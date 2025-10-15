import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# === Input Data ===
# Weighted Grade (%): Represents the metal content of ore
# Net Price ($/unit): Fixed assumed net revenue per unit of recovered metal
data = {
    "Weighted Grade (%)": [0.5, 1.0, 1.5, 2.0, 2.5],
    "Net Price ($/unit)": [100, 100, 100, 100, 100]
}

df = pd.DataFrame(data)

# === Recovery Calculation (Logistic Model) ===
# Recovery (%) = R_max / (1 + exp(-k * (Grade - x0)))
# Models increasing recovery efficiency with grade using an S-curve
R_max = 100   # Maximum theoretical recovery (%)
k = 1.5        # Steepness of the logistic curve
x_0 = 0.2     # Grade at which recovery rate reaches ~50% of R_max

df["Recovery (%)"] = (R_max / (1 + np.exp(-k * (df["Weighted Grade (%)"] - x_0))))

# === Processing Cost Estimation (Linear Regression Model) ===
# Processing Cost ($/t) = A + B * Grade
# Reflects increasing cost with higher grade due to more intensive processing
A = 12    # Fixed base processing cost ($/t)
B = 0.6   # Incremental cost increase per % grade
df["Processing Cost ($/t)"] = A + B * df["Weighted Grade (%)"]

# === Cut-off Grade Calculation ===
# Cut-off Grade (%) = 100 * (Processing Cost / (Net Price * Recovery))
# Represents the minimum grade required to break even
df["Cut-off Grade (%)"] = 100 * (df["Processing Cost ($/t)"] / (df["Net Price ($/unit)"] * df["Recovery (%)"]))

# === Output Table ===
print("\nCalculated Mining Metrics:")
print(df[[
    "Weighted Grade (%)",
    "Recovery (%)",
    "Processing Cost ($/t)",
    "Cut-off Grade (%)"
]])

# === Visualization ===
plt.figure(figsize=(15, 5))

# Plot 1: Recovery vs Grade
plt.subplot(1, 3, 1)
plt.plot(df["Weighted Grade (%)"], df["Recovery (%)"], marker='s', color='green')
plt.title("Recovery vs Weighted Grade")
plt.xlabel("Weighted Grade (%)")
plt.ylabel("Recovery (%)")
plt.grid(True)

# Plot 2: Processing Cost vs Grade
plt.subplot(1, 3, 2)
plt.plot(df["Weighted Grade (%)"], df["Processing Cost ($/t)"], marker='^', color='red')
plt.title("Processing Cost vs Weighted Grade")
plt.xlabel("Weighted Grade (%)")
plt.ylabel("Processing Cost ($/t)")
plt.grid(True)

# Plot 3: Cut-off Grade vs Grade
plt.subplot(1, 3, 3)
plt.plot(df["Weighted Grade (%)"], df["Cut-off Grade (%)"], marker='o', color='blue')
plt.title("Cut-off Grade vs Weighted Grade")
plt.xlabel("Weighted Grade (%)")
plt.ylabel("Cut-off Grade (%)")
plt.grid(True)

plt.tight_layout()
plt.savefig('plot.png')
