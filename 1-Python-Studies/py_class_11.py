import json


def print_family_names(family_member, level=0):
    # Print the name of the current family member with indentation
    print(' | ' * level + family_member['name'])

    # If the family member has children, recursively print their names with increased indentation
    if 'children' in family_member:
        for child in family_member['children']:
            print_family_names(child, level + 1)


# Example JSON family tree
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

# Parse the JSON data
family_tree = json.loads(family_tree_json)
print()

# Call the function to print all family members' names for each family
for index, family in enumerate(family_tree):
    print_family_names(family)
    if index < len(family_tree) - 1:
        print(" | ")
