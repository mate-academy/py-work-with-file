def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    summ_supply = 0
    summ_buy = 0

    with open(data_file_name, "r") as f:
        for line in f:
            line = line.strip().split(",")

            if line[0] == "supply":
                summ_supply += int(line[1])
            elif line[0] == "buy":
                summ_buy += int(line[1])
            else:
                pass
        result = summ_supply - summ_buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{summ_supply}\n"
                     f"buy,{summ_buy}\n"
                     f"result,{result}\n")


create_report(
    "apples.csv",
    "report.csv"
)
