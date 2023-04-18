#!/usr/bin/env python
# coding: utf-8
import re


def listToString(s):
    str1 = " "
    return (str1.join(s))

with open('input.xml', 'r', encoding='utf-8-sig') as input_to_check:
    in_check = input_to_check.readlines()
    ready_check = listToString(in_check)
#   dump interferring attributes
    ready_check = re.sub(r'status="verified"', r'', ready_check)
    ready_check = re.sub(r'type="[^"]+"', r'', ready_check)
#   gather the Tibetan Unicode strings
    terms = re.findall(r'<term\s* xml:lang="bo"\s*>(.+)</term>', ready_check)
#    for lines in ready_check:
#        if '<term xml:lang="bo">' in line:
#            term = re.sub(r'.*<term xml:lang="bo">(.+)</term>.*', r'\1', line)
#            terms.append(term)

# re.sub(r'<tei:milestone xml:id="UT22084-\d+-\d+-\d+"/>', '', tm)

with open('source.txt', 'r', encoding='utf-8-sig') as checker:
    to_check = checker.readlines()
    source2 = listToString(to_check)
    source = re.sub(r'{{page:{number:\d+,folio:\d+[ab],volume:\d+}}}', r'', source2)

with open('not_in_source.txt', 'w', encoding='utf-8-sig') as writer:
    for trm in terms:
        trm = trm.rstrip()
        trm = trm.rstrip('།')
        trm = trm.rstrip('་')
        if trm in source:
            trm = ''
        else:
            trm += '\n'
        writer.write(trm)
