from collections import defaultdict


INF = float('inf')
COST_MAX = 1000000000
N, M = map(int, input().split())
material_costs = defaultdict(int)
material_costs['LOVE'] = INF
for _ in range(N):
    material, cost = input().split()
    material_costs[material] = int(cost)

complex_materials = defaultdict(list)
for _ in range(M):
    material, expression = input().split('=')
    partitions = expression.split('+')
    if material_costs[material] == 0:
        material_costs[material] = INF

    express_dict = defaultdict(int)
    for partition in partitions:
        n, name = int(partition[0]), partition[1:]
        if material_costs[name] == 0:
            material_costs[name] = INF
        express_dict[name] += n
    complex_materials[material].append(express_dict)

for _ in range(M):
    for material in complex_materials.keys():
        for expression in complex_materials[material]:
            cost = sum([material_costs[name] * val for name, val in expression.items()])
            material_costs[material] = min(material_costs[material], cost)
print(-1 if material_costs['LOVE'] == INF else min(COST_MAX + 1, material_costs['LOVE']))
