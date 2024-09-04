With CustomersWithReferralNames as (
SELECT 
    C1.Name AS Employee,
	C1.Id AS CustomerId
    C2.Name AS ReferralName
FROM 
    Customers C1
LEFT JOIN 
    Customers C2 ON C1.Id = C2.Id
)
SELECT INV.ID as InvoiceID , INV.BillingDate, CST.Name,CST.ReferralName
FROM INVOICES INV
LEFT JOIN CustomersWithReferralNames CST ON INV.CustomerId = CST.CustomerId
order by INV.BillingDate

