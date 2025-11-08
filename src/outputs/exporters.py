thonimport json

def export_to_json(data, filename):
    """
    Exports the scraped data to a JSON file
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data exported to {filename}")