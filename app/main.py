import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, newline="") as file1:
        reader = csv.reader(file1)
        data_list = []
        supply = 0
        buy = 0
        for row in reader:
            data_list.append(row)
        for i in range(len(data_list)):
            if data_list[i][0] == "supply":
                supply += int(data_list[i][1])
            if data_list[i][0] == "buy":
                buy += int(data_list[i][1])

    result = supply - buy

    with open(report_file_name, "w", newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=",")
        spamwriter.writerow(["supply", supply])
        spamwriter.writerow(["buy", buy])
        spamwriter.writerow(["result", result])
