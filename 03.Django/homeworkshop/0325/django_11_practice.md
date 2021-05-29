# Practice

**1)** `User.objects.all()`

**2)** `User.objects.get(id=19).age`

**3)** `User.objects.values('age')`

**4)** `User.objects.filter(age__lte=40).values('id', 'age')`

**5)** `User.objects.filter(last_name='김', balance__gte=500).values('first_name')`

**6)** `User.objects.filter(first_name__endswith='수', country='경기도').values('balance')`

**7)** `User.objects.filter(balance__gte=2000, age__lte=40).count()`

**8)** `User.objects.filter(phone__startswith='010').count()`

**9)**

```
user = User.objects.get(last_name='김', first_name='옥자')
user.country = '경기도'
user.save()
```

**10)** 

```
user = User.objects.get(first_name='진호', last_name='백')
user.delete()
```

**11)** `User.objects.order_by('-balance').values('first_name', 'last_name', 'balance')[:4]`

**12)** `User.objects.filter(phone__contains='123', age__lt=30)`

**13)** `User.objects.filter(phone__startswith='010').values('country').distinct()`

**14)** `User.objects.aggregate(Avg('age'))`

**15)** `User.objects.filter(last_name='박').aggregate(Avg('balance'))`

**16)** `User.objects.filter(country='경상북도').aggregate(Max('balance'))`

**17)** `User.objects.filter(country='제주특별자치도').order_by('-balance')[0].first_name`

