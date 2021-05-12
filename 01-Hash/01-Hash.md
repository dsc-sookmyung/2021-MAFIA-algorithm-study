# 01-Hash

> 담당 : 권은지

### 해시
 - Key - value쌍으로 데이터를 저장하는 자료 구조
 - 데이터를 아주 빠르게 삽입하거나 가져올 때 사용하는 기법
 - 예) python 딕셔너리

## 문제 1. 완주하지 못한 선수 (level1)
### 문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

### 제한사항
 - 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
 - completion의 길이는 participant의 길이보다 1 작습니다.
 - 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
 - 참가자 중에는 동명이인이 있을 수 있습니다.

### 입출력 예
<table>
<tr>
<td>participant</td>
<td>completion</td>
<td>return</td>
</tr>
<tr>
<td>["leo", "kiki", "eden"]</td>
<td>["eden", "kiki"]</td>
<td>"leo"</td>
</tr>
<tr>
<td>["marina", "josipa", "nikola", "vinko", "filipa"]</td>
<td>["josipa", "filipa", "marina", "nikola"]</td>
<td>"vinko"</td>
</tr>
<tr>
<td>["mislav", "stanko", "mislav", "ana"]</td>
<td>["stanko", "ana", "mislav"]</td>
<td>"mislav"</td>
</tr>
</table>

### 입출력 예 설명
예제 #1
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

## 문제 2. 전화번호 목록 (level2)
###문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

 - 구조대 : 119
 - 박준영 : 97 674 223
 - 지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

### 제한 사항
 - phone_book의 길이는 1 이상 1,000,000 이하입니다.
 - 각 전화번호의 길이는 1 이상 20 이하입니다.
 - 같은 전화번호가 중복해서 들어있지 않습니다.

### 입출력 예제
<table>
<tr>
<td>phone_book</td>
<td>return</td>
</tr>
<tr>
<td>["119", "97674223", "1195524421"]</td>
<td>false</td>
</tr>
<tr>
<td>["123","456","789"]</td>
<td>true</td>
</tr>
<tr>
<td>["12","123","1235","567","88"]</td>
<td>false</td>
</tr>
</table>

### 입출력 예 설명
입출력 예 #1
앞에서 설명한 예와 같습니다.

입출력 예 #2
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

입출력 예 #3
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

## 문제 3. 위장 (level2)
###문제 설명
스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.
<table>
<tr>
<td>종류</td>
<td>이름</td>
</tr>
<tr>
<td>얼굴</td>
<td>동그란 안경, 검정 선글라스</td>
</tr>
<tr>
<td>상의</td>
<td>파란색 티셔츠</td>
</tr>
<tr>
<td>하의</td>
<td>청바지</td>
</tr>
<tr>
<td>겉옷</td>
<td>긴 코트</td>
</tr>
</table>
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

###제한사항
 - clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
 - 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
 - 같은 이름을 가진 의상은 존재하지 않습니다.
 - clothes의 모든 원소는 문자열로 이루어져 있습니다.
 - 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
 - 스파이는 하루에 최소 한 개의 의상은 입습니다.

### 입출력 예제
<table>
<tr>
<td>clothes</td>
<td>return</td>
</tr>
<tr>
<td>[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]</td>
<td>5</td>
</tr>
<tr>
<td>[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]</td>
<td>3</td>
</tr>
</table>

### 입출력 예 설명
예제 #1
headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.

1. yellow_hat
2. blue_sunglasses
3. green_turban
4. yellow_hat + blue_sunglasses
5. green_turban + blue_sunglasses

예제 #2
face에 해당하는 의상이 crow_mask, blue_sunglasses, smoky_makeup이므로 아래와 같이 3개의 조합이 가능합니다.

1. crow_mask
2. blue_sunglasses
3. smoky_makeup

## 문제 4. 베스트앨범 (level3)
###문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

### 제한 사항
 - genres[i]는 고유번호가 i인 노래의 장르입니다.
 - plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
 - genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
 - 장르 종류는 100개 미만입니다.
 - 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
 - 모든 장르는 재생된 횟수가 다릅니다.

### 입출력 예제
<table>
<tr>
<td>genres</td>
<td>plays</td>
<td>return</td>
</tr>
<tr>
<td>["classic", "pop", "classic", "classic", "pop"]</td>
<td>[500, 600, 150, 800, 2500]</td>
<td>[4, 1, 3, 0]</td>
</tr>
</table>

### 입출력 예 설명
classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.
 - 고유 번호 3: 800회 재생
 - 고유 번호 0: 500회 재생
 - 고유 번호 2: 150회 재생
pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.
 - 고유 번호 4: 2,500회 재생
 - 고유 번호 1: 600회 재생
따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.
