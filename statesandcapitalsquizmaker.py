capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

from pathlib import Path
import random
questioncount=1
testcount=1

def questionWriter(letter):
    global questioncount
    test=open(Path(directoryLocation),letter)
    key=open(Path(keyLocation),letter)
    answerchoices= random.sample(list(capitals.values()),3)
    if(capitals[states[questioncount-1]] not in answerchoices):
        answerchoices.append(capitals[states[questioncount-1]])
    else:
        x=capitals.copy()
        x.pop(states[questioncount-1])
        anotherChoice=random.sample(list(x.values()),1)
        answerchoices.append(anotherChoice[0])
    random.shuffle(answerchoices)
    test.write(str(questioncount)+". What is the capital of "+states[questioncount-1]+"?\nA. "+answerchoices[0]+"\nB. "+answerchoices[1]+"\nC. "+answerchoices[2]+"\nD. "+answerchoices[3]+"\n\n")
    key.write(str(questioncount)+". "+capitals[states[questioncount-1]]+"\n")
    key.close()
    test.close()
    questioncount+=1

while(testcount<=35):    
    states=random.sample(list(capitals.keys()),35)
    nameOfTest="Test"+str(testcount)+".txt"
    nameOfKey="Key"+str(testcount)+".txt"
    directoryLocation="C:\\Users\\smvya\\OneDrive\\Desktop\\States and capitals test and key\\Tests\\"+nameOfTest
    keyLocation="C:\\Users\\smvya\\OneDrive\\Desktop\\States and capitals test and key\\Keys\\"+nameOfKey
    while(questioncount<=35):
        if(questioncount==1):
            questionWriter("w")
        else:
            questionWriter("a")
    print(testcount)
    testcount+=1
    questioncount=1
    
