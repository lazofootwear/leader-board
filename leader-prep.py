#!/usr/local/bin/python3

import sys
import math
import pandas as pd 

args_list = sys.argv
del args_list[0]
filename=args_list[0]

super_dataframe = pd.DataFrame()
outfile="master-clean.csv"


for file in args_list:
  print(file)
  filedata = pd.read_csv(file, low_memory=False)

  # drop function which is used in removing or deleting rows or columns from the CSV files
  filedata.drop('Notes', inplace=True, axis=1)
  filedata.drop('Note Attributes', inplace=True, axis=1)
  filedata.drop('Currency', inplace=True, axis=1)
  filedata.drop('Subtotal', inplace=True, axis=1)
  filedata.drop('Shipping', inplace=True, axis=1)
  filedata.drop('Taxes', inplace=True, axis=1)
  filedata.drop('Discount Code', inplace=True, axis=1)
  filedata.drop('Discount Amount', inplace=True, axis=1)
  filedata.drop('Shipping Method', inplace=True, axis=1)
  filedata.drop('Lineitem requires shipping', inplace=True, axis=1)
  filedata.drop('Lineitem taxable', inplace=True, axis=1)
  filedata.drop('Cancelled at', inplace=True, axis=1)
  filedata.drop('Payment Reference', inplace=True, axis=1)
  filedata.drop('Vendor', inplace=True, axis=1)
  filedata.drop('Employee', inplace=True, axis=1)
  filedata.drop('Location', inplace=True, axis=1)
  filedata.drop('Device ID', inplace=True, axis=1)
  filedata.drop('Id', inplace=True, axis=1)
  filedata.drop('Tags', inplace=True, axis=1)
  filedata.drop('Risk Level', inplace=True, axis=1)
  filedata.drop('Source', inplace=True, axis=1)
  filedata.drop('Lineitem discount', inplace=True, axis=1)
  filedata.drop('Tax 1 Name', inplace=True, axis=1)
  filedata.drop('Tax 1 Value', inplace=True, axis=1)
  filedata.drop('Tax 2 Name', inplace=True, axis=1)
  filedata.drop('Tax 2 Value', inplace=True, axis=1)
  filedata.drop('Tax 3 Name', inplace=True, axis=1)
  filedata.drop('Tax 3 Value', inplace=True, axis=1)
  filedata.drop('Tax 4 Name', inplace=True, axis=1)
  filedata.drop('Tax 4 Value', inplace=True, axis=1)
  filedata.drop('Tax 5 Name', inplace=True, axis=1)
  filedata.drop('Tax 5 Value', inplace=True, axis=1)
  filedata.drop('Receipt Number', inplace=True, axis=1)
  filedata.drop('Duties', inplace=True, axis=1)
  filedata.drop('Billing Province Name', inplace=True, axis=1)
  filedata.drop('Payment ID', inplace=True, axis=1)
  filedata.drop('Payment Terms Name', inplace=True, axis=1)
  filedata.drop('Next Payment Due At', inplace=True, axis=1)
  filedata.drop('Billing Name', inplace=True, axis=1)
  filedata.drop('Billing Street', inplace=True, axis=1)
  filedata.drop('Billing Address1', inplace=True, axis=1)
  filedata.drop('Billing Address2', inplace=True, axis=1)
  filedata.drop('Billing Company', inplace=True, axis=1)
  filedata.drop('Billing City', inplace=True, axis=1)
  filedata.drop('Billing Zip', inplace=True, axis=1)
  filedata.drop('Billing Province', inplace=True, axis=1)
  filedata.drop('Billing Country', inplace=True, axis=1)
  filedata.drop('Billing Phone', inplace=True, axis=1)
  filedata.drop('Lineitem name', inplace=True, axis=1)
  filedata.drop('Lineitem price', inplace=True, axis=1)
  filedata.drop('Lineitem compare at price', inplace=True, axis=1)
  filedata.drop('Lineitem sku', inplace=True, axis=1)
  filedata.drop('Lineitem fulfillment status', inplace=True, axis=1)
  filedata.drop('Name', inplace=True, axis=1)
  filedata.drop('Paid at', inplace=True, axis=1)
  filedata.drop('Fulfilled at', inplace=True, axis=1)
  filedata.drop('Accepts Marketing', inplace=True, axis=1)
  filedata.drop('Created at', inplace=True, axis=1)
  filedata.drop('Lineitem quantity', inplace=True, axis=1)
  super_dataframe = super_dataframe.append(filedata)

super_dataframe.to_csv(outfile)
