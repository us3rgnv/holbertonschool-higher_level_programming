Python Invitation Generator
Overview

This project demonstrates how to generate personalized invitation files from a template using Python.
It uses string templating, file handling, and error handling to create individual output files for a list of attendees.

Features

Replace placeholders in a template ({name}, {event_title}, {event_date}, {event_location}) with actual values.

Handle missing data by substituting "N/A".

Validate input types and handle empty templates or attendee lists gracefully.

Generate sequential output files: output_1.txt, output_2.txt, etc.

Project Structure
python-server_side_rendering/
├── task_00_intro.py
├── main.py (example usage)
├── template.txt
└── output_X.txt (generated)

Requirements

Python 3.x

No external libraries are required.

Template File (template.txt)
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team

Example Attendees List
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

Usage Example
from task_00_intro import generate_invitations

# Read template
with open("template.txt", "r", encoding="utf-8") as file:
    template_content = file.read()

# Call function
generate_invitations(template_content, attendees)


This will create:

output_1.txt for Alice

output_2.txt for Bob

output_3.txt for Charlie (with event_date: N/A)
