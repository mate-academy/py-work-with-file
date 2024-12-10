def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(f"{data_file_name}.csv", "r") as csv:
        csv_list = csv.readlines()
        supply = 0
        buy = 0
        for cs in range(len(csv_list)):
            csv_list[cs] = csv_list[cs][:-1]
            if "supply" in csv_list[cs]:
                for chair in csv_list[cs]:
                    if chair == ",":
                        supply += int(
                            csv_list[cs][csv_list[cs].index(chair) + 1:])
            if "buy" in csv_list[cs]:
                for chair in csv_list[cs]:
                    if chair == ",":
                        buy += int(
                            csv_list[cs][csv_list[cs].index(chair) + 1:])
        result = supply - buy
        with open(f"{report_file_name}.csv", "w+") as new_csv:
            new_csv.write(f"supply, {supply}\n")
            new_csv.write(f"buy, {buy}\n")
            new_csv.write(f"result, {result}\n")
