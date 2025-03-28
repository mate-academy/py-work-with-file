import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file_read:
        csv_reader = csv.reader(file_read)
        for i in csv_reader:
            if i[0] == "supply":
                supply += int(i[1])
            elif i[0] == "buy":
                buy += int(i[1])
        result = supply - buy
    with open(report_file_name, "w") as file_write:
        file_write.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
