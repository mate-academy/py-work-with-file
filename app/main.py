def create_report(data_file_name: str, report_file_name: str) -> str:
    i_supply = 0
    i_buy = 0
    with open(data_file_name, "r") as file:
        for i in open(data_file_name).read().rsplit("\n"):
            if i.rsplit(";")[0] == "supply":
                i_supply += int(i.rsplit(";")[1])
            elif i.rsplit(";")[0] == "buy":
                i_buy += int(i.rsplit(";")[1])
            with open(report_file_name, "w") as file:
                file.write(
                    str(f"supply,{i_supply}\nbuy,"
                        f"{i_buy}\nresult,{i_supply - i_buy}\n")
                )
            file.close()
    return f"supply,{i_supply}\nbuy,{i_buy}\nresult,{i_supply - i_buy}\n"
