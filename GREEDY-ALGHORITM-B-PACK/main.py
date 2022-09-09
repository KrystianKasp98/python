def backpack_greedy(weights, values, total_weight):
    data = []
    # find the most profitable items
    for i in range(len(weights)):
        data.append({
            "value": values[i],
            "weight": weights[i],
            "cost": float(values[i]/float(weights[i]))
        })
    # sort list from the most profitable to the least profitable
    data = sorted(data, key=lambda x: x["cost"], reverse=True)
    # print(f'DEBUG: {data}')

    remain = total_weight
    result = 0
    result_list = []
    i = 0

    while i < len(data):
        if data[i]["weight"] <= remain:
            remain -= data[i]["weight"]
            result += data[i]["value"]
            result_list.append(data[i])
            # print(f"DEBUG: adding {data[i]} - total value = {result} remaining space = {remain}")
        i += 1

    return result, result_list, total_weight - remain


t_weights = [10, 20, 30, 5, 20]
t_values = [60, 100, 120, 30, 600]
bp_total_weight = 50

res = backpack_greedy(weights=t_weights, values=t_values, total_weight=bp_total_weight)
print(f"==> total value: {res[0]}, backpack: {res[1]} backpack weight: {res[2]} <==")
