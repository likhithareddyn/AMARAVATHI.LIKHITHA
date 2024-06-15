import pandas as pd

customers_df = pd.read_csv('/Users/likhithanarapareddy/Downloads/Customers.csv')
transactions_df = pd.read_csv('/Users/likhithanarapareddy/Downloads/Transaction.csv')
course_df = pd.read_csv('/Users/likhithanarapareddy/Downloads/Studies.csv')
courses_df = pd.read_csv('/Users/likhithanarapareddy/Downloads/Software.csv')

merged_df = pd.merge(customers_df, transactions_df, on='customer_id')

merged_df['start_date'] = pd.to_datetime(merged_df['start_date'], format='%d-%m-%Y')
merged_df['end_date'] = pd.to_datetime(merged_df['end_date'], format='mixed' ,errors='coerce')
merged_df['duration'] = (merged_df['end_date'] - merged_df['start_date']).dt.days

merged_df.drop_duplicates(inplace=True)

merged_df.dropna(inplace=True)

average_duration = merged_df.groupby('customer_id')['duration'].mean()

unique_transaction_types = merged_df['txn_type'].unique()

region_to_continent = {
    1: 'Asia',
    2: 'Europe',
    3: 'North America',
    4: 'South America',
    5: 'Australia',
    6: 'Africa'
}
merged_df['continent'] = merged_df['region_id'].map(region_to_continent)
transaction_type_count = merged_df.groupby(['continent', 'txn_type']).size()

pascal_avg_selling_cost = courses_df[courses_df['DEVELOPIN'] == 'PASCAL']['SCOST'].mean()

dap_course_names = course_df[course_df['COURSE'] == 'DAP']['PNAME']

lowest_course_fee = courses_df['SCOST'].min()

recovered_packages = courses_df[courses_df['SCOST'] >= courses_df['DCOST']]

costliest_basic_dev = courses_df[courses_df['DEVELOPIN'] == 'BASIC']['DCOST'].max()

programmers_paid_range = len(courses_df[(courses_df['SCOST'] >= 5000) & (courses_df['SCOST'] <= 10000)])

cobol_pascal_programmers = len(courses_df[courses_df['DEVELOPIN'].str.contains('COBOL|PASCAL', regex=True)])

# Display results
print("Average duration of each customer:\n", average_duration)
print("\nUnique transaction types:\n", unique_transaction_types)
print("\nCount of each transaction type with respect to each continent:\n", transaction_type_count)
print("\nAverage selling cost for Pascal packages:\n", pascal_avg_selling_cost)
print("\nNames of those who have done the DAP Course:\n", dap_course_names)
print("\nLowest course fee:\n", lowest_course_fee)
print("\nDetails of packages for which development costs have been recovered:\n", recovered_packages)
print("\nCost of the costliest software development in Basic:\n", costliest_basic_dev)
print("\nNumber of programmers who paid 5000 to 10000 for their course:\n", programmers_paid_range)
print("\nNumber of programmers who know either COBOL or Pascal:\n", cobol_pascal_programmers)
