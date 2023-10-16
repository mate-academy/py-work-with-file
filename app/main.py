import pandas as pd


def create_report(data_file_name: str, report_file_name: str) -> None:

    df = pd.read_csv(data_file_name)
    grouped = df.groupby("operation")["amount"].sum()
    result = grouped["supply"] - grouped["buy"]

    with open(report_file_name, "w") as rf:
        rf.write(f'supply,{grouped["supply"]}\nbuy,{grouped["buy"]}\nresult,{result}\n')
