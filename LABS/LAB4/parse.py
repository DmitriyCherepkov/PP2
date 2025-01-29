import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

header = f"{'Interface Status':<105}"
separator = "=" * 100
columns = f"{'DN':<50}{'Description':<30}{'Speed':<10}{'MTU':<5}"
print(header)
print(separator)
print(columns)

for item in data['imdata']:
    dn = item['l1PhysIf']['attributes']['dn']
    speed = item['l1PhysIf']['attributes']['speed']
    mtu = item['l1PhysIf']['attributes']['mtu']
    print(f"{dn:<50}{'':<30}{speed:<10}{mtu:<5}")