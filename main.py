from strInvoice import sendInvoice

price=int(input("What Price? ex. $1 = 100 : "))
productID=input("Stripe Product ID? ex. prod_###### : ")
desc=input("Reference Description? (Not customer facing) : ")
path=input("Drag .txt file here or paste path: ")

# If file is dragged will remove qoutes
if path[:1] == "'" :
  x=len(path)
  path=path[1:]
  path=path[:x-2]

with open(path,"r") as txt:
  for line in txt:
        line = line.split(":")
        line[1] = line[1].strip()
        email = line[0]
        qty = line[1]
        sendInvoice(email,qty,price,productID,desc)
