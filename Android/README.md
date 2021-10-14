# Android

## Project architecture

기본적으로 안드로이드 스튜디오 화면에 보이는 디렉터리의 구조를 실제 파일 탐색기나 파인더로 열어보면 그 구조가 완전히 다릅니다. 

### Android 뷰의 구조

Android 뷰는 안드로이드 개발을 편하게 하기 위해 재배치한 가상의 디렉터리 구조를 보여줍니다. 크게 app과 Gradle Scripts로 구성되는데 app에는 코딩하면서 생성한 모든 파일이 저장되고, Gradle Scripts에는 빌드에 필요한 설정 정보들이 저장됩니다.

![image-20211013155256866](README.assets/image-20211013155256866.png)

### Project 뷰의 구조

Project 뷰는 실제 디렉터리의 구조를 그대로 보여줍니다. 이미지를 추가하거나 다양한 화면 크기를 처리하는 작업 등의 리소스를 변경할 때 Project 뷰로 전환해서 작업하는 것이 좋습니다.

![image-20211013155346587](README.assets/image-20211013155346587.png)

