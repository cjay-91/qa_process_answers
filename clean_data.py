import ijson
import json
import csv
import itertools
import pandas as pd
import numpy as np
import re

#code to check 
# for prefix, theType, value in ijson.parse(open('dev.jsonl', encoding="utf-8"),multiple_values=True):
#     print(prefix)

document_title = []
yes_no_answer = []
question_text = []
full_list = []
short_answer = []
np.random.seed(2015)
token_start_byte = []
token_end_byte = []
start_token = 0
end_token = 0
token_count = 0
token_list = []
short_answers_all =[]
annotation_count = 0
data = {}
df = pd.DataFrame([])
token_location = []
all_tokens = []
short_answer_count = []
token_dict= {}

#read data from json file(Used ijson parse to read data row by row to avoid getting all data to memory by other json readers)
data = ijson.parse(open('dev.jsonl', encoding="utf8"),multiple_values=True)
for prefix, event, value in data:

    #get yes,no answer column
    if (prefix, event) == ('annotations.item.yes_no_answer', 'string'):
        yes_no_answer.append(value)
    
    #get document_title column
    if (prefix, event) == ('document_title', 'string'):
        document_title.append(value)
        print(document_title)

    #get question_text column
    if (prefix, event) == ('question_text', 'string'):
        question_text.append(value)
        print(question_text)

    if (prefix, event) == ('annotations.item.yes_no_answer', 'string'):
        yes_no_answer.append(value)
    
    #start code get short_answer column

    #getting all token locations to an array due to multiple short answers
    if (prefix, event) == ('annotations.item.short_answers.item.end_token', 'number'):
        end_token = value
        token_location.append(end_token)
        token_count = 0

    if (prefix, event) == ('annotations.item.short_answers.item.start_token', 'number'):
        start_token = value
        token_location.append(start_token)
    
    #get all token names by count
    if((prefix, event) == ('document_tokens.item.token', 'string') ):   
        token_count = token_count + 1
        token_dict[token_count] = value


    if (prefix, event) == ('annotations', 'start_array'):
        all_tokens.append(token_list)
        token_list = []

    #loop through the token location array and get all short answers to an array
        i=0
        while((i<len(token_location))):
            for key, value in token_dict.items():
                    if(len(token_location)>=2):
                        if(token_location[i+1] <= key <= token_location[i]):
                            token = value 
                            token_list.append(token)
                            token_count = 0
            token_list = ' '.join([str(elem) for elem in token_list])
            short_answer_count.append(token_list)
            token_list = []
            i = i+2

        #remove ','s and append the list items in to a sentence
        listToStr1 = ' '.join([str(elem) for elem in yes_no_answer])

        #add '==' as the separator between multiple short answers.
        listToStr2 = '=='.join([str(elem) for elem in short_answer_count])

        #remove html tags
        CLEANR = re.compile('<.*?>') 
        listToStr2 = listToStr2.replace("<[^>]*>", "")

        #create data frame using created lists
        df = df.append({'document_title': document_title, 'question_text': question_text,'short_answers':listToStr2, 'yes_no_answer':listToStr1}, ignore_index=True)

        print(yes_no_answer) 
        print(token_list)
        short_answer_count = []
        token_dict = {}
        all_tokens.append(token_list)
        token_list = []
        document_title = []
        question_text = []
        yes_no_answer = []
        short_answer = []
        token_location = []
        all_tokens = []
        token_count = 0

        print(token_count)
        short_answers_all = []
        print(short_answers_all)
        annotation_count = annotation_count + 1
        print(annotation_count)

    #used only 100 rows to avoid front end issues due to high number of columns. Can change the number of rows by changing annotation_count
    if(annotation_count>=7830):
        print(df['short_answers'])

        #split short answers column in to multiple sentences using sentence separator.
        df = pd.concat([df['document_title'], df['question_text'],df['short_answers'].str.split('==', expand=True),df['yes_no_answer']], axis=1)
        print(df)

        #convert the dataframe in to a json array
        data = df.to_json(orient = 'records')

        # Writing the json file to a file (data.json)which will be used to create the table by React front end.
        with open("data.json", "w") as outfile:
            outfile.write(data)
        break

