
cupcake_invoices = open("CupcakeInvoices.csv")  #2 Open the CupcakeInvoices.csv.

#3 Loop through all the data and print each row.
for row in cupcake_invoices :
    print(row)
 
#4 Loop through all the data and print the type of cupcakes purchased.
    print(row[2])
    row= row.rstrip("\n").split(",")
    print(row[2])

#5 Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
    total +=(Int(row[3])*float(row[4]),2)
    print(total)
#6  Loop through all the data, and print out the total for all invoices combined.
    print(total,2)
#7  Close your open file.
cupcake_invoices.close()

