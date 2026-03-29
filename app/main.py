from csv import reader


def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        lines = reader(file_in)
        supply = 0
        buy = 0

        for line in lines:
            if line[0] == "supply":
                supply += int(line[1])
            else:
                buy += int(line[1])

        file_out.write(f"supply,{supply}\n")
        file_out.write(f"buy,{buy}\n")
        file_out.write(f"result,{supply - buy}\n")
