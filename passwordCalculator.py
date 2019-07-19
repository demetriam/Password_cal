userPassword =[ {
"name": "Brice", 
"Instagram" : "BriceistheBest",
"Snapchat": "Fintechfocus101",
"Twitter": "Bricestwitter123" },
{"name":"Ashley",
"Twitter" : "oreo123",
"Chase" : "moneymakesmehappy",
"Linkedin":"networkworks"
}
]
userName = input("What is your name? ")
for currentuser in userPassword:
   if currentuser["name"] == userName:
        userWebsite = input ("What website do you want a password to? ")
        print ("The website is " + userWebsite + " and the password is  " + str(currentuser[userWebsite]))
        enterPassword = input("What is your password? ")
        if currentuser[userWebsite] == enterPassword:
            print("That is correct ! ")
        else:
            print("That password is incorrect")
  
 