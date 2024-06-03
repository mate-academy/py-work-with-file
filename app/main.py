def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        data = {}
        for line in file_in:
            if line == "":
                break
            name, amount = line.split(",")
            if name not in data:
                data[name] = int(amount)
            else:
                data[name] += int(amount)
        data["result"] = data["supply"] - data["buy"]

        file_out.write(f"supply,{data["supply"]}\n")
        file_out.write(f"buy,{data["buy"]}\n")
        file_out.write(f"result,{data["result"]}\n")
