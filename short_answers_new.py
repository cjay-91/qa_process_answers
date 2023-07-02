import ijson
import json
import csv
import itertools
import pandas as pd
import numpy as np

# for prefix, theType, value in ijson.parse(open('dev.jsonl', encoding="utf-8"),multiple_values=True):
#     print(prefix)


short_answer = []
np.random.seed(2015)
df = pd.DataFrame(columns=['document_title', 'question_text'])
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
all_tokens =[]
token_list = []

data = ijson.parse(open('dev.jsonl', encoding="utf8"),multiple_values=True)
for prefix, event, value in data:

    if (prefix, event) == ('annotations.item.short_answers.item.end_token', 'number'):
        end_token = value
        token_location.append(end_token)
        # print(start_token)

    if (prefix, event) == ('annotations.item.short_answers.item.start_token', 'number'):
        start_token = value
        token_location.append(start_token)
        # print(end_token)

    if((prefix, event) == ('document_tokens.item.token', 'string') ):
            token_count = token_count + 1
            if(len(token_location)>0):
                # if(int(token_location[1]) <= token_count <= int(token_location[0])):
                #     token = value 
                #     print(token)
                #     token_list.append(token)
                if(start_token <= token_count <= end_token):
                    token = value 
                    token_list.append(token)
                    token_count = 0


    if (prefix, event) == ('annotations.item.annotation_id', 'number'):
        # print(token_location)
        all_tokens.append(token_list)
        token_list = []
        # token_location = []

    # with open('readme.txt', 'w') as f:
    #     f.write(",".join(str(short_answers_all)))

    if (prefix, event) == ('annotations', 'end_array'):
        
        listToStr2 = ' '.join([str(elem) for elem in short_answers_all])
        df = df.append({'short_answers':all_tokens}, ignore_index=True)
        with open('readme.txt', 'w') as f:
            f.write(str(df['short_answers']))
        print(token_location)
        short_answer = []
        token_list = [] 
        token_count = 0
        short_answers_all = []
        token_location = []
        all_tokens = []
        # print(short_answers_all)
        annotation_count = annotation_count + 1
        print(annotation_count)
    if(annotation_count>3):
        print(df['short_answers'])
        
        break


        