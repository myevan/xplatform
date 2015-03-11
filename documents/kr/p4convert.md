P4Convert
=========

다른 버전 관리 시스템(SVN, CVS)에서 퍼포스로 저장소 이전



준비 작업
---------

#### 다운로드

* 매뉴얼 <ftp://ftp.perforce.com/perforce/tools/p4convert/p4convert.pdf>
* 패키지 <ftp://ftp.perforce.com/perforce/tools/p4convert/p4convert.tgz>


### 모드 결정

* 임포트 모드: 리비전 단위 이전
* 컨버트 모드: 저장소 전체 이전
* 점진적 갱신 모드: 임포트 모드 기반. 새로운 리비전 이전


#### 요구 사항

* 저장소 데이터
	* SVN: 덤프 파일 (--delta 플래그 없이 생성해야 함)
* 자바: Java SE Runtime 1.7 
* 퍼포스: p4d 2010.2 이상 
	* 임포트 모드: 작동중인 퍼포스 서버 (가능하면 비어있는 저장소. 작업 중인 사항이 없어야 함)



SVN 윈도우
----------

#### 요구 사항

* TortoiseSVN
* 관리자 권한 커맨드 라인 콘솔 


#### 로컬 백업 

SVN 관리자 권한이 없을 경우 덤프 생성을 위해 백업 필요

	D:\> mkdir SVNBackups
	
	D:\> cd SVNBackups
	
	D:\SVNBackups> svnadmin create LOCAL_REPO_NAME
	
	D:\SVNBackups> notepad.exe LOCAL_REPO_NAME\hooks\pre-revprop-change.bat
	@ECHO OFF
	exit 0

	D:\SVNBackups> svnsync init file:///d:/SVNBackups/LOCAL_REPO_NAME svn://REMOTE_REPO_HOST/PATH	

	D:\SVNBackups> svnsync sync file:///d:/SVNBackups/LOCAL_REPO_NAME


#### 덤프 생성 

	D:\SVNBackups> svnsync sync file:///d:/SVNBackups/LOCAL_REPO_NAME

	D:\SVNBackups> svnadmin dump LOCAL_REPO_NAME > LOCAL_REPO_NAME.dmp


#### 변환 설정

	D:\SVNBackups> java -jar p4convert.jar --type=SVN --default

	D:\SVNBackups> ren default.cfg LOCAL_REPO_NAME.cfg

	D:\SVNBackups> notepad.exe LOCAL_REPO_NAME.cfg
	com.p4convert.svn.dumpFile=D:\\SVNBackups\\LOCAL_REPO_NAME.dmp	

	com.p4convert.p4.caseMode=First
	com.p4convert.p4.charset=utf8
	com.p4convert.p4.client=USER_HOST
	com.p4convert.p4.clientRoot=D:\\PerforceWorkspaces\\USER_HOST
	com.p4convert.p4.depotPath=depot

	com.p4convert.p4.port=PERFORCE_HOST:PORT
	com.p4convert.p4.root=

	com.p4convert.p4.subPath=REMOTE_REPO_PATH
	com.p4convert.p4.unicode=true
	com.p4convert.p4.user=USER


#### 변환 시작

	D:\SVNBackups> java -jar p4convert.jar --config=LOCAL_REPO_NAME.cfg