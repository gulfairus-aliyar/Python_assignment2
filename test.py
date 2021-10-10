from src import*

some_Data = get_Data()
scrapper = getDate_byReq("Ethereum")

# Print out our html
print("Parameter")
print(soup.find_all('p'))
examine = input("Select:")
if examine == 0:
    for j in scrapper:
        print(j)

