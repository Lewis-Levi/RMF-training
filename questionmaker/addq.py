import json
import sys
import os

numDivs = 0;
selects = []
keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

templatefile = open('./template.html', 'r')
htmldata = templatefile.readlines()
templatefile.close()

questionJSFile = './questions.js'
OutputFile = open(questionJSFile, 'a')

selectJSFile = './selectbutton.js'

# clear all questions first
print('clear questions')
open(questionJSFile, 'w').close()
print('----------------------')

for x in range(1, (len(sys.argv))):
    # if sys.argv[1] == 'clear':
        # open(questionJSFile, 'w').close()
        # print('cleared all questions')
        # break

    questionsetnum = str(os.path.basename(sys.argv[x]))
    print(questionsetnum)

    InputFile = open(sys.argv[x], 'r')
    allLines = InputFile.readlines()
    InputFile.close()

    newLines = []
    for i in allLines:
        newline = i.strip()
        newLines.append(newline)

    try:
        while newLines[-1] == '':
            newLines.pop()
    except:
        print('\tEmpty file: ' + questionsetnum)
        pass

    myQuestions = []

    linecount = 0
    while (True):
            try:
                newLines[linecount]
            except IndexError:
                break;
            
            if newLines[linecount] == 'tf':
                curQuestion = {}
                curQuestion['type'] = newLines[linecount]
                linecount += 1
                curQuestion['question'] = newLines[linecount]
                linecount += 1

                if newLines[linecount] not in ['t', 'f']:
                    print('\tinvalid true or false answer:', questionsetnum)
                    break;

                curQuestion['correctAnswer'] = newLines[linecount]
                myQuestions.append(curQuestion)
                linecount += 2
                continue

            elif newLines[linecount] == 'mc':
                curQuestion = {}
                curQuestion['type'] = newLines[linecount]
                linecount += 1
                curQuestion['question'] = newLines[linecount]
                linecount += 1
                values = []

                try:
                    while (newLines[linecount + 1] != '---' and newLines[linecount + 1] != ''):
                        values.append(newLines[linecount])
                        linecount += 1

                    values.append(newLines[linecount])
                    curQuestion['correctAnswer'] = newLines[linecount]
                    linecount += 2
                    answerBank = dict(zip(keys[0:len(values)-1], values))
                    curQuestion['answers'] = answerBank
                    myQuestions.append(curQuestion)
                    continue;

                except:
                    print('\tno termination char', questionsetnum)
                    break;

            else:
                print('\tinvalid question type:', questionsetnum)
                break;

    myQuestionsJSON = json.dumps(myQuestions)

    OutputFile.write("var q" + questionsetnum + " = " + myQuestionsJSON + ";\n")

    option = '<option value="q' + questionsetnum + '">' + questionsetnum + '</option>'
    selects.append(option)

    numDivs += 1;

    newHtml = './build/' + questionsetnum + '.html'
    allexc = ''.join(htmldata[:15]) + 'show_selected(q' + questionsetnum + ');\n' + ''.join(htmldata[16:])
    newHtmlFile = open(newHtml, 'w')
    newHtmlFile.write(allexc)
    newHtmlFile.close()

selectFile = open(selectJSFile, 'r')
selectFile_data = selectFile.readlines()
selectFile.close()

newFile = open(selectJSFile, 'w')
newFile.write("var numQuestions = " + str(numDivs) + ";\n" + ''.join(selectFile_data[1:6]) + "var selects = " + str(selects) + ";\n"  + ''.join(selectFile_data[7:]))
newFile.close()

OutputFile.close()
print('----------------------')
print('Done')
