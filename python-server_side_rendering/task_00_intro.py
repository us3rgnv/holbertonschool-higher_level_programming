#!/usr/bin/python3
"""
Generate personalized invitation files from a template
"""

import os

def generate_invitations(template, attendees):
    """Generate invitation files for each attendee from a template"""

    # Input type checks
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    # Empty input checks
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        content = template
        # Replace placeholders with actual values or "N/A"
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for key in placeholders:
            value = attendee.get(key) if attendee.get(key) is not None else "N/A"
            content = content.replace(f"{{{key}}}", str(value))

        # Generate output file
        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
