def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as r:
        file_in = r.read()
        new_list = []
        for i in file_in.split("\n"):
            new_list.append(i.split(","))
        supply = 0
        buy = 0
        for i in range(len(new_list)):
            if len(new_list[i]) > 1 and new_list[i][0][0] == "s":
                supply += int(new_list[i][1])
            if len(new_list[i]) > 1 and new_list[i][0][0] == "b":
                buy += int(new_list[i][1])
        with open(report_file_name, "w") as e:
            e.write(f"supply,{str(supply)}\nbuy,"
                    f"{str(buy)}\nresult,{str(supply - buy)}\n")
