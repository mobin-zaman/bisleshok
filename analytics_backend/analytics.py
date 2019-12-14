import pandas as pd


# def get_columns(DF, SD, ED, bank_categories, column_name1, column_name2):
def get_columns(SD, ED, data_frame_params):
    df = pd.read_csv('all_merged_cleaned_3.csv')
    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y', errors='coerce')
    df.set_index('date', inplace=True)


    empty_df = pd.DataFrame()

    print(data_frame_params)
    a = df.loc[SD:ED, data_frame_params]

    empty_df = empty_df.append(a, ignore_index=False)

    return empty_df

# data_frame_params = ['categories','agent_banking_no_of_agents','cheque_clearing_non_micr_amount_tk_in_crore']


# result = get_columns(df, '2015-04-30', '2015-05-30', 'categories', 'agent_banking_no_of_agents', 'cheque_clearing_non_micr_amount_tk_in_crore')
# result = get_columns(df, '2015-04-30', '2015-05-30',data_frame_params)
# print(result)
