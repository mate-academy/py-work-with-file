def create_report(data_file_name: str, report_file_name: str) -> None:

    with (open(data_file_name, "r") as file_data,
          open(report_file_name, "w") as file_result):
        content = file_data.read()

        csv_list = content.replace("\n", ",").split(",")
        csv_list.pop(len(csv_list) - 1)

        buy = 0
        supply = 0
        result = 0

        for i, buy_data in enumerate(csv_list):
            if buy_data == "buy":
                buy += int(csv_list[i + 1])

        for i, supply_data in enumerate(csv_list):
            if supply_data == "supply":
                supply += int(csv_list[i + 1])

        result = supply - buy

        file_result.write(f"supply,{supply}\n")
        file_result.write(f"buy,{buy}\n")
        file_result.write(f"result,{result}\n")
