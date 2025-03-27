def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file_in,\
         open(report_file_name, "w") as file_out:
        content = file_in.read()
        content = content.split("\n")
        sum_supply = 0
        sum_buy = 0
        for i in content:
            i = i.split(",")
            if "supply" == i[0]:
                sum_supply += int(i[1])
            if "buy" == i[0]:
                sum_buy += int(i[1])
        result = f"supply,{sum_supply}\n" \
                 f"buy,{sum_buy}\n" \
                 f"result,{sum_supply - sum_buy}\n"
        file_out.write(result)
