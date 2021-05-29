# Workshop

#### 1)

(a) : `forms.ModelForm`

(b) : `Meta`

#### 2)

`create.html`의 `form`에서 작성된 내용이 다시 `request.POST`로 넘어왔을 때,
만약 내용이 valid하지 않다면 `if form.is_valid():`에서 `False` 가 나와 아무것도 실행되지 않는 경우가 발생한다.

이를 방지하기 위해

```
else:
	form = ReservationForm()
context = {
	'form': form,
}
return = render(request, 'reservations/create.html', context)
```

`else` 이하 구문을 위와 같이 작성하여 valid하지 않을 경우에 전송될 경로를 설정하면 된다.

#### 3)

(a) : `form = ArticleForm(request.POST, instance=reservation)`

(b) : `form = ArticleForm(instance=article)`

#### 4)

```
as_p, as_ul, as_table
```



# Homework

#### 1.

`context`가 `else` 구문 아래 들어가있다면
`if form.is_valid()`에서 `form`으로 전달된 내용이 유효하지 않을 경우 아무것도 `return`되지 않는다.

이를 방지하기 위해 `if else` 구문과 동일한 레벨에 두어 유효하지 않을 경우에도 `return`될 수 있도록 하는 것이다.

#### 2.

`POST`는 서버 DB를 수정하는 method이므로 우선적으로 처리한다.

`POST`가 아니고 `PUT`, `DELETE`여도 DB에 수정을 가하므로 `if request.method == 'OOO'` 방식으로 좀 더 명시적으로 처리해준다.