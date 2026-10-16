"""Generate a fictional UNF graduating-class CSV for the CONFERRA demo.

Every person in the output is invented. The seed is fixed, so the file is
reproducible. Run from the repo root:

    python scripts/generate_sample_cohort.py
"""
import csv
import random
from pathlib import Path

SEED = 20261014
CONFERRAL = "2026-10-14"
TERM = "Fall 2026"
OUT = Path(__file__).resolve().parent.parent / "samples" / "unf-graduating-class-fall-2026.csv"

# Course codes must match PROGRAMS in index.html.
PROGRAMS = {
    "MSc Data Analytics": {
        "faculty": "School of Data Science",
        "level": "Graduate",
        "courses": ["DAT5010", "DAT5020", "DAT5100", "DAT5200", "DAT5300", "DAT5900"],
        "weight": 22,
    },
    "MBA": {
        "faculty": "Faculty of Business",
        "level": "Graduate",
        "courses": ["MGT6010", "MGT6020", "MGT6030", "MGT6040", "MGT6050", "MGT6900"],
        "weight": 16,
    },
    "BBA": {
        "faculty": "Faculty of Business",
        "level": "Undergraduate",
        "courses": ["BUS1010", "ACC2010", "MKT2100", "FIN3010", "HRM3200", "BUS4900"],
        "weight": 12,
    },
}

GRADES = ["A+", "A", "A-", "B+", "B", "B-", "C+"]
GRADE_WEIGHTS = [6, 22, 22, 20, 15, 9, 6]
GP = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3}

FIRST = [
    "Aisha", "Arjun", "Beatriz", "Callum", "Chidinma", "Daniela", "Dev", "Elif", "Emeka", "Fatima",
    "Gabriel", "Hana", "Ibrahim", "Isabella", "Jiho", "Kavya", "Liam", "Lina", "Mateo", "Mei",
    "Mohammed", "Nadia", "Noah", "Olivia", "Omar", "Parisa", "Rahul", "Riya", "Samuel", "Sana",
    "Simran", "Sophie", "Tariq", "Thanh", "Tomás", "Valentina", "Vikram", "Yara", "Yusuf", "Zoë",
    "Adebayo", "Camille", "Diego", "Grace", "Harpreet", "Ines", "Jun", "Leila", "Marc-André", "Nikhil",
]
LAST = [
    "Adeyemi", "Ahmed", "Banerjee", "Bouchard", "Castillo", "Chowdhury", "Costa", "Dhillon", "Diallo", "Dubois",
    "Eze", "Farouk", "Gagnon", "Gill", "Haddad", "Ibrahim", "Iyer", "Joshi", "Kaur", "Khan",
    "Kim", "Kowalski", "Lam", "Lavoie", "Li", "Malik", "Mensah-Boateng", "Morales", "Nair", "Nguyen",
    "Obi", "Okonkwo", "Oliveira", "Patel", "Pelletier", "Qureshi", "Rahman", "Reddy", "Rossi", "Sandhu",
    "Santos", "Sharma", "Silva", "Tran", "Tremblay", "Vasquez", "Wang", "Yilmaz", "Zhang", "Zhou",
]
CITIZENSHIP = ["International", "International", "International", "Domestic"]


def slug(name: str) -> str:
    return (name.lower().replace(" ", "").replace("-", "")
            .translate(str.maketrans("áàâäéèêëíïóôöúüçñõã", "aaaaeeeeiiooouucnoa")))


def main() -> None:
    rng = random.Random(SEED)
    firsts = rng.sample(FIRST, len(FIRST))
    lasts = rng.sample(LAST, len(LAST))
    program_pool = [p for p, cfg in PROGRAMS.items() for _ in range(cfg["weight"])]
    rng.shuffle(program_pool)

    rows = []
    for i, program in enumerate(program_pool):
        cfg = PROGRAMS[program]
        first, last = firsts[i], lasts[i]
        grades = rng.choices(GRADES, weights=GRADE_WEIGHTS, k=len(cfg["courses"]))
        gpa = sum(GP[g] for g in grades) / len(grades)
        honours = ("With Distinction" if gpa >= 3.8 else "") if cfg["level"] == "Graduate" \
            else ("With Great Distinction" if gpa >= 3.8 else "With Distinction" if gpa >= 3.5 else "")
        rows.append({
            "student_id": f"UNF-2026-{101 + i:03d}",
            "first_name": first,
            "last_name": last,
            "preferred_email": f"{slug(first)}.{slug(last)}@students.unf-sandbox.example",
            "program": program,
            "faculty": cfg["faculty"],
            "level": cfg["level"],
            "citizenship_status": rng.choice(CITIZENSHIP),
            "convocation_term": TERM,
            "conferral_date": CONFERRAL,
            "credits_earned": len(cfg["courses"]) * 3,
            "honours": honours,
            "graduation_status": "Eligible",
            "grades": ";".join(f"{c}:{g}" for c, g in zip(cfg["courses"], grades)),
        })

    rows.sort(key=lambda r: (r["program"], r["last_name"]))
    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} graduates to {OUT}")


if __name__ == "__main__":
    main()
