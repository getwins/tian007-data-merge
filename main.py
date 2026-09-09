import pandas as pd
import argparse
from pathlib import Path

# AOMEN_COMPANIES = {
#     1: "澳*",
#     3: "Crow*",
#     4: "立*",
#     8: "36*",
#     12: "易*",
#     14: "伟*",
#     22: "10*",
#     31: "利*",
#     35: "盈*",
#     42: "18*",
# }

# EXCELS = {
#     "titan007_data_3.xlsx": "Crow*", 
#     # "titan007_data_4.xlsx": "立*", 
#     "titan007_data_8.xlsx": "36*", 
#     "titan007_data_12.xlsx": "易*", 
#     "titan007_data_14.xlsx": "伟*", 
#     # "titan007_data_22.xlsx": "10*", 
#     "titan007_data_31.xlsx": "利*", 
#     "titan007_data_35.xlsx": "盈*", 
#     "titan007_data_42.xlsx": "18*" 
# }

# BASEDIR = "D:\\github\\titan007Crawler-\\"
EXCELS = [
    "titan007_data_Crow.xlsx",
    "titan007_data_36.xlsx",
#    "titan007_data_易.xlsx",
    "titan007_data_伟.xlsx",
    "titan007_data_明.xlsx",
    "titan007_data_12.xlsx",
   "titan007_data_利.xlsx",
   "titan007_data_盈.xlsx",
   "titan007_data_18.xlsx"
]

LEAGUES = ["英超", "西甲", "德甲", "意甲", "法甲", "欧冠"]

def get_company_name_from_excel_filename(file_path: Path):
    # Extract the company name from the Excel filename
    # Assuming the filename format is "titan007_data_<company_name>.xlsx"
    # base_name = file_path.split('/')[-1]  # Get the filename without the path
    base_name = file_path.name
    company_name = base_name.replace("titan007_data_", "").replace(".xlsx", "")
    return company_name + "*"

SHIFT_COLS = [
    "联赛",
    "时间",
    "比赛",
    # "状态",
    # "比赛球队-上",
    # "比分",
    # "比赛球队-下"
]

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Combine multiple Excel files into one.")
    parser.add_argument("--basedir", type=str, default='', help="Base directory where the Excel files are located.")
    parser.add_argument("--excels", nargs='*', default=EXCELS, help="List of Excel files to combine.")
    parser.add_argument("--league", nargs='*', default=LEAGUES, help="League to filter the data.")
    parser.add_argument("--output", type=str, default="combined_data.xlsx", help="Output Excel file name.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    df_list = []
    for excel_file in args.excels:
        # file_path = Path(args.basedir + excel_file)
        file_path = Path(args.basedir) / excel_file  # Create a Path object for the Excel file
        if file_path.is_file():
            company_name = get_company_name_from_excel_filename(file_path)
            df = pd.read_excel(file_path)  # Read the Excel file (you can process it as needed)
            df = df.dropna(subset=['联赛']) # Drop rows with any NaN values
            df.insert(loc=6, column="公司", value=company_name)  # Insert the company name as a new column at index 6
            df_list.append(df)
    
    mdf = pd.concat(df_list, axis=0, ignore_index=True)  # Concatenate all DataFrames into one
    mdf = mdf[mdf['状态'] == "未"]  
    new_col = mdf['比赛球队-上'] + " VS " + mdf['比赛球队-下']  # Create a new column '比赛' by combining two existing columns
    mdf.insert(loc=2, column="比赛", value=new_col)  # Insert the new '比赛' column at index 3
    mdf = mdf.drop(columns=["状态", "比赛球队-上", "比分", "比赛球队-下", 
                      "赔率变动", "盘口变动", "赔率变动-大", "盘口变动-大"])  
    mdf.sort_values(by=["比赛"], ascending=[False], inplace=True)  # Sort by company and date
    # mdf = mdf[mdf['联赛'] in ["英超", "西甲", "德甲", "意甲", "法甲", "欧冠", "欧联"]]
    mdf = mdf[mdf['联赛'].isin(args.league)]  # Filter rows based on the specified leagues

    target_cols = SHIFT_COLS
    # 核心逻辑：标记target_cols里，和上一行两列同时完全重复的行
    # keep='first' 意思是保留第一行不标记，后续所有连续重复行都返回True
    mask = mdf.duplicated(subset=target_cols, keep='first')
    # 把标记为重复的行，对应的target_cols字段全部置为NaN
    mdf.loc[mask, target_cols] = pd.NA

    mdf.to_excel(args.output, index=False) 
  

