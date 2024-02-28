def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as incoming_data,
          open(report_file_name, "a") as output_data):
        sum_supply = 0
        sum_buy = 0
        for line in incoming_data:
            line = line.strip().split(",")
            k, v = line
            print(k, v)
            if k == "supply":
                sum_supply += int(v)
            if k == "buy":
                sum_buy += int(v)

        output_data.write("supply,"f"{sum_supply}\n")
        output_data.write("buy,"f"{sum_buy}\n")
        output_data.write("result,"f"{sum_supply - sum_buy}\n")
