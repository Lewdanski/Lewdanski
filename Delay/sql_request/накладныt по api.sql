select * from InputInvoiceData 
join InputInvoice on InputInvoiceData.InvoiceId = InputInvoice.Id
where InputInvoiceData.FormId = 74128511