def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as dat:
        dat_file = dat.read()
        dat_file = dat_file.replace(",", " ").replace("\n", " ")
        files = dat_file.split(" ")
        file_dict = {}
        for index in range(len(files)):
            if index == 0 or index % 2 == 0 and files[index] != "":
                if files[index] in file_dict:
                    file_dict[files[index]] += int(files[index + 1])
                else:
                    file_dict[files[index]] = int(files[index + 1])
        file_dict["result"] = file_dict["supply"] - file_dict["buy"]
    with open(report_file_name, "w") as rep:
        rep.write(f"supply,{file_dict['supply']}\n"
                  f"buy,{file_dict['buy']}\n"
                  f"result,{file_dict['result']}\n")
