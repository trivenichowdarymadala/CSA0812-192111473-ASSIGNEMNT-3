"""Q7: Merge contacts from multiple devices using normalized phone numbers."""
import re
from collections import defaultdict

def normalize_phone(phone):
    digits = re.sub(r"\D", "", phone or "")
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return digits

def normalize_name(name):
    return " ".join((name or "").lower().split())

def merge_contacts(*sources):
    merged = {}
    name_index = defaultdict(set)
    for source in sources:
        for contact in source:
            phone = normalize_phone(contact.get("phone", ""))
            name = contact.get("name", "").strip()
            if not phone:
                # Keep contacts without phone separate using normalized name and email.
                key = "NO_PHONE:" + normalize_name(name) + ":" + contact.get("email", "").lower()
            else:
                key = phone
            if key not in merged:
                merged[key] = {"name": name, "phones": set(), "emails": set(), "sources": set()}
            entry = merged[key]
            if name and (not entry["name"] or len(name) > len(entry["name"])):
                entry["name"] = name
            if phone:
                entry["phones"].add(phone)
            if contact.get("email"):
                entry["emails"].add(contact["email"].strip().lower())
            if contact.get("source"):
                entry["sources"].add(contact["source"])
            if name:
                name_index[normalize_name(name)].add(key)
    output = []
    for item in merged.values():
        output.append({
            "name": item["name"],
            "phones": sorted(item["phones"]),
            "emails": sorted(item["emails"]),
            "sources": sorted(item["sources"]),
        })
    return sorted(output, key=lambda x: x["name"].lower())

if __name__ == "__main__":
    phone = [{"name": "Dr. Ravi", "phone": "+91 98400 12345", "email": "ravi@example.com", "source": "Phone A"}]
    phone_b = [{"name": "Ravi Kumar", "phone": "9840012345", "source": "Phone B"},
               {"name": "Meena", "phone": "9876543210", "source": "SIM"}]
    print("Merged contacts:")
    for contact in merge_contacts(phone, phone_b):
        print(contact)
