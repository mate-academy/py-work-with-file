def create_report(data_file_name: str, report_file_name: str) -> None:
    content_dict = {}

    with open(data_file_name, "r") as file_out:
        for line in file_out:
            if line.strip() == "":
                continue

            if content_dict.get(line.split(",")[0]) is None:
                content_dict[line.split(",")[0]] = int(line.split(",")[1])
            else:
                content_dict[line.split(",")[0]] += int(line.split(",")[1])

    with open(report_file_name, "w") as file_in:
        file_in.write(f"supply,{content_dict.get('supply')}\n")
        file_in.write(f"buy,{content_dict.get('buy')}\n")
        file_in.write(f"result,"
                      f"{content_dict.get('supply') - content_dict.get('buy')}"
                      f"\n")
