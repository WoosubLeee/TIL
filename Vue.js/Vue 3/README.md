# Vue 3

## Composition API

### Why use Composition API?

When our components get bigger, the list of **logical concerns** also grows. This can lead to components that are hard to read and understand, especially for people who didn't write them in the first place.

![Vue Options API: Code grouped by option type](https://v3.vuejs.org/images/options-api.png)

Example presenting a large component where its **logical concerns** are grouped by colors. Such fragmentation is what makes it difficult to understand and maintain a complex component. The separation of options obscures the underlying logical concerns.

Composition API enables us to collocate code related to the same logical concern.

### setup

setup은 component가 생성될 때, props가 resolved될 때 실행된다.

setup은 props와 context에 접근하는 function이어야 하고,
setup에서 return하는 것들은 모두 component의 다른 것들(computed, methods, lifecycle hooks 등)에서 접근이 가능하다.

다음은 setup의 기본 구조이다.

```js
export default {
  components: { RepositoriesFilters, RepositoriesSortBy, RepositoriesList },
  props: {
    user: {
      type: String,
      required: true
    }
  },
  setup(props) {
    console.log(props) // { user: '' }

    return {} // anything returned here will be available for the rest of the component
  }
  // the "rest" of the component
}
```





## 참고자료

https://v3.vuejs.org/guide/composition-api-introduction.html