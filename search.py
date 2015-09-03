#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import math
import json
import sys
import os
import re

OUTPUT = 'output'

re_striptag = re.compile(r'<[^>]+>')

db = dict()
tf = dict()
idf = dict()
titles = dict()

totale_documenti = 0
for root, dirs, files in os.walk(OUTPUT):
    for f in files:
        fullname = os.path.join(root,f)
        if (fullname.endswith('.html')) and not root.lower().endswith('drafts'):
            totale_documenti += 1
            urlname = fullname[len(OUTPUT)+1:].replace('\\','/')
            print fullname.ljust(80),urlname
            content = open(fullname,'rb').read().lower()
            [title for title in re.findall(r'<title>(.*?)</title>', content, re.I|re.S)]
            titles[urlname] = title;
            db[urlname] = { 'content' : content, 'title' : title }
            content = re_striptag.sub('', content)
            for word in re.findall(r'\w{2,}', content):
                if word not in tf:
                    tf[word] = {'occorrenze':0, 'documenti':0}
                tf[word]['occorrenze'] += 1;
            for word in set(re.findall(r'\w{2,}', content)):
                tf[word]['documenti'] += 1;

idf = dict(((word,math.log(float(totale_documenti)/float(tf[word]['documenti']))) for word in tf))
tf = dict(((word,float(tf[word]['occorrenze'])/tf[word]['documenti']) for word in tf))
#opzionale
max_f = max([x for _,x in tf.items()])
tf = dict(((k, 0.5+0.5*v/max_f) for k,v in tf.items()))
#fine opzionale
prod = dict(((word,tf[word]*idf[word]) for word in tf))
words = prod.keys()
#precalcolo
for url in db:
    ret = dict()
    for word in words:
        peso = prod[word]
        cnt = len(re.findall(r'\b'+word+r'\b', db[url]['content'], re.I))
        cnt_title = len(re.findall(r'\b'+word+r'\b', db[url]['title'], re.I))
        cnt_url = len(re.findall(r'\b'+word+r'\b', url, re.I))
        if cnt or cnt_title or cnt_url:
            if cnt:
                dallinizio = 100 - \
                    50 * db[url]['content'].find(word) \
                    / (1+len(db[url]['content']))
            else:
                dallinizio = 100
            score = (cnt + cnt_title * 1.1 + cnt_url * 2) * peso * dallinizio
            if score:
                ret[word] = score
    db[url] = ret

data = { 'db': db, 'words': words, 'titles': titles}

json.dump(
    data,
    open(os.path.join(OUTPUT,'search.json'),'wb')
)

sys.exit()

max_prod = max([int(x*1000) for _,x in prod.items()])
print '---', [(x,y) for x,y in prod.items() if int(y*1000)>=0.8*max_prod]

def spell(term, max=3):
    if term in tf:
        return [(1.0, term)]

    from difflib import SequenceMatcher
    matches = [(SequenceMatcher(None, term, word).ratio(), word) for word in tf]
    if ' ' in term:
        score = 1
        spelled = list()
        for word in term.split():
            spelledword = spell(word, 1)
            if spelledword:
                score *= spelledword[0][0]
                spelled.append(spelledword[0][1])
        matches.append((score,' '.join(spelled)))
    matches.sort()
    matches.reverse()
    return matches[:max]

print spell('vreoprogramatore')
print spell('programatore')
print spell('il vreo programatore')
print spell('il')
print spell('varie anomalie')
print spell('vrie nomalie')

def cerca(terms):
    terms = spell(terms)[0][1]
    #media = sum([x for x,y in cerca]) / len(cerca)
    #sqm = (sum([abs(media - x)**2 for x,y in cerca]) / len(cerca))**0.5
    #cerca = [(x,y) for x,y in cerca if x>(media-sqm)]
    #print 'termini ridotti', cerca
    ret = {}
    for link, words in db.items():
        ret[link] = 0
        for term in terms.split():
            ret[link] += words.get(term,0)

    ret = [(abs(v),k) for k,v in ret.items() if v]
    ret.sort()
    ret.reverse()
    return ret

print '- programmatore'
print cerca('programmatore')[:3]

print '- penna'
print cerca('penna')[:3]

print '- fojonco'
print cerca('fojonco')
