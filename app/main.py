import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name) as file_to_read:
        for line in file_to_read:
            operation, amount = line.split(",")
            if operation == "buy":
                buy += int(amount)
                continue
            supply += int(amount)
    result = supply - buy
    with open(report_file_name, "a") as file:
        write = csv.writer(file, delimiter=",")
        write.writerow(["supply", supply])
        write.writerow(["buy", buy])
        write.writerow(["result",result])
