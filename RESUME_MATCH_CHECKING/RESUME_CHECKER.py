from colorama import Fore, Style

# Read resume text
with open('resume.txt', 'r', encoding='utf-8') as file:
    resume_text = file.read().lower()

# Read job description text
with open('job.txt', 'r', encoding='utf-8') as file:
    job_text = file.read().lower()

# Turn into sets of words
resume_words = set(resume_text.split())
job_words = set(job_text.split())

# Compare
matched = resume_words.intersection(job_words)
not_matched = job_words - resume_words

# Output
print(Fore.GREEN + "Matched skills:", ' '.join(matched))
print(Fore.RED + "Missing skills:", ' '.join(not_matched))
print(Fore.BLUE + "Match percentage:", (len(matched) / len(job_words)) * 100, "%")
print(Style.RESET_ALL,end='')
