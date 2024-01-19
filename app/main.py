def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_in,\
         open(report_file_name, "w") as file_out:
        dictionary = {"supply": 0, "buy": 0, "result": 0}
        for line in file_in.readlines():
            d_name, d_number = line.split(",")
            dictionary[d_name] += int(d_number)
        dictionary["result"] = dictionary["supply"] - dictionary["buy"]
        for d_name, d_number in dictionary.items():
            file_out.write(f"{d_name},{d_number}\n")
