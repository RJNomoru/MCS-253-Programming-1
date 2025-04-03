"""Assignment 1 - MCS253
Creating Python Objects ~ Lists, Tuples, Dictionaries"""

#Due Date - Submit no later than 4:10 pm on Thursday (3rd April 2025)

#Please type in your name in the next line by way of commenting

#Name: Rophie NOMORU

#----------------------------------------------------------------

#Quesiton 1

"""Create a python object to store all the courses you are taking this semester.
You may be required to change a course next week."""

#Answer_code

cyber_yr2_courses = ['Set Theory & Logic (MA 211)','Calculus 1 (MA 221)','Discrete Mathematics 1 (MA 241)',
                     'Data Structure & Algorithm 1 (MCS 251)','Programming 1 (MCS 253)']


#Question 2

"""Store all MCS 253 students ID in a python object. These IDs will be
used for 4 years thus do not change IDs."""

#Answer_code

mcs253_stdID = (202412253,202412245,202412236,202412232,2023314260,2023314233)


#Question 3

"""Since students IDs are a unique identifying number for each student, 

use it as a reference to point to students records. The students records
should consist of full names, gender, DOB,Province of origin & email addresses."""

#Answer_code

Std1_ID202412253 = {'Name':'Junior ROBERT',
                    'Gender':'Male',
                    'DOB':'12-10-2000',
                    'Province of Origin':'JIWAKA PROVINCE',
                    'Email Address':'juniorwalrob127@gmail.com'}

Std2_ID202412245 = {'Name':'Margreth KURI',
                    'Gender':'Female',
                    'DOB':'18-12-1998',
                    'Province of Origin':'JIWAKA PROVINCE',
                    'Email Address':'kurimargreth@gmail.com'}

Std3_ID202412236 = {'Name':'Natasha RICKY',
                    'Gender':'Female',
                    'DOB':'05-07-1998',
                    'Province of Origin':'EASTERN HIGHLANDS PROVINCE',
                    'Email Address':'natashajricky@gmail.com'}

Std4_ID202412232 = {'Name':'Dahan TIMINAI',
                    'Gender':'Male',
                    'DOB':'11-11-2001',
                    'Province of Origin':'WESTERN PROVINCE',
                    'Email Address':'timinaidahan@gmail.com'}

Std5_ID2023314260 = {'Name':'Jonah ALBERT',
                     'Gender':'Male',
                     'DOB':'09-05-2004',
                     'Province of Origin':'CENTRAL PROVINCE',
                     'Email Address':'albertjonah84@gmail.com'}

Std6_ID2023314233 = {'Name':'Rophie NOMORU',
                     'Gender':'Male',
                     'DOB':'19-10-2002',
                     'Province of Origin':'MOROBE PROVINCE',
                     'Email Address':'rophiejosephnomoru191002@gmail.com'}

Student_Records = {202412253:Std1_ID202412253,202412245:Std2_ID202412245,202412236:Std3_ID202412236,
                   202412232:Std4_ID202412232,2023314260:Std5_ID2023314260,2023314233:Std6_ID2023314233}


#Question 4

"""Using indexing, print out your favorite course for the sem (refer to Q1)"""

#Answer_code

print(cyber_yr2_courses[4])


#Question 5

"""Print out only your student ID from Q2"""

#Answer_code

print(mcs253_stdID[5])


#Question 6

"""Print out all students records (exclude the IDs)"""

#Answer_code

for record in Student_Records.values():
    print(record)


#Question 7

"""Print out only your student record"""

#Answer_code

print(Student_Records[2023314233])


#Question 8

"""Update the student ID in Q2.
What is the error here?
WHy do you think this happened"""

#Answer_code

mcs253_stdID[0,1,2,3,4,5] = (2023314233,2013314260,202412232,202412236,202412245,202412253)
print("Update Tuple = ",mcs253_stdID[0,1,2,3,4,5])

""""This is a TypeError
Implies that Tuple object does not support item assignment because Tuple are Immutable, which means 
their contents cannot be changed or modified once defined"""

#Question 9

"""Print out the data types for all the objects you have created so far"""

#Answer_code

print(type(cyber_yr2_courses))
print(type(mcs253_stdID))
print(type(Std1_ID202412253))
print(type(Std2_ID202412245))
print(type(Std3_ID202412236))
print(type(Std4_ID202412232))
print(type(Std5_ID2023314260))
print(type(Std6_ID2023314233))
print(type(Student_Records))


#------end of Assignment
#UPLOAD your completed A1 to your GitHub account. Only share the link with me. 