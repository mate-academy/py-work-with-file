import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file
          ):
        data = csv.reader(data_file)
        for line in data:
            if line:
                operation = line[0]
                amount = int(line[1])

                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount

        result = supply - buy

        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
