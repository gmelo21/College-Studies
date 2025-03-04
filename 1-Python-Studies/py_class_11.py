import json


def print_family_names(family_member, level=0):
    print(' | ' * level + family_member['name'])

    if 'children' in family_member:
        for child in family_member['children']:
            print_family_names(child, level + 1)


family_tree_json = '''
[
  {
    "name": "Chrom",
    "children": [
      {
        "name": "Lucina",
        "children": [
            {
                "name": "Morgan"
            }
        ]
      }
    ]
  },
  {
    "name": "Lissa",
    "children": [
      {
        "name": "Owain"
      }
    ]
  },
  {
    "name": "Emmeryn"
  }
]
'''

family_tree = json.loads(family_tree_json)
print()

for index, family in enumerate(family_tree):
    print_family_names(family)
    if index < len(family_tree) - 1:
        print(" | ")
