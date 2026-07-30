import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    file1 = open(data_file_name)
    supply = 0
    buy = 0
    for line in file1.readlines():
        text = line.split(",")
        if text[0] == "buy":
            buy += int(text[1])
        else:
            supply += int(text[1])
    file1.close()

    file2 = open(report_file_name, "w", newline="")
    writer = csv.writer(file2)
    writer.writerow(["supply", supply])
    writer.writerow(["buy", buy])
    writer.writerow(["result", supply - buy])
    file2.close()
