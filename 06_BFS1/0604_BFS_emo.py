from collections import deque

def makeEmoji(start, end):
    visited=[ [-1]*(end+1) for _ in range(end+2)]
    q=deque()
    q.append((start,0,0))

    while(q):
        i,n,c =q.popleft()
        if i<start or i> end+1:continue
        if i==end:
            print(n)
            break

        if visited[i][c]!=-1: continue
        visited[i][c]=n

        q.append((i,n+1,i))
        q.append((i+c,n+1,c))
        q.append((i-1,n+1,c))
    
    
def main():
    end=int(input())
    start=1
    
    makeEmoji(start,end)

if __name__ == "__main__":
    main()

# 영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.

# 영선이는 이미 화면에 이모티콘 1개를 입력했다. 이제, 다음과 같은 3가지 연산만 사용해서
# 이모티콘을 S개 만들어 보려고 한다.

# 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 화면에 있는 이모티콘 중 하나를 삭제한다.

# 모든 연산은 1초가 걸린다. 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다.
# 클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다.
# 또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다.
# 화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.

# 영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 이모티콘을 S개 만들기 위해 필요한 시간의 최솟값을 출력한다.

# 예제 입력 1 2
# 예제 출력 1 2
# 예제 입력 2 4
# 예제 출력 2 4
# 예제 입력 3 6
# 예제 출력 3 5
