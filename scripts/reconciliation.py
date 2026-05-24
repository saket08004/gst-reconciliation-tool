import pandas as pd

pr = pd.read_csv('../data/raw/purchase_register.csv')
g2a = pd.read_csv('../data/raw/gstr_2a.csv')

merged = pr.merge(g2a, on='Invoice_Number', how = 'left')

print(merged.shape)
print(merged.columns.tolist())

missing_invoice = merged[merged['GSTIN_y'].isna()]
print(len(missing_invoice))

amount_mismatch = merged[(merged['Taxable_Amount_y'].notna()) & (merged['Taxable_Amount_x'] != merged['Taxable_Amount_y'])]
print(len(amount_mismatch))

gst_rate_mismatch = merged[(merged['GST_Rate_%_y'].notna()) & (merged['GST_Rate_%_x'] != merged['GST_Rate_%_y'])]
print(len(gst_rate_mismatch))

tax_credit_lost = missing_invoice['GST_Amount_x'].sum()
print(f"Total tax credit lost: ₹{tax_credit_lost:,.2f}") 

amount_mismatch['gst_at_risk'] = (amount_mismatch['Taxable_Amount_x'] - amount_mismatch['Taxable_Amount_y']) * amount_mismatch['GST_Rate_%_x'] / 100
total_gst_at_risk = amount_mismatch['gst_at_risk'].sum()
print(f"Total GST at risk from amount mismatches: ₹{total_gst_at_risk:,.2f}")

gst_rate_mismatch['gst_rate_difference'] = (gst_rate_mismatch['Taxable_Amount_y']) * (gst_rate_mismatch['GST_Rate_%_x'] - gst_rate_mismatch['GST_Rate_%_y']) / 100
total_gst_rate_difference = gst_rate_mismatch['gst_rate_difference'].sum()
print(f"Total GST at risk from rate mismatches are: ₹{total_gst_rate_difference:,.2f}")

print("="*50)
print("GST RECONCILIATION SUMMARY")
print("="*50)
print(f"Total invoices in Purchase Register: {len(pr)}")
print(f"Total invoices in GSTR-2A: {len(g2a)}")
print(f"Missing invoices: {len(missing_invoice)}")
print(f"Amount mismatches: {len(amount_mismatch)}")
print(f"GST rate mismatches: {len(gst_rate_mismatch)}")
print("="*50)
print(f"Tax credit lost (missing): ₹{tax_credit_lost:,.2f}")
print(f"GST at risk (amount): ₹{total_gst_at_risk:,.2f}")
print(f"GST at risk (rate): ₹{total_gst_rate_difference:,.2f}")
print("="*50)

# purchase_register.to_csv('purchase_register.csv', index=False)

missing_invoice.to_csv('../data/processed/missing_invoices.csv', index = False)
amount_mismatch.to_csv('../data/processed/amount_mismatch.csv', index = False)
gst_rate_mismatch.to_csv('../data/processed/gst_rate_mismatch.csv', index = False)