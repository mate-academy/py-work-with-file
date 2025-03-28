def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0

    with (open(data_file_name, "r") as data_file_name,
          open(report_file_name, "a") as report_file_name):

        for line in data_file_name.readlines():
            if line:
                action, amount = line.split(",")
                if "supply" in action:
                    supply += int(amount)
                elif "buy" in action:
                    buy += int(amount)

        result = supply - buy

        report_file_name.write(f"supply,{supply}\n")
        report_file_name.write(f"buy,{buy}\n")
        report_file_name.write(f"result,{result}\n")
