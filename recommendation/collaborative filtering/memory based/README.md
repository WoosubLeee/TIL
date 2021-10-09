# Memory-based

## User-based

```
for every item i that u has no preference for yet

 for every other user v that has a preference for i

   compute a similarity s between u and v

   add v's preference for i, weighted by s, to a running average

 return the top items, ranked by weighted average
```

This algorithm is very efficient when the number of users is way smaller than the number of items. The major drawback is that adding a new user is expensive since it requires updating all similarities between users.



## Item-based

```
for every item i that u has no preference for yet

  for every item j that u has a preference for

    compute a similarity s between i and j

    add u's preference for j, weighted by s, to a running average

 return the top items, ranked by weighted average
```

In a system where there are more users than items, item-based filtering is faster and more stable than user-based. It is well suited if your items don't change too much, since updating the table for adding a new item is unfortunately hard.

Although, the item-based approach performs poorly for datasets with browsing or entertainment related items such as MovieLens, where the recommendations it gives out seem very obvious to the target users.



## Cosine similarity

다음은 두 영화에 평점을 매긴 4명의 사용자를 그래프로 나타낸 것이다. A와 B는 평점의 정도는 다르지만 Movie 2에 비해 Movie 1에 2배 높은 평점을 주었다는 점에서는 동일하다. Cosine similarity는 위 특징에 착안해 유사도를 측정한다.

Cosine, 즉 원점에서 이은 선의 각도를 구하여 해당 각의 차이로 유사도를 측정한다.

![img](https://files.realpython.com/media/cosine-similarity.76bcd5413eb8.jpg)

```python
>>> from scipy import spatial
>>> a = [1, 2]
>>> b = [2, 4]
>>> c = [2.5, 4]
>>> d = [4.5, 5]

>>> spatial.distance.cosine(c,a)
0.004504527406047898

>>> spatial.distance.cosine(c,b)
0.004504527406047898

>>> spatial.distance.cosine(c,d)
0.015137225946083022

>>> spatial.distance.cosine(a,b)
0.0  # 차이가 가장 적다
```

### Centered cosine

This approach is normally used when there are a lot of missing values in the vectors, and you need to place a common value to fill up the missing values.

A good choice to fill the missing values could be the average rating of each user, but the original averages of user A and B are `1.5` and `3` respectively, and filling up all the empty values of A with `1.5` and those of B with `3` would make them dissimilar users.

But after adjusting the values, the **centered** average of both users is `0`, which allows you to capture the idea of the item being above or below average more accurately for both users with all missing values in both user’s vectors having the same value `0`.

- For user **A**, the rating vector [1, 2] has the average 1.5. Subtracting 1.5 from every rating would give you the vector [-0.5, 0.5].
- For user **B**, the rating vector [2, 4] has the average 3. Subtracting 3 from every rating would give you the vector [-1, 1].
- 

## Calculate predicted ratings

To calculate the predicted rating **R** that an user **U** would give to a certain item **I**, you should get the average of the ratings given to **I** by the users most similar to **U**.

<img src="https://files.realpython.com/media/average_rating.73cdfc1d58c4.png" alt="img" style="zoom: 25%;" />

The average rating given by the *n* similar users is equal to the sum of the ratings given by them divided by the number of similar users, which is *n*.

### Weighted average

The more similar, the more the rating should matter.

The weighted average can help us achieve that. In the weighted average approach, you multiply each rating by a similarity factor(which tells how similar the users are). By multiplying with the similarity factor, you add weights to the ratings.

**S** is similarity factor.

<img src="https://files.realpython.com/media/weighted_rating.06ba3ea506b6.png" alt="img" style="zoom:25%;" />

Every rating is multiplied by the similarity factor of the user who gave the rating. The final predicted rating by user **U** will be equal to the sum of the weighted ratings divided by the sum of the weights.

