import pandas as pd
import numpy as np
from faker import Faker

fake = Faker('en_IN')
Faker.seed(42)
np.random.seed(49)

NUM_RECORDS = 500
GST_RATES = [5, 12, 18, 28]

records = []
for i in range(NUM_RECORDS):
    taxable_amount = round(np.random.uniform(5000, 500000), 2)
    gst_rate = np.random.choice(GST_RATES)
    gst_amount = round(taxable_amount *  gst_rate / 100,2)
    total_amount = round(taxable_amount + gst_amount,2)
    record= {
            'Invoice_Number': f'INV-{1000 + i}',
            'Invoice_Date': fake.date_between(start_date= '-1y', end_date = 'today').strftime('%Y-%m-%d'),
            'Vendor_Name': fake.company(),
            'GSTIN': fake.bothify(text = '##????####?#?#?'),
            'Taxable_Amount': taxable_amount,
            'GST_Rate_%': gst_rate,
            'GST_Amount': round(gst_amount,2),
            'Total_Amount': round(total_amount,2)
            }
    records.append(record)

purchase_register = pd.DataFrame(records)
print(purchase_register.head())

gstr_2a = purchase_register.copy()
rows_to_keep = np.random.choice(np.arange(500), size = 425, replace = False)

gstr_2a = gstr_2a.iloc[rows_to_keep]
print(len(gstr_2a))

no_of_amount_mismatch = int(len(gstr_2a) * 0.10)
mismatch_rows = gstr_2a.sample(no_of_amount_mismatch).index

gstr_2a.loc[mismatch_rows, 'Taxable_Amount'] =round(gstr_2a.loc[mismatch_rows, 'Taxable_Amount']* np.random.uniform(0.95, 1.05),2)

no_of_invoice_wrong_gst_rate = int(len(gstr_2a) * 0.08)
print(no_of_invoice_wrong_gst_rate)
rows_to_choose = gstr_2a.sample(no_of_invoice_wrong_gst_rate).index
gstr_2a.loc[rows_to_choose, 'GST_Rate_%']= np.random.choice(GST_RATES)

gstr_2a = gstr_2a.drop(columns=['Vendor_Name'])

purchase_register.to_csv('../data/raw/purchase_register.csv', index=False)
gstr_2a.to_csv('../data/raw/gstr_2a.csv', index = False)

# df = pd.read_csv('gstr_2a.csv'); print(df.shape)

