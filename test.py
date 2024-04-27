import json

# JSON data with column headers
json_data = '''
[
  {"Table": "abc", "order date": "1/1/2024", "order ID": 123456},
  {"Table": "abc", "order date": "2/1/2024", "order ID": 123457},
  {"Table": "bcd", "order date": "2/28/2024", "order ID": 123458},
  {"Table": "bcd", "order date": "3/1/2024", "order ID": 123459},
  {"Table": "bcd", "order date": "5/1/2024", "order ID": 123460},
  {"Table": "abc", "order date": "1/1/2024", "order ID": 123461}
]
'''

# Load JSON data
data = json.loads(json_data)

# Create a dictionary to store partitions for each table
table_partitions = {}

# Group the data by the "Table" column
for item in data:
    table = item["Table"]
    order_date = item["order date"]
    # Convert order date to YYYYMMDD format
    parts = order_date.split("/")
    yyyymmdd = parts[2] + parts[0].zfill(2) + parts[1].zfill(2)
    # Add the partition to the dictionary for the corresponding table
    table_partitions.setdefault(table, set()).add(yyyymmdd)
    
# Create JSON structure
json_structure = {
    "type": "full",
    "commitMode": "transactional",
    "objects": []
}

# Populate the JSON structure with unique table-partition combinations
for table, partitions in table_partitions.items():
    json_structure["objects"].append({
        "table": table,
        "partition": sorted(partitions)  # Sort the partitions in ascending order
    })

# Convert to JSON string
json_string = json.dumps(json_structure, indent=2)

print(json_string)
