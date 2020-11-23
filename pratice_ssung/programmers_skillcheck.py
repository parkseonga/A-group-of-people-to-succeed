# -*- coding: utf-8 -*-

# 1. 숫자가 포함되면 TRUE 포함되어 있지 않으면 FLASE
import re

def solution1(s):
    answer = bool(re.search(r'\d', s)) 
    return answer

solution1("j123")  # 통과와 런타임에러가 같이 나옴.



# 2. 공백을 기준으로 짝수번째는 소문자로, 홀수번째는 대문자로 나타내기
def solution2(s):
    
    answer = ''
    
    blank_list = s.split(" ")
    
    for idx, string in enumerate(blank_list):
        
        for i in range(0,len(string)):
            
            if i%2 == 0:
                string = string[:i] + string[i].upper() + string[i+1:]
            else: 
                string = string[:i] + string[i].lower() + string[i+1:]
                
        blank_list[idx] = string
            
    return " ".join(blank_list) 
     
solution2("try hello world")
      