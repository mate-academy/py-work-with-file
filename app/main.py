def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as f:
        ghij = f.read()
        hijk = ghij.split("\n")
        sum_supply = 0
        sum_buy = 0
        for elem in hijk:
            temp_lst = elem.split(",")
            if temp_lst[0] == "buy":
                sum_buy += int(temp_lst[1])
            if temp_lst[0] == "supply":
                sum_supply += int(temp_lst[1])
        res = sum_supply - sum_buy
        final_report = f"supply,{sum_supply}\nbuy,{sum_buy}\nresult,{res}\n"

    with open(report_file_name, "w") as repo:
        repo.write(final_report)
