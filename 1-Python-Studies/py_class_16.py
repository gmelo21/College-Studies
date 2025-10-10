items = [
    {"name": "Item1", "weight": 2, "value": 3},
    {"name": "Item2", "weight": 3, "value": 4},
    {"name": "Item3", "weight": 4, "value": 8},
    {"name": "Item4", "weight": 2, "value": 5},
    {"name": "Item5", "weight": 1, "value": 2},
    {"name": "Item6", "weight": 5, "value": 6},
    {"name": "Item7", "weight": 3, "value": 3}
]

max_weight = 8

valid_combinations = []

def generate_combinations(start, current_combo):
    if current_combo:
        total_weight = sum(item['weight'] for item in current_combo)
        total_value = sum(item['value'] for item in current_combo)
        if total_weight <= max_weight:
            valid_combinations.append({
                'combo': current_combo,
                'total_weight': total_weight,
                'total_value': total_value
            })

    for i in range(start, len(items)):
        generate_combinations(i + 1, current_combo + [items[i]])

generate_combinations(0, [])

if valid_combinations:
    max_value = max(c['total_value'] for c in valid_combinations)
    best_by_value = [c for c in valid_combinations if c['total_value'] == max_value]

    min_weight = min(c['total_weight'] for c in best_by_value)
    best_combinations = [c for c in best_by_value if c['total_weight'] == min_weight]

    print("\nBest Combination(s):\n")
    for combo in best_combinations:
        names = [item['name'] for item in combo['combo']]
        print(f"Items: {', '.join(names)} - Total Weight: {combo['total_weight']} - "
              f"Total Value: {combo['total_value']}")
else:
    print("No valid combinations within weight limit.")
