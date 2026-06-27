import json
import os

# Build path cleanly to look inside the datasets folder
dataset_path = os.path.join("datasets", "hr_dataset.json")

print("--- Loading Golden Evaluation Dataset ---")

with open(dataset_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print(f"Total Test Cases Loaded: {len(data)}\n")

for item in data:
    print(f"ID: {item['id']}")
    print(f"Q: {item['question']}")
    print(f"Expected A: {item['expected_answer']}")
    print(f"Criteria: {item['evaluation_criteria']}")
    print("-" * 50)