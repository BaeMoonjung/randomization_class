import pandas as pd
import random
from string import ascii_uppercase

seed_n = int(input("임의의 숫자 9자리를 입력하세요:"))
participant_n = int(input("시험 대상자 수를 입력하시오:"))
group_n = int(input("시험 그룹 수를 입력하시오:"))
parallel = int(input("직렬 투약인 경우 1, 병렬 투약인 경우 2를 입력하시오:"))

alphabet_list = list(ascii_uppercase)
randomization_n=[]
randomization_group = []

# 무작위 배정 번호 생성

class randomization():
    def __init__(self, seed_n, participant_n, group_n, parallel):
        self.seed_n = seed_n
        self.participant_n= participant_n
        self.group_n = group_n
        self.parallel = parallel
        self.alphabet_list = alphabet_list
        self.randomization_n = randomization_n
        self.randomization_group = randomization_group
        
    def studyRandom(self):
        # 직렬인 경우 무작위 번호 생성

        if self.parallel == 1:
            for i in range(self.participant_n):
                s = "R" + str(101+i)
                self.randomization_n.append(s)    
            
            # 시험군 수에 따른 그룹 설정    
            
            for i in range(self.group_n):
                g = self.alphabet_list[i]
                self.randomization_group.append(g)

            self.randomization_group = self.randomization_group*int(self.participant_n/self.group_n)
                
            # 무작위 배정

            random.seed(self.seed_n)
            random.shuffle(self.randomization_group)

            df = pd.DataFrame({"무작위 번호":self.randomization_n, "투여군": self.randomization_group})
            df.to_excel("randomization.xlsx")
            print(df)

        # 병렬인 경우 무작위 번호 생성       
                
        if self.parallel == 2:
            for i in range(int(self.participant_n/2)):
                s = "R" + str(101+i)
                self.randomization_n.append(s)
            for i in range(int(self.participant_n/2)):
                s = "R" + str(201+i)
                self.randomization_n.append(s)
            
            # 시험군 수에 따른 그룹 설정          
            
            for i in range(int(self.group_n)):
                g = self.alphabet_list[i]
                self.randomization_group.append(g)

            self.randomization_group = self.randomization_group*int(self.participant_n/group_n)
                    
            # 무작위 배정

            random.seed(self.seed_n)
            random.shuffle(self.randomization_group)

            df = pd.DataFrame({"무작위 번호":self.randomization_n, "투여군": self.randomization_group})
            df.to_excel("randomization.xlsx")
            print(df)
            
yjrandomization = randomization(seed_n, participant_n, group_n, parallel)
yjrandomization.studyRandom()
