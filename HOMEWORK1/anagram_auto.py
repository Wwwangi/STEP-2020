#Load dictionary data
import pandas as pd
data = pd.read_csv('dic.txt')

#Prepare sorted dictionary
import numpy as np
dic=np.array(data.values.reshape(1,-1)[0])
sorted_dic=[]
for word in dic:
  word=str(word).lower()
  sorted_word=''.join(sorted(word))
  sorted_dic.append([sorted_word,word])
sorted_dic.sort()

#binary search
def anagram_binary_search(word,sorted_dic):
  anagram=[]
  initial_word=word
  word=''.join(sorted(word))
  #find the left-most position
  l,r=0,len(sorted_dic)-1
  while l<=r:
    mid=(l+r)//2
    if(sorted_dic[mid][0]>=word):
      r=mid-1
    elif(sorted_dic[mid][0]<word):
      l=mid+1
  position_l=l
  #find the right-most position
  l,r=0,len(sorted_dic)-1
  while l<=r:
    mid=(l+r)//2
    if(sorted_dic[mid][0]>word):
      r=mid-1
    elif(sorted_dic[mid][0]<=word):
      l=mid+1
  position_r=r
  #append anagram
  for i in range(position_l,position_r+1):
    if sorted_dic[i][1]!=initial_word:
      anagram.append(sorted_dic[i][1])
  return anagram

#To find all anagram
def all_anagram(word,sorted_dictionary):
  candidates=[""]
  anagram=[]
  for char in word:
    current_candidates=candidates.copy()
    for candidate in current_candidates:
      new_candidate=candidate+char
      anagram_candidate=anagram_binary_search(sorted(new_candidate),sorted_dictionary)
      for item in anagram_candidate:
        if item not in anagram:
          anagram.append(item)
      candidates.append(new_candidate)
  return anagram

#Find the one with highest score
def anagram_with_best_score(anagram):
  lookup={'a':1,'b':1,'d':1,'e':1,'g':1,'i':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1,'c':2,'f':2,'h':2,'l':2,'m':2,'p':2,'v':2,'w':2,'y':2,'j':3,'k':3,'q':3,'x':3,'z':3}
  score=[]
  for word in anagram:
    i=0
    temp=0
    while i<len(word):
      temp+=lookup[word[i]]
      if word[i]!='q':
        i+=1
      else:
        i+=2
    score.append((temp+1)**2)
  res=anagram[score.index(max(score))]
  print('The anagram with the highest score is: '+ res)
  print('The score is: '+ str(max(score)))
  return res

#automation
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://icanhazwordz.appspot.com/')
for i in range(10):
  #to get the characters on the website for each round
  string=[]
  bs = BeautifulSoup(driver.page_source, "html.parser")
  char = bs.findAll('div',{'class':['letter p1','letter p2','letter p3']})
  for c in char:  
    string.append(c.string.lower())
  anagram=all_anagram(string,sorted_dic)
  if anagram:
    chosen_anagram=anagram_with_best_score(anagram)
    print(chosen_anagram)
    driver.find_element_by_id('MoveField').send_keys(chosen_anagram)
    driver.find_element_by_xpath("//input[@value='Submit']").click()
  else:
  	driver.find_element_by_name('pass').click()