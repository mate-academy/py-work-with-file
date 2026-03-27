import csv


def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0
    with open(data_file_name, 'r') as file_input,\
         open(report_file_name, 'w', newline='') as file_output:
        reader = csv.reader(file_input)
        for row in reader:
            if row[0] == "supply":
                supply += int(row[1])
            if row[0] == "buy":
                buy += int(row[1])
        writer = csv.writer(file_output)
        writer.writerow(["supply", str(supply)])
        writer.writerow(["buy", str(buy)])
        writer.writerow(["result", str(supply - buy)])
