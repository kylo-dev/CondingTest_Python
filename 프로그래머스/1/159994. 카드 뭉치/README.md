# 나의 문제 풀이
문제를 푸는데 계속 "index of error"가 나서 의문이었다.

```python
for i in range(len(goal)):
  if cards1[0] in goal[i]:
      answer.append(cards1.pop(0))
  elif cards2[0] in goal[i]:
      answer.append(cards2.pop(0))
```
goal 리스트의 크기만큼 cards1과 cards2의 0번째 위치의 단어를 비교했다.같은 단어인 경우 pop()을 하면서 answer 리스트에 추가하는 로직을 짰는데 에러가 났었다.

여러번 반복을 해 보니까 cards1 이나 cards2에 같은 단어를 제거하여 빈 리스트 상태가 됐을 때에도 조건문을 돌 때 "index of error"가 발생한 것이었다.

에러를 피하기 위해서는 

```python
for word in goal:
        if len(cards1) > 0 and cards1[0] == word:
            answer.append(cards1.pop(0))
        elif len(cards2) > 0 and cards2[0] == word:
            answer.append(cards2.pop(0))
        else:
            break
```
다음과 같이 리스트의 크기를 확인해줘야 한다.

---
# [level 1] 카드 뭉치 - 159994 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/159994) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2023년 11월 5일 12:54:13

### 문제 설명

<p>코니는 영어 단어가 적힌 카드 뭉치 두 개를 선물로 받았습니다. 코니는 다음과 같은 규칙으로 카드에 적힌 단어들을 사용해 원하는 순서의 단어 배열을 만들 수 있는지 알고 싶습니다.</p>

<ul>
<li>원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.</li>
<li>한 번 사용한 카드는 다시 사용할 수 없습니다.</li>
<li>카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.</li>
<li>기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.</li>
</ul>

<p>예를 들어 첫 번째 카드 뭉치에 순서대로 ["i", "drink", "water"], 두 번째 카드 뭉치에 순서대로 ["want", "to"]가 적혀있을 때 ["i", "want", "to", "drink", "water"] 순서의 단어 배열을 만들려고 한다면 첫 번째 카드 뭉치에서 "i"를 사용한 후 두 번째 카드 뭉치에서 "want"와 "to"를 사용하고 첫 번째 카드뭉치에 "drink"와 "water"를 차례대로 사용하면 원하는 순서의 단어 배열을 만들 수 있습니다.</p>

<p>문자열로 이루어진 배열 <code>cards1</code>, <code>cards2</code>와 원하는 단어 배열&nbsp;<code>goal</code>이 매개변수로 주어질 때, <code>cards1</code>과 <code>cards2</code>에 적힌 단어들로 <code>goal</code>를 만들 있다면 "Yes"를, 만들 수 없다면 "No"를 return하는 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>cards1</code>의 길이, <code>cards2</code>의 길이 ≤ 10

<ul>
<li>1 ≤ <code>cards1[i]</code>의 길이, <code>cards2[i]</code>의 길이 ≤ 10</li>
<li><code>cards1</code>과 <code>cards2</code>에는 서로 다른 단어만 존재합니다.</li>
</ul></li>
<li>2 ≤ <code>goal</code>의 길이 ≤ <code>cards1</code>의 길이 + <code>cards2</code>의 길이

<ul>
<li>1 ≤ <code>goal[i]</code>의 길이 ≤ 10</li>
<li><code>goal</code>의 원소는 <code>cards1</code>과 <code>cards2</code>의 원소들로만 이루어져 있습니다.</li>
</ul></li>
<li><code>cards1</code>, <code>cards2</code>, <code>goal</code>의 문자열들은 모두 알파벳 소문자로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>cards1</th>
<th>cards2</th>
<th>goal</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["i", "drink", "water"]</td>
<td>["want", "to"]</td>
<td>["i", "want", "to", "drink", "water"]</td>
<td>"Yes"</td>
</tr>
<tr>
<td>["i", "water", "drink"]</td>
<td>["want", "to"]</td>
<td>["i", "want", "to", "drink", "water"]</td>
<td>"No"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<p>본문과 같습니다.</p>

<p>입출력 예 #2</p>

<p><code>cards1</code>에서 "i"를 사용하고 <code>cards2</code>에서 "want"와 "to"를 사용하여 "i want to"까지는 만들 수 있지만 "water"가 "drink"보다 먼저 사용되어야 하기 때문에 해당 문장을 완성시킬 수 없습니다. 따라서 "No"를 반환합니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
