def sort_dict(original_dict: dict) -> dict:
    sorted_dict = {
        k: v
        for k, v in sorted(
            original_dict.items(), key=lambda item: item[1], reverse=True
        )
    }

    values = list(sorted_dict.values())
    difference = values[0]
    for i in range(1, len(values)):
        difference -= values[i]

    sorted_dict["result"] = difference
    return sorted_dict


def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {}
    lines = []

    with open(data_file_name, "r") as file_in, open(
        report_file_name, "w"
    ) as file_out:
        for line in file_in:
            words = line.split(",")
            if not data.get(words[0]):
                data[words[0]] = int(words[1])
            else:
                data[words[0]] += int(words[1])

        data = sort_dict(data)

        for key, value in data.items():
            lines.append(f"{key},{value}")

        lines.append("")

        file_out.write("\n".join(lines))
