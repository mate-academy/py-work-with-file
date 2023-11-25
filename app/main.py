def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "a") as file_out):
        for line in file_in.readlines():
            splited = line.split(",")
            if len(splited) == 2:
                operation_type = splited[0]
                amount = int(splited[1][:-1])
                if operation_type == "supply":
                    supply += amount
                if operation_type == "buy":
                    buy += amount
        file_out.write(f"supply,{supply}\n")
        file_out.write(f"buy,{buy}\n")
        file_out.write(f"result,{supply - buy}\n")
