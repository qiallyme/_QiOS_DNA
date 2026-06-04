import csv
import yaml

# File paths
csv_file = 'slug_mapping.csv'  # Your input CSV file
yaml_file = 'slug_mapping.yaml'  # Your output YAML file

# Initialize empty mappings
slug_mapping = {
    "clients": {},
    "entities": {},
    "topics": {}
}

# Function to update the slug mapping from CSV
def update_slug_mapping(csv_file, yaml_file):
    # Read the CSV file
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        # Process each row in the CSV
        for row in csv_reader:
            type_slug = row['Type'].strip().lower()
            slug = row['Slug'].strip().lower()
            full_name = row['Full Name'].strip()

            # Add the slug to the appropriate section
            if type_slug in slug_mapping:
                slug_mapping[type_slug][slug] = full_name
            else:
                print(f"Invalid type '{type_slug}' in CSV. Skipping row.")

    # Write the updated mapping to YAML
    with open(yaml_file, 'w') as yaml_out:
        yaml.dump(slug_mapping, yaml_out, default_flow_style=False)

    print(f"Slug mapping updated and saved to {yaml_file}")

# Call the function to update
update_slug_mapping(csv_file, yaml_file)
