// Vue app 생성
const app = Vue.createApp({
  data() {
    return {
      title: 'The Final Empire',
      author: 'Woosub Lee',
      released: 1924,
      showBooks: true,
      x: 0,
      y: 0,
      books: [
        {
          title: 'name of the wind',
          author: 'patrick rothfuss',
          img: 'assets/1.jpg',
          isFav: true
        },
        {
          title: 'the way of kings',
          author: 'brandon sanderson',
          img: 'assets/2.jfif',
          isFav: false
        },
        {
          title: 'the final empire',
          author: 'brandon sanderson',
          img: 'assets/3.jfif',
          isFav: true
        }
      ],
      url: 'http://www.naver.com'
    }
  },
  methods: {
    changeTitle(title) {
      this.title = title
    },
    toggleShowBooks() {
      this.showBooks = !this.showBooks
    },
    handleEvent(e, data) {
      console.log(e, e.type)
      if (data) {
        console.log(data)
      }
    },
    handleMousemove(e) {
      this.x = e.offsetX
      this.y = e.offsetY
    },
    toggleFav(book) {
      book.isFav = !book.isFav
    }
  },
  computed: {
    filteredBooks() {
      return this.books.filter((book) => book.isFav)
    }
  }
})

// app이란 id 셀렉터를 가진 태그에 mount 한다
app.mount('#app')