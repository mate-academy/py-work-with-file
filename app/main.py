import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r", encoding="UTF-8") as csvfile_read:
        reader = csv.reader(csvfile_read)
        for row in reader:
            if row[0] == "supply":
                total_supply = total_supply + int(row[1])
            if row[0] == "buy":
                total_buy = total_buy + int(row[1])
        rezult = total_supply - total_buy
    
    rezult_rows = [
        ["supply"], total_supply,
        ["buy"], total_buy,
        ["rezult"], rezult

    ]

    with open(report_file_name, "w", encoding="UTF-8") as csvfile_write:
        csvwriter = csv.writer(csvfile_write)
        for row in result_rows:
            csvwriter.writerow(row)
