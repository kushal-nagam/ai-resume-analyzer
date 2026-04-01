import re

def analyze_resume(text):
    skills = ["python", "machine learning", "ai", "nlp", "api", "data analysis"]
    
    found_skills = []
    
    for skill in skills:
        if re.search(skill, text.lower()):
            found_skills.append(skill)
    
    return found_skills

resume_text = input("Paste your resume text:\n")

skills_found = analyze_resume(resume_text)

print("\nSkills found in resume:")
for skill in skills_found:
    print("-", skill)

if len(skills_found) < 3:
    print("\nSuggestion: Add more technical skills to improve your resume.")
