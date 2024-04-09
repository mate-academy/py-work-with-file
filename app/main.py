def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_out,
          open(report_file_name, "w") as file_in):
        buy = 0
        supply = 0
        for el in file_out:
            actions = el.split(",")[0]

            if actions == "buy":
                buy += int(el.split(",")[-1])
            else:
                supply += int(el.split(",")[-1])

        file_in.write("supply," + str(supply) + "\n")
        file_in.write("buy," + str(buy) + "\n")
        file_in.write("result," + str(supply - buy) + "\n")
