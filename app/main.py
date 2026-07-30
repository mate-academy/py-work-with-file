def create_report(data_file_name: str, report_file_name: str) -> None:
    dictionary = {}
    with (
        open(data_file_name, "r") as source,
        open(report_file_name, "w") as result
    ):
        for line in source:
            data = line.split(",")
            try:
                dictionary[data[0]] += int(data[1])
            except KeyError:
                dictionary[data[0]] = int(data[1])
        dictionary["result"] = dictionary["supply"] - dictionary["buy"]
        dictionary = {
            "supply": dictionary["supply"], "buy": dictionary["buy"],
            "result": dictionary["result"]
        }
        for key, value in dictionary.items():
            string = f"{key},{value}\n"
            result.write(string)
