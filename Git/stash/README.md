# Git stash

branch에서 코드를 작성 중 갑자기 다른 branch로 넘어가야 할 일이 생겼다고 생각해보자. commit을 해도 되겠지만 완성되지 않은 난잡한 코드를 commit하는 것은 별로 바람직한 일은 아닐 것이다. 이럴 때 사용할 수 있는 것이 `git stash`이다.

- `git stash` = `git stash push` : Saves local modifications away and reverts the working directory to match the `HEAD` commit
- `git stash list` : Stash list 확인
- `git stash show` : Inspect list
- `git stash pop` : Remove a single stashed state from the stash list and apply it on top of the current working tree state.

