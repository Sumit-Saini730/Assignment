

def clean_readings(data):
    if not data:
        # print("This list is empty")
        return []

    cleaned_data = []

    for item in data:
        try:
            val = float(item)

            if val < 0:
                continue

            if val > 500.0:
                val = 500.0

            cleaned_data.append(val)

        except(ValueError, TypeError):
            continue

    return cleaned_data



values1 = [10, "20.5", None, -5, "invalid", 600, 500]
result1 = clean_readings(values1)
print("Test 1:", result1)

values2 = []
result2 = clean_readings(values2)
print("Test 2:", result2)

values3 = [None, "hello", -10, "-5.5"]
result3 = clean_readings(values3)
print("Test 3:", result3)

values4 = [0, 499.9, 500, 500.1, -0.1]
result4 = clean_readings(values4)
print("Test 4:", result4)

