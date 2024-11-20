from companyConnect import create_conn
from sqlalchemy import create_engine, text # "Text" is only included with the newest call
import pandas as pd

conn = create_conn()

# create a connection to the database
# We are going to use a formatted string to connect using the lambda function
engine = create_engine("mysql+mysqlconnector://", creator=lambda: conn)

# Set a custom display format for floats
pd.options.display.float_format = '{:,.2f}'.format

# Select records
sql_query = "select Store, Weekly_Sales from sales where Store = 1;"

sql = text(sql_query)

# Execute the query and return the results into a Pandas dataframe
sales_df = pd.read_sql_query(sql, engine)

# Print the results
print(sales_df)

