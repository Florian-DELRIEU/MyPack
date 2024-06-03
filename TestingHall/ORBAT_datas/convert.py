import csv
import json

# SIDC codes dictionary
sidc_codes = {
    "Corps": "10031000221211000000",
    "Division": "10031000211211000000",
    "Regiment": "10031000171211000000",
    "Artillery": "10031000171303000000",
    "Cavalry": "10031000221213000000",
    "Horse Artillery": "10031000171303030000",
    "Guard": "10031000221211000100",
    "Old Guard": "10031000211211000100",
    "Young Guard": "10031000211211006100",
    "Guard Battery": "10031000171303000100"
}


def create_org(name, sidc, sub_orgs):
    return {
        "options": {
            "uniqueDesignation": name,
            "sidc": sidc
        },
        "subOrganizations": sub_orgs
    }


def parse_csv_to_json(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        org_dict = {}

        for row in reader:
            level = row["Level"]
            name = row["Unit Name"]
            sub_units = row["Subordinate Units"].split(';') if row["Subordinate Units"] else []

            if level == "Corps":
                org_dict[name] = create_org(name, sidc_codes["Corps"], [])
            elif level == "Division":
                parent_name = [key for key, val in org_dict.items() if name in val["options"]["uniqueDesignation"]]
                if parent_name:
                    org_dict[parent_name[0]]["subOrganizations"].append(create_org(name, sidc_codes["Division"], []))
            elif level == "Regiment":
                for key, val in org_dict.items():
                    for sub_org in val["subOrganizations"]:
                        if name in sub_org["options"]["uniqueDesignation"]:
                            sub_org["subOrganizations"].append(create_org(name, sidc_codes["Regiment"], []))

        json_data = {
            "options": {
                "uniqueDesignation": "Grande Armée",
                "sidc": "10031000000000009500"
            },
            "subOrganizations": list(org_dict.values())
        }

        return json_data


# Parse the CSV file and generate JSON
path_to_file = ""
filename_source = "orbat_fra.csv"
filename_target = "orbat_fra_converted.json"

file_path = 'path_to_your_file.csv'
json_data = parse_csv_to_json(path_to_file+filename_source)

# Save the JSON data to a file
output_file_path = path_to_file + filename_target
with open(output_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(json_data, jsonfile, indent=2, ensure_ascii=False)

print(f"JSON data has been written to {output_file_path}")
