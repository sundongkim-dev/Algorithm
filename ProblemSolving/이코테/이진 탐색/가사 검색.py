'''
출처: https://school.programmers.co.kr/learn/courses/30/lessons/60060

풀이 시작 시간: 2022-11-22 13:13
풀이 종료 시간: 2022-11-22 13:

시간 제한: 
메모리 제한: 

입력: 

출력: 

제한사항:
words의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
전체 가사 단어 길이의 합은 2 이상 1,000,000 이하입니다.
가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공됩니다.
각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
queries의 길이(검색 키워드 개수)는 2 이상 100,000 이하입니다.
각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하입니다.
검색 키워드는 중복될 수도 있습니다.
각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 '?' 로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며, '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.

풀이: 
1st / ?의 시작 지점과 끝나는 지점을 제외하고 비교하여 구한다.
2nd / 정방향 word와 반대방향 word list 두개를 만들어서 ?를 a와 z로 바꾸었을 때 그 사이에 위치한 값들을 모두 세어준다.

제출 이력:
1st / Fail(효율성 문제)
2nd / Pass

'''
from bisect import bisect_left, bisect_right

def count(arr, left, right):
    leftIdx = bisect_left(arr, left)
    rightIdx = bisect_right(arr, right)
    return rightIdx - leftIdx

def solution(words, queries):
    answer = [0] * len(queries)
    asc_words = [[] for _ in range(100_001)]
    desc_words = [[] for _ in range(100_001)]

    for word in words:
        asc_words[len(word)].append(word)
        desc_words[len(word)].append(word[::-1])
    
    for i in range(100_001):
        asc_words[i].sort()
        desc_words[i].sort()

    for i in range(len(queries)):
        q = queries[i]
        if q[0] != "?":
            answer[i] = count(asc_words[len(q)], 
                                q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            q = q[::-1]
            answer[i] = count(desc_words[len(q)],
                                q.replace('?', 'a'), q.replace('?', 'z'))

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = solution(words, queries)
print(result)
# [3, 2, 4, 1, 0]