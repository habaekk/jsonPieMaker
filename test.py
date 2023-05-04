from tqdm import tqdm
import time

iter = range(365)

for i in tqdm(iter, 
              total = len(iter), ## 전체 진행수
              desc = 'Description', ## 진행률 앞쪽 출력 문장
              ncols = 120, ## 진행률 출력 폭 조절
              ascii = ' =', ## 바 모양, 첫 번째 문자는 공백이어야 작동
              leave = True, ## True 반복문 완료시 진행률 출력 남김. False 남기지 않음.
             ):
    time.sleep(0.01)