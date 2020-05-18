#Load dictionary data
import pandas as pd
data = pd.read_csv('dic.txt')

#Calculate score for one word
def score_cal(word):
  lookup={'a':1,'b':1,'d':1,'e':1,'g':1,'i':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1,'c':2,'f':2,'h':2,'l':2,'m':2,'p':2,'v':2,'w':2,'y':2,'j':3,'k':3,'q':3,'x':3,'z':3}
  i=0
  score=0
  while i<len(word):
    score+=lookup[word[i]]
    if word[i]!='q':
      i+=1
    else:
      i+=2
  score=(score+1)**2
  return score

#Prepare dictionary, calculate score for each word, maintain only one word with highest score
import numpy as np
dic=np.array(data.values.reshape(1,-1)[0])
modified_dic={}
for word in dic:
  word=str(word).lower()
  sorted_word=''.join(sorted(word))
  score=score_cal(word)
  if sorted_word not in modified_dic:
    modified_dic[sorted_word]=[word,score]
  else:
    if score>modified_dic[sorted_word][1]:
      modified_dic[sorted_word]=[word,score]

#given a word, find the anagram with the highest score
def find_anagram(word,modified_dic):
  candidates=[""]
  anagram=''
  current_score=0
  for char in word:
    current_candidates=candidates.copy()
    for candidate in current_candidates:
      new_candidate=candidate+char
      sorted_candidate=''.join(sorted(new_candidate))
      if sorted_candidate in modified_dic and modified_dic[sorted_candidate][1]>current_score:
        anagram=modified_dic[sorted_candidate][0]
        current_score=modified_dic[sorted_candidate][1]
      candidates.append(new_candidate)
  return [anagram,current_score]

#automation
from bs4 import BeautifulSoup
from selenium import webdriver
while True:
  driver = webdriver.Chrome()
  driver.get('https://icanhazwordz.appspot.com/')
  total_score=0
  for i in range(10):
    #to get the characters on the website for each round
    string=[]
    bs = BeautifulSoup(driver.page_source, "html.parser")
    char = bs.findAll('div',{'class':['letter p1','letter p2','letter p3']})
    for c in char:  
      string.append(c.string.lower())
    anagram,score=find_anagram(string,modified_dic)
    if anagram:
      total_score+=score
      driver.find_element_by_id('MoveField').send_keys(anagram)
      driver.find_element_by_xpath("//input[@value='Submit']").click()
    else:
  	  driver.find_element_by_name('pass').click()
  #Record name
  if total_score>2000:
    driver.find_element_by_xpath("//input[@name='NickName']").send_keys('Wanqi Wu')
    driver.find_element_by_xpath("//input[@name='URL']").send_keys('https://github.com/Wwwangi/STEP-2020/blob/master/HOMEWORK1/anagram_auto.py')
    driver.find_element_by_xpath("//input[@id='AgentRobot']").click()
    driver.find_element_by_xpath("//input[@name='Name']").send_keys('Wanqi Wu')
    driver.find_element_by_xpath("//input[@name='Email']").send_keys('wwwangi@moegi.waseda.jp')
    driver.find_element_by_xpath("//input[@value='Record!']").click()
    break
  else:
  	driver.close()
