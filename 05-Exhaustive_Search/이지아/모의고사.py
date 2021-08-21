def solution(answers):
  
  answer = []
  results = []
  
  c1,c2,c3 = 0
  
  first = [1,2,3,4,5]
  second = [2,1,2,3,2,4,2,5]
  third = [3,3,1,1,2,2,4,4,5,5]
  
  for i in range(len(answers)):
    if answers[i] == first[i%5]:
        c1 += 1
    if answers[i] == second[i%8]:
        c2 += 1
    if answers[i] == third[i%10]:
        c3 += 1
      
  results = [c1, c2, c3] 
  
  for person, score in enumerate(results): 
    if score == max(results): 
      answer.append(person+1) 
      
return answer

  
