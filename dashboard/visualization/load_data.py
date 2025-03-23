import json
import os
from visualization.models import DataPoint

def load_json_data():
    # Get the current app directory
    app_dir = os.path.dirname(os.path.abspath(__file__))  
    
    # Construct the path to the jsondata.json file inside the 'data' folder
    json_file_path = os.path.join(app_dir, 'data', 'jsondata.json')  

    try:
        with open(json_file_path, encoding='utf-8') as f:
            data = json.load(f)
            
            for entry in data:
                DataPoint.objects.create(
                    intensity=entry.get('intensity', 0),
                    likelihood=entry.get('likelihood', 0),
                    relevance=entry.get('relevance', 0),
                    year=entry.get('year', 0),
                    country=entry.get('country', 'Unknown'),
                    topics=entry.get('topics', ''),
                    region=entry.get('region', 'Unknown'),
                    city=entry.get('city', 'Unknown'),
                    sector=entry.get('sector', ''),
                    pest=entry.get('pest', ''),
                    source=entry.get('source', ''),
                    swot=entry.get('swot', ''),
                )
        print("Data loaded successfully!")

    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in jsondata.json")
