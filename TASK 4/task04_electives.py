"""Q4: Elective registration clash detection using sets."""

def compare_electives(elective_a, elective_b, all_students):
    a, b, all_ids = set(elective_a), set(elective_b), set(all_students)
    return {
        "both": sorted(a & b),
        "exactly_one": sorted(a ^ b),
        "neither": sorted(all_ids - (a | b)),
        "union": sorted(a | b),
    }

if __name__ == "__main__":
    elective_a = ["S001", "S002", "S003", "S003", "S005"]
    elective_b = ["S002", "S004", "S005", "S006"]
    all_students = [f"S{i:03d}" for i in range(1, 9)]
    result = compare_electives(elective_a, elective_b, all_students)
    for key, value in result.items():
        print(key.replace("_", " ").title() + ":", value)
