def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        sum_supply = 0
        sum_buy = 0

        for line in data_file:
            if line.startswith("supply"):
                count = line.split(",")[1]
                sum_supply += int(count.strip())
            if line.startswith("buy"):
                count = line.split(",")[1]
                sum_buy += int(count.strip())

        result = (f"supply,{sum_supply}\n"
                  f"buy,{sum_buy}\n"
                  f"result,{sum_supply - sum_buy}\n")
        report_file.write(result)
