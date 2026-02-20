def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        with open(data_file_name, "r") as f:
            data = f.read()
    except FileNotFoundError:
        return

    try:
        with open(report_file_name, "w") as f:
            f.write(parse(data))
    except FileNotFoundError:
        return


def parse(data: str) -> str:
    word_dict = {}
    elements = data.split()

    for element in elements:
        word, number = element.split(",")
        number = int(number)
        if word in word_dict:
            word_dict[word] += number
        else:
            word_dict[word] = number

    text = ""
    for word in ["supply", "buy"]:
        value = word_dict.get(word, 0)
        text += f"{word},{value}\n"
    result = word_dict.get("supply", 0) - word_dict.get("buy", 0)
    text += f"result,{result}\n"
    return text
