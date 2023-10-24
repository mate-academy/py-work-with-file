import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f1, open(report_file_name, "w") as f2:
        f1_csv = csv.reader(f1)
        supply = 0
        buy = 0
        for i in f1_csv:
            if i[0] == "buy":
                buy += int(i[1])
            else:
                supply += int(i[1])
        result = supply - buy
        f2.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
