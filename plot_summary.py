
import json
import matplotlib.pyplot as plt

with open("summary.json", "r", encoding="utf-8") as file:
    summary = json.load(file)

devices = list(summary.keys())
temperatures = [
    data["average_temperature"]
    for data in summary.values()
]

fig, ax = plt.subplots(figsize=(9, 5))

bars = ax.bar(devices, temperatures, width=0.65)

ax.set_title("Average Temperature per Device", fontsize=14, pad=12)
ax.set_xlabel("Device ID")
ax.set_ylabel("Average Temperature (°C)")

# Add temperature values above each bar
ax.bar_label(bars, fmt="%.1f", padding=4)

# Add subtle horizontal gridlines
ax.set_axisbelow(True)
ax.yaxis.grid(True, linestyle="--", alpha=0.3)

# Leave space above the tallest bar
if temperatures:
    ax.set_ylim(0, max(temperatures) * 1.15)

fig.tight_layout()
fig.savefig("temperature_chart.png", dpi=150, bbox_inches="tight")
plt.show()
