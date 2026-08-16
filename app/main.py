def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):

        for line in file_in.readlines():
            operation, number = line.split(",")
            if operation == "supply":
                supply += int(number)
            elif operation == "buy":
                buy += int(number)

        file_out.write(f"supply,{supply}\n")
        file_out.write(f"buy,{buy}\n")
        file_out.write(f"result,{supply - buy}\n")
