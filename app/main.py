def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as file_in, open(report_file_name, "w") as file_out:
        data = file_in.readlines()
        supply = 0
        buy = 0
        for line in data:
            line = line.split(",")
            if line[0] == "supply":
                supply += int(line[1])
            if line[0] == "buy":
                buy += int(line[1])

        result = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
        file_out.write(result)
