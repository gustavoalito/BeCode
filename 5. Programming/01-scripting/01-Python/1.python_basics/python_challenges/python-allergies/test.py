def allergy(score):
    allergylist = ["cats", "pollen", "chocolate", "tomatoes", "strawberries", "shellfish", "peanuts", "eggs"]
    score = list((bin(score)[2:]).zfill(len(allergylist)))
    for j, i in enumerate(score):
        if i == "1":
            print ("You are allergic to : " + allergylist[j])
            
score = 12
allergy(score)