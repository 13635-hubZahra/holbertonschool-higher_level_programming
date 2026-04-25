import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Xeta: template setir (string) olmalidir. Verilen tip: {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Xeta: attendees lugetlerden ibaret siyahi (list of dicts) olmalidir.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ['name', 'event_title', 'event_date', 'event_location']

    for index, attendee in enumerate(attendees, start=1):
        personalized_template = template
        
        for placeholder in placeholders:
            value = str(attendee.get(placeholder, "N/A"))
            personalized_template = personalized_template.replace(f"{{{placeholder}}}", value)

        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(personalized_template)
            print(f"Ugurla yaradildi: {filename}")
        except Exception as e:
            print(f"Fayl yaradilarken xeta bas verdi ({filename}): {e}")

template_text = """
Hormetli {name},
Sizi {event_title} tedbirine devet edirik!
Tarix: {event_date}
Mekan: {event_location}
"""

data = [
    {"name": "Ali", "event_title": "Python Seminari", "event_date": "20 May", "event_location": "Baki"},
    {"name": "Leyla", "event_title": "AI Konfransi", "event_location": "Gence"},
    {"name": "Murad", "event_date": "25 Iyun"}
]

generate_invitations(template_text, data)
