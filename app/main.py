def create_report(data_file_name: str,
                  report_file_name: str):
    short = 0
    long = 0

    with open(data_file_name, "r") as file:
        seb = file
        for i in seb:
            if "supply" in i.split(",")[0]:
                short += int(i.split(",")[1])
            if "buy" in i.split(",")[0]:
                long += int(i.split(",")[1])

    with open(report_file_name, "w") as out:
        out.write(f"supply,{short}\n"
                  f"buy,{long}\n" f"result,{short - long}\n")
