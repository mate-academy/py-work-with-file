def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file_data:
        for file_line in file_data:
            file_line = file_line.strip()
            if "," in file_line:
                key, value = file_line.split(",", 1)
                try:
                    value = int(value)
                    if "supply" in key:
                        supply += value
                    elif "buy" in key:
                        buy += value
                except ValueError:
                    print(
                        f"Error in value: {value}, "
                        f"cannot be converted to an integer."
                    )
            else:
                print(f"Invalid string format: {file_line} ")

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
