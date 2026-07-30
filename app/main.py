def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line_elements = line.split(",")
            if line_elements[0] == "supply":
                supply += int(line_elements[1])
            elif line_elements[0] == "buy":
                buy += int(line_elements[1])
            else:
                raise ValueError("Allowed elements are 'supply' or 'buy'.")
        data_file.close()

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")
        report_file.close()
