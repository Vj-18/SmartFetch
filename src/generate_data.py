
import numpy as np
import pandas as pd
from pathlib import Path

# Reproducibility
np.random.seed(42)

n = 3000

# Generate package information
package_id = [f"SF{i:04d}" for i in range(1, n + 1)]

distance_km = np.random.uniform(1, 30, n).round(2)

package_weight = np.random.uniform(0.2, 20, n).round(2)

package_size = np.random.choice(
    ["Small", "Medium", "Large"],
    n,
    p=[0.5, 0.3, 0.2]
)

traffic_level = np.random.choice(
    ["Low", "Medium", "High"],
    n,
    p=[0.3, 0.45, 0.25]
)

weather = np.random.choice(
    ["Clear", "Cloudy", "Rainy"],
    n,
    p=[0.5, 0.3, 0.2]
)

hour_of_day = np.random.randint(8, 22, n)

day_of_week = np.random.choice(
    ["Monday", "Tuesday", "Wednesday",
     "Thursday", "Friday", "Saturday", "Sunday"],
    n
)

pending_orders = np.random.randint(0, 51, n)

warehouse_processing_minutes = np.random.randint(5, 31, n)

# Convert conditions into numerical effects
traffic_effect = np.select(
    [
        traffic_level == "Low",
        traffic_level == "Medium",
        traffic_level == "High"
    ],
    [0, 12, 25]
)

weather_effect = np.select(
    [
        weather == "Clear",
        weather == "Cloudy",
        weather == "Rainy"
    ],
    [0, 5, 15]
)

# Simulate actual delivery duration
delivery_time_minutes = (
    distance_km * 3.5
    + warehouse_processing_minutes
    + traffic_effect
    + weather_effect
    + pending_orders * 0.3
    + np.random.normal(0, 8, n)
)

delivery_time_minutes = np.maximum(
    delivery_time_minutes, 10
).round(2)

# Simulate promised delivery duration
promised_delivery_minutes = (
    distance_km * 3.5
    + warehouse_processing_minutes
    + 20
).round(2)

# Classification target
delayed = (
    delivery_time_minutes > promised_delivery_minutes
).astype(int)

# Create DataFrame
df = pd.DataFrame({
    "package_id": package_id,
    "distance_km": distance_km,
    "package_weight": package_weight,
    "package_size": package_size,
    "traffic_level": traffic_level,
    "weather": weather,
    "hour_of_day": hour_of_day,
    "day_of_week": day_of_week,
    "pending_orders": pending_orders,
    "warehouse_processing_minutes":
        warehouse_processing_minutes,
    "promised_delivery_minutes":
        promised_delivery_minutes,
    "delivery_time_minutes": delivery_time_minutes,
    "delayed": delayed
})

# Save dataset
output_path = Path("data/raw/package_deliveries.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)

print("Dataset generated successfully!")
print("Shape:", df.shape)
print(df.head())
