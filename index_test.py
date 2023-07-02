import ijson
import json
import csv
import itertools
import pandas as pd
import numpy as np
# i = 0

# for prefix, theType, value in ijson.parse(open('dev.jsonl', encoding="utf-8"),multiple_values=True):
#     print(prefix, '---', theType,'---', value)
    # with open ('out.txt', 'w') as f:
    #     f.write(prefix)

    # print(prefix)
    # print(prefix, '---', theType,'---', value)
# while(i<2):
#     for prefix, theType, value in ijson.parse(open('dev.jsonl', encoding="utf8"),multiple_values=True):
#         # print(value)
#         # print(prefix, '---', theType,'---', value)
#         # i = i + 1
#         if(prefix == 'document_title'):
#             print(prefix, '---', theType,'---', value)

# def extract_json(filename):
#     listJ=[]
#     with open(filename, encoding="utf8") as input_file:
#         jsonobj = ijson.items(input_file, 'records.item', use_float=True)
#         jsons = (o for o in jsonobj)
#         for j in jsons:
#             listJ.append(j)
#     return listJ[0:10]

# print(extract_json('dev.jsonl'))

# train_data=[]
# with open('dev.jsonl','r',encoding='utf-8') as j:
#    for line in j:
#            train_data.append(json.loads(line))
#            di = dict()
#            for k, v in di.items():
#             if k == 'kiwi':
#                 print(v)

# user_to_repos = {}

# with open("test.json", encoding="utf8") as f:
#     for record in ijson.items(f, 'earth.europe.item',multiple_values=True):
#         # user = record["annotations"]["annotation_id"]
#         # repo = record["yes_no_answer"]
#         # print(repo)
        # print(record)
        # if user not in user_to_repos:
        #     user_to_repos[user] = set()
        # user_to_repos[user].add(repo)

# data = list(ijson.parse(open('dev.jsonl', 'rb')))
# print(data)
# f.close()

# with open("dev.jsonl", encoding="utf8") as f:
#     for record in ijson.items(f, 'annotations.short_answers.start_byte',multiple_values=True):
#         print(record)

# data = list(ijson.parse(open('dev.jsonl', 'rb'),multiple_values=True))

# european_places = ijson.kvitems(data, 'annotations.item.short_answers.item.end_byte')
# names = (v for k, v in european_places if k == 'name')
# for name in names:
#     print(name)\



# start_token = []
# end_token = []
# doc_token_start = []
# doc_token_end = []
# token = []
# final_token = []

# data = ijson.parse(open('dev.jsonl', encoding="utf8"),multiple_values=True)
# for prefix, event, value in data:
#     if (prefix, event) == ('annotations.item.short_answers.item.start_byte', 'number'):
#         start_token = value
#     if (prefix, event) == ('annotations.item.short_answers.item.end_byte', 'number'):
#         end_token = value
#     if (prefix, event) == ('document_tokens.item.start_byte', 'number'):
#         doc_token_start = value
#     if (prefix, event) == ('document_tokens.item.end_byte', 'number'):
#         doc_token_end = value
#     if (prefix, event) == ('document_tokens.item.token', 'string'):
#         token = value
#     if (prefix, event) == ('document_tokens.item.token', 'string'):
#         token = value
#     if (prefix, event) == ('document_tokens.item.token', 'string'):
#         token = value
#     if ((prefix, event,value) == ('document_tokens', 'start_array',None)):

#         if((int(doc_token_end)<=int(end_token)) & (int(doc_token_start)>=int(start_token))):
#             final_token = str(final_token) + ' ' + str(token)
#             print(final_token)

    
# document_title = []
# yes_no_answer = []
# question_text = []
# full_list = []
# np.random.seed(2015)
# df = pd.DataFrame(columns=['document_title', 'question_text'])
# i = 0


# data = ijson.parse(open('json_test.json', encoding="utf8"),multiple_values=True)
# for prefix, event, value in data:
#     # if (prefix, event) == ('annotations.item.yes_no_answer', 'string'):
#     #     yes_no_answer.append(value)
#     #     print(yes_no_answer)
#     if (prefix, event) == ('document_title', 'string'):
#         document_title.append(value)
#         print(document_title)
#         # df[i]['document_title'] = document_title
#     if (prefix, event) == ('question_text', 'string'):
#         question_text.append(value)
#         print(question_text)
#         # df[i]['question_text'][i] = question_text
        # full_list = document_title + question_text
        # print(df)l
    # print(full_list)
    # print(document_title) 
    # ab = itertools.chain(question_text, yes_no_answer, question_text)
    # print(list(ab))
    i= i+1