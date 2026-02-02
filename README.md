# 🚀 PY_A_STAR_SCRATCH
> **Objective:** 파이썬으로 라이브러리 없이 A* 알고리즘 밑바닥부터 구현하기 (Data Structure & Algorithm Mastery)

## 1. 프로젝트 개요 (Overview)
이 프로젝트는 **로보틱스 및 자율주행의 핵심인 경로 탐색(Path Planning)** 원리를 깊이 이해하기 위해 기획되었습니다. 
편리한 라이브러리 사용을 배제하고, 핵심 자료구조(Heap, Queue)와 알고리즘 로직을 직접 구현함으로써 엔지니어링 기초 체력을 기릅니다.

* **Map Size:** 10x10 Grid
* **Input:** 시작점(Start), 도착점(Goal), 장애물(Wall)
* **Output:** CLI(터미널) 기반의 최단 경로 시각화

---

## 2. 핵심 제약사항 (Constraints)
**이 프로젝트의 핵심 규칙입니다. 타협하지 마십시오.**

1.  🔴 **NO Libraries (라이브러리 금지)**
    * `import heapq`, `import queue`, `from collections import deque` 등 자료구조 모듈 사용 절대 금지.
    * 오직 Python Native List (`[]`)와 기본 문법만 사용.
    * *이유: 자료구조의 내부 동작 원리(Index 조작 등)를 파악하기 위함.*

2.  🖥️ **CLI Only (텍스트 기반 시각화)**
    * `matplotlib`, `pygame` 등 그래픽 라이브러리 사용 금지.
    * 오직 `print()` 함수와 특수문자만 사용하여 맵과 경로를 표현.

---

## 3. 기능 요구사항 (Functional Requirements)

### 3.1 맵 관리 (Map Manager)
* **Grid 생성:** 가로 10, 세로 10 크기의 2차원 리스트(`list of lists`)를 생성한다.
* **속성 정의:**
    * `0`: 빈 공간 (Road)
    * `1`: 벽/장애물 (Wall)
* **좌표 입력:** 시작점 `(sx, sy)`과 도착점 `(gx, gy)`을 입력받아 맵에 배치한다.

### 3.2 자료구조 구현 (Data Structure) - ★ Key Point
> 이 프로젝트에서 가장 중요한 학습 파트입니다.

#### A. Node 클래스
각 격자(Grid Cell)를 하나의 객체로 관리합니다.
* **Attributes:**
    * `x`, `y`: 좌표
    * `parent`: 현재 노드에 도달하기 직전의 부모 노드 (경로 역추적용)
    * `G`: 시작점부터 현재 노드까지의 실제 이동 비용
    * `H`: 현재 노드에서 목표점까지의 예상 비용 (Heuristic, 맨해튼 거리 권장)
    * `F`: `G + H` (최종 평가 점수)
* **Methods:**
    * `__lt__`: 힙 정렬을 위한 비교 연산자 오버로딩 (F값 기준 비교)

#### B. Min-Heap (우선순위 큐)
탐색할 노드 중 **F값이 가장 작은 노드**를 $O(\log N)$ 시간 안에 꺼내야 합니다.
* **Base:** 파이썬 리스트(`[]`)를 사용.
* **Methods:**
    * `push(node)`: 노드 삽입 후, 부모 노드와 비교하며 위로 올라가는 **Up-Heap** 연산 구현.
    * `pop()`: 루트 노드(최소 F)를 반환 및 삭제 후, 마지막 노드를 루트로 올리고 아래로 내려가는 **Down-Heap** 연산 구현.

### 3.3 알고리즘 로직 (A* Algorithm)
1.  **초기화:** 시작 노드를 생성하여 `Open List`(Min-Heap)에 넣는다.
2.  **메인 루프:** `Open List`가 빌 때까지 반복한다.
    * **Pop:** F값이 가장 작은 노드(`Current`)를 꺼낸다.
    * **Goal Check:** `Current`가 도착점이면 루프 종료 및 경로 생성.
    * **Closed List:** `Current`를 방문 목록(`Closed List`)에 추가.
    * **Neighbor Search:** 상하좌우 4방향 탐색.
        * **무시 조건:** 맵 밖이거나, 벽(`1`)이거나, 이미 방문(`Closed List`)한 경우.
        * **갱신 조건:** `Open List`에 없거나, 기존 경로보다 G값이 더 작을 경우 → `Parent`, `G`, `F` 갱신 후 `push`.
3.  **경로 역추적 (Backtracking):** 도착점에서부터 `parent`를 타고 시작점까지 거슬러 올라가며 좌표를 저장한다.

### 3.4 시각화 (Visualization)
* 2차원 배열을 순회하며 출력한다.
* **Symbols:**
    * `S`: 시작점
    * `G`: 도착점
    * `W`: 벽 (Wall)
    * `.`: 빈 공간
    * `*`: **최단 경로 (Path)**

---

## 4. 시스템 설계 (Architecture)

### Class Diagram
```mermaid
classDiagram
    class Node {
        +int x
        +int y
        +int g
        +int h
        +int f
        +Node parent
        +__lt__(other)
    }

    class MinHeap {
        -list items
        +push(node)
        +pop() Node
    }

    class AStarSolver {
        +list grid_map
        +MinHeap open_list
        +set closed_list
        +get_path(start, goal)
        -heuristic(node, goal)
    }

    Node --* MinHeap : Contains
    MinHeap --* AStarSolver : Uses