import pandas as pd
import time as timer

'''
Created by Jan Kyle Lewis T. Nolasco
'''

def column_splitter(excel_df, column_name, delimiter):
    #prepare export variables
    export_rows=[]

    for index in excel_df.index:
        curr_row=list(excel_df.loc[index])
        if not pd.isnull(excel_df.loc[index, column_name]):
            curr_text=excel_df.loc[index, column_name]
        else:
            curr_text="EMPTY"

        for delimited_text in curr_text.split(delimiter):
            #create copy of curr_row
            append_row=curr_row.copy()
            #append new split text to append_row
            append_row.append(delimited_text)
            export_rows.append(append_row)


    #create export df
    export_df=pd.DataFrame(data=export_rows, columns=list(excel_df.columns)+[column_name+"_split"])
    export_df.to_excel("column_splitter_output.xlsx", index=False)

def main():
    excel_file_name="column_splitter_test.xlsx"
    sheet_name="Sheet1"
    column_name="B"
    delimiter=";"
    dtype={
        column_name: str
    }
    excel_df=pd.read_excel(excel_file_name, sheet_name=sheet_name, dtype=dtype)
    column_splitter(excel_df, column_name, delimiter)

if __name__ == '__main__':
    start=timer.time()
    main()
    end=timer.time()
    total_time=(end-start)/60
    print(f"Elapsed Time: {total_time} mins", )