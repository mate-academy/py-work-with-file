def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f:
        data = f.read().split("\n")[:-1]

    supply = []
    buy = []
    for obj in data:
        division = obj.split(",")
        if division[0] == "supply":
            supply.append(division[1])
            continue
        buy.append(division[1])

    sum_suply = sum(map(int, supply))
    sum_buy = sum(map(int, buy))
    with open(report_file_name, "w") as f:
        f.write("supply = " + " + ".join(supply) + f" = {sum_suply}\n"
                "buy = " + " + ".join(buy) + f" = {sum_buy}\n"
                f"result = {sum_suply} + {sum_buy} = {sum_suply - sum_buy}\n")
