import stripe


# Input Live key below from Stripe Developer
stripe.api_key = ""

def sendInvoice(email,qty,price,productID,desc):    
  customer = stripe.Customer.create(
    description=desc,
    email=email
  )

  invoice = stripe.Invoice.create(
    customer=customer.id,
    pending_invoice_items_behavior="exclude",
    collection_method="send_invoice",
    days_until_due=7
  )

  invoice_item = stripe.InvoiceItem.create(
    customer=customer.id,
    invoice=invoice.id,
    quantity=qty,
    price_data={
      "currency": "usd",
      "unit_amount": price,
      "tax_behavior": "exclusive",
      "product": productID
    }
  )

  invoice = stripe.Invoice.send_invoice(invoice.id)

  if invoice.status == "open":
        print("Invoice Succesfully sent to:", email)