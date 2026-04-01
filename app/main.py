def create_report(data_file_name: str, report_file_name: str):
    with (open(f"{data_file_name}", "r+") as fr,
          open(f"{report_file_name}", "w") as fw):
        fr_list = fr.readlines()
        dict_to_write = {"supply": 0, "buy": 0}
        for i in range(len(fr_list)):
            if "\n" in fr_list[i]:
                fr_list[i] = fr_list[i][:-1]
            fr_list[i] = fr_list[i].split(",")
            dict_to_write[fr_list[i][0]] += int(fr_list[i][1])
        dict_to_write.update(
            {"result": dict_to_write["supply"] - dict_to_write["buy"]}
        )
        for key, item in dict_to_write.items():
            fw.writelines(f"{key},{item}\n")
