#!/usr/local/bin/python3

import sys
import math
import pandas as pd

args_list = sys.argv
del args_list[0]

def isNaN(num):
    return num!= num

# program takes in a csv typically outputted from leader-prep.py, a 2nd file with a list of zips, a spend threshold as a positive or negative number, and a file to output
filename=args_list[0]
zipfilename=args_list[1]
spend=float(args_list[2])
outfilename=args_list[3]

# ziparray is raw
zip_array = []
# read in zips from file:  
with open(zipfilename) as myzipfilename:
    zip_array = myzipfilename.readlines()

# zips to have \n removed
zips = []
for i in zip_array:
    zips.append(i.strip())

# read csv data from file specified on cmd line
data = pd.read_csv(filename, low_memory=False)

# get a unique list of emails to loop through
emails_numpy = data.Email.unique()

#declare a new panda, this is the panda/dataframe that will be written out
customer_spend = pd.DataFrame({"Customer_Email":[],
                               "Customer_Spend":[],
                               "Customer_Name":[],
                               "Customer_Street":[],
                               "Customer_City":[],
                               "Customer_State":[],
                               "Customer_Zip":[]})
                     

customer_spend_by_zip = pd.DataFrame({"Customer_Email":[],
                                      "Customer_Spend":[],
                                      "Customer_Name":[],
                                      "Customer_Street":[],
                                      "Customer_City":[],
                                      "Customer_State":[],
                                      "Customer_Zip":[]})

for email in emails_numpy:
   if not isNaN(email):
#     email="smhughes0906@gmail.com"
     # grab all rows where for email matches
     customer_wNan=data.loc[data['Email'] == email]
     # get rid of all rows with null values for "Financial Status"
     customer_df=customer_wNan.loc[customer_wNan['Financial Status'].notnull()]
     # float for total spent starts at zero and tallies spent minus refunds
     total_spent=float(0)

     #for every row in customer_df
     for index, row in customer_df.iterrows():
        #if Shipping Name is not NaN then use data in that row for name, street, province(state), city, and zip
        if not isNaN(row['Shipping Name']):
          c_name=row['Shipping Name']
          c_street=row['Shipping Street']
          c_province=row['Shipping Province']
          c_city=row['Shipping City']
          # nine digits zips stored as a float, five digit zip stored as a str, pre-pended with a single quote. Fix all that mess.
          c_zip=str(row['Shipping Zip']).replace("'", "")
        #print(c_name)
        # tally up what customer has spent. "paid" adds to customer spend and "refunded" or "partially refunded" subtracts
        if (row['Financial Status'] == "paid"):
           total_spent+=row['Total']
        if (row['Financial Status'] == "refunded" or row['Financial Status'] == "partially_refunded"): 
           total_spent-=row['Total']

     customer_spend.loc[len(customer_spend.index)] = [email, total_spent, c_name, c_street, c_city, c_province, c_zip]

# below logic to check if customer hits spend threshold and if address in list of zip codes
# if so, store in is customer_spend_by_zip panda
for index, row in customer_spend.iterrows():
   if (row['Customer_Spend'] >= spend):
      for zip in zips:
         if (zip in row['Customer_Zip']): 
            c_by_z_email=row['Customer_Email']
            c_by_z_spend=row['Customer_Spend']
            c_by_z_name=row['Customer_Name']
            c_by_z_street=row['Customer_Street']
            c_by_z_city=row['Customer_City']
            c_by_z_state=row['Customer_State']
            c_by_z_zip=row['Customer_Zip']
            customer_spend_by_zip.loc[len(customer_spend_by_zip.index)] = [c_by_z_email, c_by_z_spend, c_by_z_name, c_by_z_street, c_by_z_city, c_by_z_state, c_by_z_zip]


sorted_customer_spend_by_zip=customer_spend_by_zip.sort_values(by='Customer_Spend', ascending=False)
sorted_customer_spend_by_zip.to_csv(outfilename)
