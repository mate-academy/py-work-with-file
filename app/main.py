def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as source:
        divided = [word.split(",") for word in source.read().split()]
        counter_supply = 0
        counter_buy = 0
        for element in divided:
            if element[0] == "supply":
                counter_supply += int(element[1])
            else:
                counter_buy += int(element[1])
    with open(f"{report_file_name}", "w") as writer:
        writer.write(f"supply,{counter_supply}\n"
                     f"buy,{counter_buy}\n"
                     f"result,{counter_supply - counter_buy}\n")
