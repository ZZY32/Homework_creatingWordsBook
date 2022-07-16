import argparse
#import numpy as np
from random import shuffle
from translate import Translator

# 获取参数size(单词本大小), begin(起始位置), end(终止位置)
parser = argparse.ArgumentParser()

parser.add_argument("size", type = int)
parser.add_argument("-b","--begin", default = -1, type = int)
parser.add_argument("-e","--end", default = -1, type = int)
parser.add_argument("-n","--number", default = 1, type = int)

args = parser.parse_args()

# 打开文件并将单词读入到列表中
#f = open('words.txt','r')

result = [] 
with open('words.txt','r') as f:
    for line in f:
        if line == '\n':
            continue
        if line[-1] == '\n':
            line = line.replace('\n','')
        temp = line.split(', ')
        result.extend(temp)
        #print(temp)


#生成单词文件和翻译文件
index = 0

#如果没有指定单词范围
if args.begin == -1 and args.end == -1:
    while args.number > 0:
        shuffle(result)
        words_count = 0
        with open(f'words_{index}.txt','w') as file_1:
            for words in result:
                if words_count < args.size:
                    file_1.write(words + '\n')
                    words_count = words_count + 1
                else:
                    break
        words_count = 0
        with open(f'translation_{index}.txt','w') as file_2:
            for words in result:
                if words_count < args.size:
                    file_2.write(words.ljust(30,' '))
                    try:
                        file_2.write(Translator(from_lang = 'English', to_lang = 'Chinese').translate(words) + '\n')
                    except RuntimeError:
                        file_2.write('该项目翻译失败\n')
                    words_count = words_count + 1
                else:
                    break
        args.number = args.number - 1
        index = index + 1

#如果指定了单词范围
if args.begin != -1 and args.end != -1:
    part_of_result = result[args.begin:args.end+1]
    while args.number > 0:
        shuffle(part_of_result)
        words_count = 0
        with open(f'words_{index}.txt','w') as file_1:
            for words in part_of_result:
                if words_count < args.size:
                    file_1.write(words + '\n')
                    words_count = words_count + 1
                else:
                    break
        words_count = 0
        with open(f'translation_{index}.txt','w') as file_2:
            for words in part_of_result:
                if words_count < args.size:
                    file_2.write(words.ljust(30,' '))
                    try:
                        file_2.write(Translator(from_lang = 'English', to_lang = 'Chinese').translate(words) + '\n')
                    except RuntimeError:
                        file_2.write('错误:该项目翻译失败\n')
                    words_count = words_count + 1
                else:
                    break
        args.number = args.number - 1
        index = index + 1