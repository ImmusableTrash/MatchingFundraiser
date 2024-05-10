import csv

with open('ENTER_CSV_NAME_HERE.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Change these headers to match the questions asked in the form. 
    questionHeaders = ["Email Address",
                       "1. Favorite color",
                       "2. Favorite Movie Genre",
                       "3. Favorite Music",
                       "4. Would you wear sandals and socks at the same time?",
                       "6. How do you replace the toilet paper?",
                       "7. Best place for a first date",
                       "8. Favorite vacation spot?",
                       "9. Favorite Sandwich",
                       "10. Favorite fruit",
                       "11. Favorite Oreo",
                       "12. What shoes do you have on right now?",
                       "13. What do you wear when it is cold out?",
                       "14. Favorite season",
                       "15. Favorite subject",
                       "16. Sleep habits?",
                       "17. Can you speak a foreign language?",
                       "18. Preferred hair color",
                       "19. Favorite old school Disney movie",
                       "20. Where would you prefer to shop?",
                       "21. Who should pay on a date?",
                       "22. What seat do you prefer to sit in during school?",
                       "23. Where do you prefer to sit in class?",
                       "24. Favorite online social media",
                       "25.  Dream Car "]
    
# initializes arrays used for data  
    fullArr = []
    girlArr = []
    guyArr = []
    
# Runs through and sorts the data into the three arrays initialized above. 
    for row in reader:
        temp = []
        mTemp = []
        fTemp = []
        for i in questionHeaders:
            if row["How do you identify? "] == "Female":
                fTemp.append(row[i])
            if row["How do you identify? "] == "Male":
                mTemp.append(row[i])
            temp.append(row[i])
        fullArr.append(temp)
        if row["How do you identify? "] == "Female":
            girlArr.append(fTemp)
        if row["How do you identify? "] == "Male":
            guyArr.append(mTemp)
        

        
# Sorting through array to get 5 top matches from the parameter arr that match the comparator parameter person       
    
def topFive(person, arr):
    returnable = ""
    collect = []
    for comPerson in arr:
        if comPerson != person:
            count = 0
            for i in range(1, len(questionHeaders)):
    
                if person[i] == comPerson[i] :
                    count = count + 1
            collect.append([comPerson[0], count])
        
    for i in range(0,5):
        max = 0
        for num in range(0, len(collect)):
            if collect[num][1] > collect[max][1] and collect[num] != collect[max]:
                max = num
        print("" + str(i + 1) + ". " + str(collect[max][0]) + " at " + str(collect[max][1])  + "/25") # The 25 at the end just finishes the compatability fraction
        collect.pop(max)

# Goes through every respondent and gives the top matches for each. 
for person in fullArr:
    print("\nTop 5 Guys for " + person[0] + ":")
    topFive(person, guyArr)
    print("\nTop 5 Girls for " + person[0] + ":")
    topFive(person, girlArr)
    
    
# Allows for you to search a student by email, and gives their results if it matches. 
while True:
    email = input("\nEnter the email of a student to search for thier results: ")
    search = []
    for person in fullArr:
        if person[0] == email:
            search = person
    if search != []:
        print("\nThe top 5 girls for " + email + " is:")
        topFive(search, girlArr)
    
        print("\nThe top 5 guys for " + email + " is:")
        topFive(search, guyArr)
    else:
        print("\nThe email address provided could not be found within the data. Check the spelling and see if there is a response connected to this email.")
    
    
    


   