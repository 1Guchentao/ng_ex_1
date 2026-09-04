booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

######### EXPECTED OUTPUT #########
""" Event code: EVT-2026
Name: Alice_Wong
Room: ROOM-305
Time: 14:30
Email domain: unimail.edu
VIP tag count: 2
Valid event code: True
Valid username: True
Valid room: True
Valid time: True
Valid email: True """

import re

booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

parts = [part.strip() for part in booking.strip().split('|')]

event_code = parts[0]
name = parts[1].title()
room = parts[2].upper()
time = parts[3]
email = parts[4]
email_domain = email.split('@')[1].lower()
vip_tag_count = parts[5].count('VIP')

valid_event_code = bool(re.match(r"^EVT-\d{4}$", event_code))
valid_username = bool(re.match(r"^[A-Za-z_]+$", parts[1]))
valid_room = bool(re.match(r"^Room-\d{3}$", parts[2], re.IGNORECASE))
valid_time = bool(re.match(r"^\d{2}:\d{2}$", time))
valid_email = bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))

print(f"Event code: {event_code}")
print(f"Name: {name}")
print(f"Room: {room}")
print(f"Time: {time}")
print(f"Email domain: {email_domain}")
print(f"VIP tag count: {vip_tag_count}")
print(f"Valid event code: {valid_event_code}")
print(f"Valid username: {valid_username}")
print(f"Valid room: {valid_room}")
print(f"Valid time: {valid_time}")
print(f"Valid email: {valid_email}")