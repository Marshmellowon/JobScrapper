import csv


def save_to_file(jobs):
    print("save_to 에서 jobs의 타입은: ", type(jobs))
    file = open("jobs.csv", mode="w", encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['title', 'company', 'location', 'link'])
    for job in jobs:
        writer.writerow(job.values())
    return
