"""Q3: Word frequency and district-wise complaint grouping."""
import re
from collections import Counter, defaultdict

STOP_WORDS = {"the", "is", "a", "an", "and", "to", "of", "in", "for"}

def tokenize(text):
    return re.findall(r"[a-zA-Z]+", text.lower())

def word_frequencies(complaints):
    counts = {}
    for complaint in complaints:
        for word in tokenize(complaint):
            if word not in STOP_WORDS:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top_k_words(counts, k):
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:max(0, k)]

def group_by_district(records):
    grouped = defaultdict(list)
    for district, complaint in records:
        grouped[district].append(complaint)
    return dict(grouped)

if __name__ == "__main__":
    records = [
        ("Mayiladuthurai", "Need help for crop damage"),
        ("Thanjavur", "Crop damage due to heavy rain"),
        ("Mayiladuthurai", "Need subsidy for seeds"),
        ("Nagapattinam", "Water supply problem for crops"),
    ]
    counts = word_frequencies([text for _, text in records])
    print("Word frequencies:", dict(sorted(counts.items())))
    print("Top 5 words:", top_k_words(counts, 5))
    print("District groups:", group_by_district(records))
    print("Counter comparison:", Counter(w for _, text in records for w in tokenize(text) if w not in STOP_WORDS))
