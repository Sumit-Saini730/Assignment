import csv
import json
import os
import math

filename = "device_telemetry.csv"

# if os.path.exists(filename):
#     with open(filename, "r", newline="") as file:
#         reader = csv.DictReader(file)

#         devices = {}

#         for row in reader:
#             device_id = row["device_id"]
#             if device_id not in devices:
#                 devices[device_id] = []

#             devices[device_id].append(row)

#         # print(devices)

#         summary = {}
        
#         for device_id, records in devices.items():
#             total_records = len(records)
#             temperatures = []
#             error_count = 0
#             for record in records:
#                 temperature = float(record["temperature"])
#                 temperatures.append(temperature)

#                 if record["status"] == "ERROR":
#                     error_count += 1

#             average_temperature = sum(temperatures)/len(temperatures)

#             if average_temperature > 80.0:
#                 continue
            
#             summary[device_id] = {
#                 "record_count": total_records,
#                 "average_temperature": average_temperature,
#                 "error_count": error_count
#             }

#         print(summary)

#     with open("summary.json", "w") as file:
#         json.dump(summary, file, indent=4)
#         print("Summary exported successfully!")

#     print(f"{'Device':<12} {'Records':<10} {'Avg Temp':<12} {'Errors':<10}")
#     print("-" * 44)

#     for device_id, data in summary.items():
#         print(
#             f"{device_id:<12} " 
#             f"{data['record_count']:<10} "
#             f"{data['average_temperature']:<12.2f} "
#             f"{data['error_count']:<10} "
#         )

# else:
#     print(f"Error: The file {filename} does not exist")




# i will be honest above code is what i wrote and when i asked ai for the edge cased it gave me the below version
# it includes if a file is empty case and file has header but no data, bad csv file and added protected against division by zero in calculation of average_temperature



if not os.path.exists(filename):
    print(f"Error: The file {filename} does not exist")

else:
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            required_columns = {"device_id", "status", "temperature"}

            if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
                raise ValueError("CSV is missing required columns")

            devices = {}

            for row in reader:
                device_id = (row.get("device_id") or "").strip()
                status = (row.get("status") or "").strip().upper()

                # Skip rows with missing device IDs
                if not device_id:
                    continue

                # Convert temperature safely
                try:
                    temperature = float(row.get("temperature", ""))
                except (ValueError, TypeError):
                    continue

                # Skip non-finite temperatures
                if not math.isfinite(temperature):
                    continue

                if device_id not in devices:
                    devices[device_id] = {
                        "temperatures": [],
                        "error_count": 0,
                        "record_count": 0
                    }

                devices[device_id]["temperatures"].append(temperature)
                devices[device_id]["record_count"] += 1

                if status == "ERROR":
                    devices[device_id]["error_count"] += 1

        summary = {}

        for device_id, data in devices.items():
            temperatures = data["temperatures"]

            # Avoid division by zero
            if not temperatures:
                continue

            average_temperature = sum(temperatures) / len(temperatures)

            if average_temperature > 80.0:
                continue

            summary[device_id] = {
                "record_count": data["record_count"],
                "average_temperature": round(average_temperature, 2),
                "error_count": data["error_count"]
            }

        with open("summary.json", "w", encoding="utf-8") as file:
            json.dump(summary, file, indent=4)

        print("Summary exported successfully!\n")

        print(f"{'Device':<12} {'Records':<10} {'Avg Temp':<12} {'Errors':<10}")
        print("-" * 44)

        for device_id, data in summary.items():
            print(
                f"{device_id:<12} "
                f"{data['record_count']:<10} "
                f"{data['average_temperature']:<12.2f} "
                f"{data['error_count']:<10}"
            )

        if not summary:
            print("No devices met the filtering criteria.")

    except (OSError, csv.Error, ValueError) as error:
        print(f"Error processing CSV: {error}")

