import ijson
import json
import csv
import itertools
import pandas as pd
import numpy as np

# for prefix, theType, value in ijson.parse(open('dev.jsonl', encoding="utf-8"),multiple_values=True):
#     print(prefix)

document_title = []
yes_no_answer = []
question_text = []
full_list = []
short_answer = []
np.random.seed(2015)
df = pd.DataFrame(columns=['document_title', 'question_text'])
token_start_byte = []
token_end_byte = []
start_token = 0
end_token = 0
token_count = 1
token_list = []
short_answers_all =[]
annotation_count = 0
data = {}
df = pd.DataFrame([])


data = ijson.parse(open('dev.jsonl', encoding="utf8"),multiple_values=True)
for prefix, event, value in data:
    if (prefix, event) == ('annotations.item.yes_no_answer', 'string'):
        yes_no_answer.append(value)
        # print(yes_no_answer)
    
    if (prefix, event) == ('document_title', 'string'):
        document_title.append(value)
        print(document_title)
        # data['document_title'] = str(document_title[0])
        # df = df.append({'document_title': document_title, 'question_text': question_text}, ignore_index=True)
    if (prefix, event) == ('question_text', 'string'):
        question_text.append(value)
        print(question_text)
        # data[question_text] = question_text[0]
        # df = df.append({'question_text': question_text}, ignore_index=True)
    if (prefix, event) == ('annotations.item.yes_no_answer', 'string'):
        yes_no_answer.append(value)
    if (prefix, event) == ('annotations.item.short_answers.item.start_byte', 'number'):
        short_answers_all.append(value)

    if (prefix, event) == ('annotations.item.short_answers.item.start_token', 'number'):
        start_token = value

    if (prefix, event) == ('annotations.item.short_answers.item.end_token', 'number'):
        end_token = value

    if((prefix, event) == ('document_tokens.item.token', 'string') ):
        token_count = token_count + 1

        if(start_token <= token_count <= end_token ):
            token = value
            token_list.append(token)
    if((prefix, event) == ('annotations.item.annotation_id', 'number') ):
        short_answers_all.append(token_list)
        token_list = []
    # with open('readme.txt', 'w') as f:
    #     f.write(",".join(str(short_answers_all)))

    if (prefix, event) == ('annotations', 'end_array'):
        listToStr1 = ' '.join([str(elem) for elem in yes_no_answer])
        listToStr2 = ' '.join([str(elem) for elem in short_answers_all])
        df = df.append({'document_title': document_title, 'question_text': question_text,'short_answers':listToStr2, 'yes_no_answer':listToStr1}, ignore_index=True)
        with open('readme.txt', 'w') as f:
            f.write(str(df['short_answers']))

        print(yes_no_answer) 
        print(token_list)
        document_title = []
        question_text = []
        yes_no_answer = []
        short_answer = []
        token_list = [] 
        token_count = 0
        print(token_count)
        short_answers_all = []
        print(short_answers_all)
        annotation_count = annotation_count + 1
        print(annotation_count)
    if(annotation_count>5):
        print(df['short_answers'])
        break


        

        # df[i]['question_text'][i] = question_text
        # full_list = document_title + question_text
        # print(df)l
    # print(full_list)
    # print(document_title) 
    # ab = itertools.chain(question_text, yes_no_answer, question_text)
    # print(list(ab))
