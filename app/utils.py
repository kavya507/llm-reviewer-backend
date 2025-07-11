def extract_pros_cons(text: str):
    pros, cons = [], []
    current = None
    for line in text.splitlines():
        if "pros" in line.lower(): current = "pros"
        elif "cons" in line.lower(): current = "cons"
        elif line.startswith("-") and current:
            (pros if current == "pros" else cons).append(line[1:].strip())
    return pros, cons
