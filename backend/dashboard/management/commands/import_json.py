import json
import os
from datetime import datetime
from dateutil import parser  # Import dateutil for flexible date parsing
from django.utils.timezone import make_aware  # Ensure timezone support
from django.core.management.base import BaseCommand
from dashboard.models import DataEntry

class Command(BaseCommand):
    help = "Import JSON data into PostgreSQL"

    def handle(self, *args, **kwargs):
        # Define the absolute path of the JSON file
        json_file_path = r"E:\Data-Visualization-Dashboard\backend\jsondata.json"

        # Check if the file exists
        if not os.path.exists(json_file_path):
            self.stderr.write(self.style.ERROR(f"Error: File not found at {json_file_path}"))
            return

        try:
            # Open file with UTF-8 encoding
            with open(json_file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            entries = []
            for entry in data:
                def parse_date(date_str):
                    """ Convert date string to timezone-aware datetime or return None """
                    if not date_str or date_str.strip() == "":
                        return None
                    try:
                        dt = parser.parse(date_str)
                        if dt.tzinfo is None:  # Convert naive datetime to timezone-aware
                            dt = make_aware(dt)
                        return dt
                    except ValueError:
                        return None  # Skip invalid dates

                def parse_int(value):
                    """ Convert value to int or return None if empty/invalid """
                    if isinstance(value, int):
                        return value
                    if isinstance(value, str) and value.strip().isdigit():
                        return int(value.strip())
                    return None  # Return None if value is empty or non-numeric

                # Append data entry with cleaned values
                entries.append(DataEntry(
                    end_year=parse_int(entry.get("end_year")),
                    intensity=parse_int(entry.get("intensity")),
                    sector=entry.get("sector") or None,
                    topic=entry.get("topic") or None,
                    insight=entry.get("insight") or None,
                    url=entry.get("url") or None,
                    region=entry.get("region") or None,
                    start_year=parse_int(entry.get("start_year")),
                    impact=entry.get("impact") or None,
                    added=parse_date(entry.get("added")),
                    published=parse_date(entry.get("published")),
                    country=entry.get("country") or None,
                    relevance=parse_int(entry.get("relevance")),
                    pestle=entry.get("pestle") or None,
                    source=entry.get("source") or None,
                    title=entry.get("title") or None,
                    likelihood=parse_int(entry.get("likelihood")),
                    city=entry.get("city") or None,
                ))

            # Bulk insert into the database
            DataEntry.objects.bulk_create(entries)
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(entries)} records from {json_file_path}"))

        except UnicodeDecodeError as e:
            self.stderr.write(self.style.ERROR(f"Unicode Error: {e}"))
        except json.JSONDecodeError as e:
            self.stderr.write(self.style.ERROR(f"JSON Error: {e}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Unexpected Error: {e}"))
