def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        content = file_in.read().split("\n")
        for i in range(len(content) - 1):
            if "supply" in content[i]:
                number = content[i].split(",")
                supply += int(number[1])
            if "buy" in content[i]:
                number = content[i].split(",")
                buy += int(number[1])

        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply-buy}\n")
