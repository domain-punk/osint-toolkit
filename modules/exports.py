import csv
def export_to_csv(data):
    with open('data/exports/results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for k, v in data.items():
            writer.writerow([k, str(v)])
def export_to_pdf(data):
    with open('data/exports/report.pdf', 'w') as f:
        f.write(str(data))
