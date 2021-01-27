# 마크다운(Markdown)

> 일반 텍스트 형식 구문을 사용하는 마크업 언어의 일종으로 사용법이 쉽고 간결하여 빠르게 문서 정리를 할 수 있습니다. 단, 모든 HTML 마크업을 대체하지는 않습니다.



## 1. 문법

### 1.1 Header

> 헤더는 제목을 표현할 때 사용합니다. 단순히 글자의 크기를 표현하는 것이 아닌 의미론적인 중요도를 나타냅니다.

- `<h1>` 부터 `<h6>`  까지 표현이 가능합니다
- `# ` 의 개수로 표현하거나 `<h1></h1> ` 의 형태로 표현 가능합니다.



# h1 태그입니다.

## h2 태그입니다.

### h3 태그입니다.

#### h4 태그입니다.

##### h5 태그입니다.

###### h6 태그입니다.



### 1.2 List

> 목록을 나열할 때 사용합니다. 순서가 필요한 항목과 그렇지 않은 항목으로 구분할 수 있습니다. 순서가 있는 항목 아래 순서가 없는 항목을 지정할 수 있으며 그 반대도 가능합니다.

- 순서가 있는 목록
  - `1.` 을 누르고 스페이스바를 누르면 생성할 수 있습니다.
  - `tab ` 키를 눌러서 하위 항목을 생성할 수 있고 `shift + tab ` 키를 눌러서 상위항목으로 이동할 수 있습니다.
- 순서가 없는 목록
  - `-`  (하이픈)을 쓰고 스페이스바를 누르면 생성할 수 있습니다.
  - `tab ` 키를 눌러서 하위 항목을 생성할 수 있고 `shift + tab ` 키를 눌러서 상위항목으로 이동할 수 있습니다.



1. 순서가 있는 목록
2. 순서가 있는 목록
   1. 순서가 있는 하위 항목
   2. 순서가 있는 하위 항목



- 순서가 없는 항목
- 순서가 없는 항목
  - 순서가 없는 하위 항목
  - 순서가 없는 하위 항목



### 1.3 Code Block

> 코드 블럭은 작성한 코드를 정리하거나 강조하고 싶은 부분을 나타낼 때 사용합니다. 인라인과 블럭 단위로 구분할 수 있습니다.

- Inline
  - 인라인 블럭으로 처리하고 싶은 부분을 `(백틱)으로 감싸줍니다.
- Block
  - `(백틱)을 3번 입력하고 Enter 를 눌러 생성합니다.

`add ` 한 요소를 remote 저장소에 올리려면 `$ git push origin master` 를 터미널에 입력합니다.

```bash
$ git add .
$ git commit -m "first commit"
$ git push origin master
```



### 1.4 Image

> 로컬에 있는 이미지를 삽입하거나 이미지 링크를 활용하여 이미지를 나타낼 때 사용합니다.

- `![]()` 을 작성하고 `()` 안에 이미지 주소를 입력합니다. `[]` 안에는 이미지 파일의 이름을 작성합니다.
- 로컬에 이미 파일을 저장한 경우 절대 경로가 아닌 상대 경로를 사용하여 이미지를 저장합니다.



<img src="markdown.assets/서울_3반_이우섭(0547386).jpg" style="zoom:10%;" />

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--i_sb3chq--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://thepracticaldev.s3.amazonaws.com/i/fk0849hvg2rt13bpqhjy.jpg" style="zoom:25%;" />



### 1.5 Link

> 특정 주소로 링크를 걸 때 사용합니다.

- `[]()` 을 작성하고 `()` 안에 주소를 작성하고 `[]` 안에 어떤 링크 주소인지 작성합니다.



[Github 구글 이미지 검색](https://www.google.com/search?q=github&newwindow=1&sxsrf=ALeKk03omdvCSi07gXAhQusd-eD8UnV6_w:1610526470058&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjerZjRvpjuAhWXFogKHa7YCkkQ_AUoAXoECBgQAw&biw=1536&bih=722#imgrc=bgKiPn6UOsCJaM)



### 1.6 Table

> 표를 작성하여 요소를 구분할 수 있습니다.

- `|` (파이프) 사이에 컬럼을 작성하고 `enter` 를 입력합니다.
- 마지막 컬럼을 작성하고 뒤에 `|` 를 붙여줍니다.



| working directory | staging area | remote repo |
| ----------------- | ------------ | ----------- |
| working tree      | index        | history     |
| working copy      | cache        | tree        |



### 1.7 기타

인용문(참조문)

- `>` 을 입력하고 `enter` 키를 누릅니다.

> git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다.

- 인용문 안에 인용문을 작성하면 중첩해서 사용할 수 있습니다.

> $ git add .
>
> > $ git commit -m "first commit"
> >
> > > $ git push origin master



수평선

- `---`, `***`, `___` 을 입력하여 작성합니다.

Working Directory

---

Staging Area

***

Remote Repository

___



강조

- 이탤릭체는 해당 부분을 `*` 혹은 `_`(언더바)로 감싸줍니다.
- 볼드체는 해당 부분을 `**` 혹은 `__`(언더바2개)로 감싸줍니다.
- 취소선은 `~~` 표시를 사용합니다.

이것은 *이탤릭체*  입니다.

이것은 **볼드체** 입니다.

이것은 ~~취소선~~ 입니다.
