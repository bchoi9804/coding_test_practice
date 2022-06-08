class Node:
    def __init__(self, item): # 노드 생성
        self.data = item # 노드 값
        self.next = None # 다음 노드를 가리키는 주소

class LinkedList: 
    def __init__(self): # 연결리스트 생성
        self.nodeCount = 0 # 노드 갯수
        self.head = None # 시작 노드
        self.tail = None # 끝 노드

    def getAt(self, pos): #노드 위치 메서드
        if pos < 1 or pos > self.nodeCount: # 위치가 1보다 작거나 총노드갯수보다 크다면
            return None # 위치가 없다?
        i = 1 # 시작 인덱스 1
        curr = self.head # 현재위치 = 시작 노드
        while i < pos: # 현재 위치가 인덱스보다 작은 동안 반복
            curr = curr.next # 현재위치에 다음노드를 가리키는 주소를 저장
            i += 1 # 인덱스 증가
        return curr # 다음 노드의 위치를 반환

    def traverse(self): # 리스트 순회 메서드
        curr_node = self.head # 현재 노드에 시작노드를 저장
        L_list_data = []
        while curr_node.next != None: # 다음 노드를 가리키는 링크가 없을 때까지 = 마지막 노드까지
            L_list_data.apped(curr_node.data) # 현재 노드 데이터값을 빈 리스트에 추가
            curr_node = curr_node.next # 다음 노드로 이동
        return []                                            