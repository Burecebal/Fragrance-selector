# Fragrance-selector for windows
Fragrance-selector lets you add the name of a fragrance and then it automatically gets the seasons and day/night ratings of that fragrance from the fragrantica.com site. You can then randomize the fragrances for your specific season or time of day. 
The randomize uses algorithms which take the number of votes, seasons percentages and day/night percentages. The result of the randomize can be sent to your email. 
NOTE: This represents a project to hone and show my python skills and also to satisfy my problem of not being able to decide what perfume to wear. :D

More updates will be made for this. For example, adding a  Graphical User Interface and compatibility for other systems other than Windows.

PART I - Adding a fragrance

If you decide to add a fragrance, you will be asked to add the full name of it. Adding the full name will ensure that the correct perfume is selected and it will avoid any potential errors.
After adding the name, you will be asked if you want to automatically(A) or manually (M) add the ratings.
If you decide to manually add, you will be given the URL to the perfume site and asked one by one to add the ratings for seasons and votes.
The ratings are determined by the lenght of the chart. EX: If winter has half the chart full, then it is 50. If day has almost full chart it is 98 and so on.
If you decide to automatically add, then the selenium module will be used to extract the ratings and votes. NOTE: To use this option you will need to have the lastest version of Chrome installed.
After getting the info for the fragrances, a json will be saved in the same directory as the .exe. This json contains the added fragrances, so do not delete.

PART II - RANDOMIZE

Choosing the random option will make the program ask you day or night and which season. Once added, the application will print the fragrance.
How the randomizer works:
The ratings for the chosen season and time of day are added. Ex: You choose night and fall. The program takes the night ratings and adds it to the fall rating. If Sauvage has night: 76 and fall: 89 then the result will be 165.
The votes are also taken in consideration. For a fragrance with less then 250 votes, the result is only 25% of ratings sum. Between 250 and 500, 33%. Between 500 and 750, 50%. Between 750 and 1000 75%. And over 1000 its 100%.
The final result represent the number of entries in the list. Ex: Sauvage has 145*100% = 145 entries. Hugo Boss has 123*50%=61 entries.
After the randomize is complete, you will be asked if you want to send the result to your email. If yes, you will be asked to enter your email. The email used to do this is a spam one with my name created for this sole purpose. So do not send replies.

PART III - OTHER

You have the choices to also view all your fragrances. The format is not the most refined. Further updates will be made.
You can also delete fragrances if you do not have them anymore. This is possible only if you corectly type the name. One recommandation would be to show all the fragrances and copy exactly the name from there.

