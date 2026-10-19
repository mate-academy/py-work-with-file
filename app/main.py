def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as f:
        supply = 0
        buy = 0
        for line in f:
            if line.strip():
                name, number = line.split(",")
                number = int(number)
                if name == "supply":
                    supply += number
                elif name == "buy":
                    buy += number
        with open(report_file_name, "w") as file:
            file.write(f"supply,{supply}\n")
            file.write(f"buy,{buy}\n")
            file.write(f"result,{supply - buy}\n")
