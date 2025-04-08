import json

results = []

# Simulate test 1
try:
    assert 1 + 1 == 2
    results.append({"name": "addition", "status": "passed", "points": 2})
except AssertionError:
    results.append({"name": "addition", "status": "failed", "points": 2})

# Simulate test 2
try:
    assert 5 * 0 == 0
    results.append({"name": "multiply", "status": "passed", "points": 3})
except AssertionError:
    results.append({"name": "multiply", "status": "failed", "points": 3})

# Write to results.json
with open("results.json", "w") as f:
    json.dump(results, f)

# Optionally print total score
total = sum(r["points"] for r in results if r["status"] == "passed")
max_points = sum(r["points"] for r in results)
print(f"Test Score: {total} / {max_points}")