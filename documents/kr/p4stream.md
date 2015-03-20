퍼포스 스트림
==============

빠르고 간편한 브랜치 전환을 지원합니다.


사용 방법
---------

#### 스트림 연결 

* 메인 메뉴 VIew > Workspaces 메뉴 선택
* 워크스페이스들 (Workspaces) 뷰 현재 워크 스페이스 선택
* 스트림 브라우즈(Stream Browse) 버튼: main 스트림 선택

#### 환경 설정

* 메인 메뉴 Edit > Preferences 메뉴 선택
* 스트림들 (Streams) 패널 선택
* 스트림 워크스페이스들 (Stream Workspaces) 섹션 
	* 이 스트림에서 작업 선택시 (When clicking 'Work in this Stream'): reuse current workspace
	* 워크스페이스 아이콘 드래그시 (When dragging workspace icon to a new steam): reuse current workspace

#### 스트림 변경 

* 스트림 리스트 (Streams) 뷰 그래프 패널: 스트림 더블 클릭 후 이 스트림에서 작업(Work is this Stream) 클릭 or 모니터 아이콘 드래그


관리 방법 
----------


#### P4V: 워크 스페이스 맵핑 확인

스트림은 맵핑 변경 불가능

 * //depot/PATH1/TO1
 * //depot/PATH2/TO2



#### P4Admin: 스트림 디팟 준비

팀 단위로 스트림 디팟 

* 디팟 이름(depot name): TEAM
* 디팟 타입(depot type): stream



#### P4V: 메인 라인 생성

* Streams 탭 > Graph View Options 패널 > No items Available 우 클릭
* 컨텍스트 메뉴 New Stream 선택
	* 스트림 이름(Sream name): main
	* 스트림 타입(Steam type): mainline
	* 스트림 디팟(The depot where the mainline stream will be located): TEAM
	* 스트림 워크스페이스 생성(Create a workspace to use with this tream): 체크 안함
	* 스트림 생성 후 메인 스트림 준비(Populate the main stream after it is created): 체크 안함
* 워크 스페이스들 (Workspaces) 뷰: 현재 워크스페이스 선택 후 편집 
	* 스트림(Stream) 선택: //TEAM//main
	* OK 버튼 클릭
* 디팟(Depot) 뷰 선택
	*  기존 맵핑 폴더 선택: //depot/PATH1/TO1
		* 카피(Copy...) 메뉴 클릭
			* 타겟 파일 및 폴더 선택(Choose target files/folders): //TEAM/main/TO1
			* 프리뷰(Preview) 버튼 클릭
			* 카피(Copy) 버튼 클릭
		* 서밋(Submmit) 버튼 클릭


#### P4V: 개발 라인 생성 

* Streams 탭 > Graph View Options 패널 > main 스트림 선택 후 우클릭
* 메인 기반 새로운 스트림 생성(Create New Stream from 'main')
	* 스트림 이름(Stream name): dev
	* 스트림 타입(Steam type): development
	* 부모 스트림(The parent stream from which this stream will be branched)
	* 확인(OK) 버튼 클릭
* 스트림 그래프 패널
	* dev 스트림 선택 후 더블 클릭
		* dev 스트림 전환 (Work in this Stream)
	* dev 스트림 선택 후 우클릭
		* dev 스트림 머지 (Merge/Integrate to dev) 메뉴 선택
		* 서밋(Submit) 버튼 클릭
		* 리졸브(Resolve) 실행