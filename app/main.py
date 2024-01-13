def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as start:
        total_supply = 0
        total_buy = 0
        for line in start.readlines():
            if line.split(",")[0] == "supply":
                total_supply += int(line.split(",")[1])
            if line.split(",")[0] == "buy":
                total_buy += int(line.split(",")[1])

        result = total_supply - total_buy

    with open(report_file_name, "a") as end:
        end.write(f"supply,{total_supply}\n")
        end.write(f"buy,{total_buy}\n")
        end.write(f"result,{result}\n")
