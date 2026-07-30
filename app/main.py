def create_report(data_file_name: str, report_file_name: str) -> None:
    input_file = open(data_file_name, "r")

    supply = 0
    buy = 0

    for line in input_file:
        method, amount = line.split(sep=",")
        if method == "supply":
            supply += int(amount)
        elif method == "buy":
            buy += int(amount)
    input_file.close()

    output_file = open(report_file_name, "w")
    output_file.write(f"supply,{supply}\n")
    output_file.write(f"buy,{buy}\n")
    output_file.write(f"result,{supply - buy}\n")
    output_file.close()
