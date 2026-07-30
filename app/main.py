import csv


def create_report(data_file_name: str, report_file_name: str) -> object:
    supply = 0
    buy = 0
    result = 0
    with (
        open(data_file_name, "r") as csv_data_file,
        open(report_file_name, "w") as report_file,
    ):
        text = csv.reader(csv_data_file)

        for char in text:
            if "supply" in char:
                supply += int(char[-1])
            if "buy" in char:
                buy += int(char[-1])

        result = supply - buy

        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
