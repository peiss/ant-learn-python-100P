

def compute_score():
    scores = []
    with open("./student_grade_input.txt") as fin:
        for line in fin:
            line = line[:-1]
            fields = line.split(",")
            scores.append(int(fields[-1]))
    max_score = max(scores)
    min_score = min(scores)
    avg_score = round(sum(scores) / len(scores), 2)
    return max_score, min_score, avg_score


max_score, min_score, avg_score = compute_score()
print(f"max_score={max_score}, min_score={min_score}, avg_score={avg_score}")
