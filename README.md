# 구현 목표
본 프로젝트는 1992년부터 2012년까지 30년이라는 긴 세월동안 Microsoft Windows 시리즈에 포함되어온 유서깊은 기본 게임 중 하나인 지뢰찾기(MineSweeper)를 구현하는 것을 목적으로 합니다. 플레이어는 빈칸을 클릭하여 지뢰의 위치에 대한 단서를 얻고, 최종적으로 지뢰칸을 제외한 모든 칸을 파내면 승리, 지뢰칸을 건드리면 패배합니다.

# 구현 기능
* pygame 기반 게임 환경 구현
* 마우스 클릭으로 칸을 파냄
* 해당 칸의 주변 8방향에 존재하는 지뢰의 숫자를 표시
* 주변에 지뢰가 전혀 없을 경우 그와 연결된 지뢰가 0개인 칸이 모두 파짐

# Reference
[1] https://github.com/pygame/pygame "pygame"

# 지원 Operating Systems 및 실행 방법

## 지원 Operating Systems
|OS| 지원 여부 |
|-----|--------|
|windows | :x:(확인 필요)  |
| Linux  | :o: |
|MacOS  | :x:(확인 필요)  |
본 프로젝트는 Ubuntu 22.04 LTS 환경에서 개발 및 테스트 되었으며 다른 환경에서의 동작은 테스트되지 않았습니다. 그러나 pygame을 통해 개발되었기 때문에 pygame을 지원하는 환경에서는 모두 동작이 가능할 것으로 예상됩니다.

## 실행 방법

### Windows
https://github.com/pygame/pygame 참조하여 설치 후 확인 필요

### Linux
1. python3 설치
'''
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3
'''
2. pygame 설치
'''
pip3 install pygame
'''
3. 프로젝트 폴더 내부에서 main.py 실행
'''
python3 main.py
'''

### MacOS
https://github.com/pygame/pygame 참조하여 설치 후 확인 필요

# 실행 예시
![example](https://github.com/RmKuma/oss_personal_project_phase1/assets/20412048/98ecfe0c-34c5-4592-86e9-defded705a36)

# 코드 설명

## 전역변수
* field[][]: 좌표에 해당하는 정보(지뢰 or 숫자)를 저장하는 2차원 list
* field_cover[][]: 아직 파지 않은 좌표를 저장하는 2차원 list
## main.py

### 메인 루프
* 이벤트 처리
uncover(x, y): 마우스가 유효한 좌표를 클릭했을 때 그 좌표에 해당하는 칸을 파냄.
* 화면 렌더링
if(field_cover[x][y]): 아직 파지 않은 칸은 흰색으로 덮음
else: 파낸 칸은 회색으로 덮음, 숫자가 존재하면 숫자를 표시

# TODO List
* 지뢰로 예상되는 칸에 다른 동작(예: 우클릭)을 통해 깃발(flag)를 꽂아 실수로 클릭하는 것을 방지하기
* 주변에 깃발이 해당 칸의 숫자만큼 꽂혀있는 칸에 다른 동작(예: 마우스 휠 클릭)을 통해 깃발이 꽂힌 칸을 제외한 나머지 8칸을 모두 파내는 기능
* 게임이 끝나면 다시 시작할 수 있도록 하기
* 첫칸에 지뢰가 묻혀있는 현상 제거하기
* 타이머를 추가하여 경쟁요소 도입하기
