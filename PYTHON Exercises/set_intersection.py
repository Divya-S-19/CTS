def common_skills(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        return "Invalid input"

    return set1 & set2


skills_a = {"Python", "Java", "SQL"}
skills_b = {"Python", "C++", "SQL"}

result = common_skills(skills_a, skills_b)
print("Common Skills:", result)