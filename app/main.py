import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_to_read, \
            open(report_file_name, "w") as file_to_write:
        reader = csv.reader(file_to_read)
        count_supply = 0
        count_buy = 0
        for row in reader:
            if row[0] == "supply":
                count_supply += int(row[1])
            if row[0] == "buy":
                count_buy += int(row[1])
        result = count_supply - count_buy
        write_info_1 = ["supply", count_supply]
        write_info_2 = ["buy", count_buy]
        write_info_3 = ["result", result]
        writer = csv.writer(file_to_write, delimiter=",")
        writer.writerow(write_info_1)
        writer.writerow(write_info_2)
        writer.writerow(write_info_3)
