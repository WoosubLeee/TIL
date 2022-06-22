# Next.js

##   Pages

In Next.js, a **page** is a [React Component](https://reactjs.org/docs/components-and-props.html) exported from a `.js`, `.jsx`, `.ts`, or `.tsx` file in the `pages` directory. Each page is associated with a route based on its file name.

**Example**: If you create `pages/about.js` that exports a React component like below, it will be accessible at `/about`.

```js
function About() {
  return <div>About</div>
}

export default About
```



## Pre-rendering

By default, Next.js **pre-renders** every page, generates HTML for each page in advance, instead of having it all done by client-side JavaScript. Pre-rendering can result in better performance and SEO.

Each generated HTML is associated with minimal JavaScript code necessary for that page. When a page is loaded by the browser, its JavaScript code runs and makes the page fully interactive. (This process is called *hydration*.)

**Two forms of pre-rendering**

- **static generation** : The HTML is generated at build time and the same HTML file will be reused on each request.
- **server-side rendering** : The HTML is generated on each request.

Static generation is recommended for performance reasons.

You can also use **client-side rendering** if you want.

### Static generation

The page HTML is generated at **build time**.

```js
function About() {
  return <div>About</div>
}

export default About
```

 cases like this, Next.js generates a single HTML file per page during build time.

#### Static generation with data

##### `getStaticProps`

It's needed when your page content depends on external data.

```js
// TODO: Need to fetch `posts` (by calling some API endpoint)
//       before this page can be pre-rendered.
function Blog({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li>{post.title}</li>
      ))}
    </ul>
  )
}

export default Blog
```

To fetch this data on pre-render, Next.js allows you to `export` an `async` function called `getStaticProps` from the same file. This function gets called at build time and lets you pass fetched data to the page's `props` on pre-render.

```js
function Blog({ posts }) {
  // Render posts...
}

// This function gets called at build time
export async function getStaticProps() {
  // Call an external API endpoint to get posts
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      posts,
    },
  }
}

export default Blog
```

When you navigate to a page that’s pre-rendered using `getStaticProps`, Next.js fetches this JSON file (pre-computed at build time) and uses it as the props for the page component. This means that client-side page transitions will **not** call `getStaticProps` as only the exported JSON is used.

`getStaticProps` can only be exported from a **page**. You **cannot** export it from non-page files.

###### Incremental static regeneration

Incremental Static Regeneration (ISR) enables you to use static-generation on a per-page basis, **without needing to rebuild the entire site**.

To use ISR, add the `revalidate` prop to `getStaticProps`:

```js
function Blog({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}

// This function gets called at build time on server-side.
// It may be called again, on a serverless function, if
// revalidation is enabled and a new request comes in
export async function getStaticProps() {
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  return {
    props: {
      posts,
    },
    // Next.js will attempt to re-generate the page:
    // - When a request comes in
    // - At most once every 10 seconds
    revalidate: 10, // In seconds
  }
}

// This function gets called at build time on server-side.
// It may be called again, on a serverless function, if
// the path has not been generated.
export async function getStaticPaths() {
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  // Get the paths we want to pre-render based on posts
  const paths = posts.map((post) => ({
    params: { id: post.id },
  }))

  // We'll pre-render only these paths at build time.
  // { fallback: blocking } will server-render pages
  // on-demand if the path doesn't exist.
  return { paths, fallback: 'blocking' }
}

export default Blog
```

위에서 `getStaticProps()`를 살펴보면 현재 `revalidate` 값이 10(초)으로 설정돼있다. 시간마다의 작동 방식을 살펴보면:

- At build time : 일단 페이지를 기존 방식대로 생성하고 cache한다.
- Request before 10 seconds after build time : 처음에 cache된 페이지를 응답한다.
- Request after 10 seconds after build time : 처음에 cache된 페이지를 응답하나, triggers a regeneration of the page in background.
- Request after regeneration : 새로 생성되어 cache된 페이지를 보여준다. If the background regeneration fails, the old page would still be unaltered.
- 10초, 20초, 30초, ... 계속 10초 간격이 지난 후의 요청은 regeneration을 trigger하게 된다.

##### `getStaticPaths`

It allows you to create pages with dynamic routes. 예를 들어, 만약 게시글 번호 1~3 번까지 작성되어 있다면 각 id 당 1개의 HTML 파일이 생성되어야 할 것이다. 이 경우 `pages/posts/[id].js` 와 같이 `[]` 안에 dynamic route value를 작성하고, `getStaticPaths`에서

```js
[
  {
    params: {
      id: 1
    }
  },
  {
    params: {
      id: 2
    }
  },
  {
    params: {
      id: 3
    }
  }
]
```

형식의 Array를 넘겨준다.

```js
// This function gets called at build time
export async function getStaticPaths() {
  // Call an external API endpoint to get posts
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  // Get the paths we want to pre-render based on posts
  const paths = posts.map((post) => ({
    params: { id: post.id },
  }))

  // We'll pre-render only these paths at build time.
  // { fallback: false } means other routes should 404.
  return { paths, fallback: false }
}
```

Also, you need to export ``getStaticProps` so that you can fetch the data about the post with this `id` and use it to pre-render the page:

```js
function Post({ post }) {
  // Render post...
}

export async function getStaticPaths() {
  // ...
}

// This also gets called at build time
export async function getStaticProps({ params }) {
  // params contains the post `id`.
  // If the route is like /posts/1, then params.id is 1
  const res = await fetch(`https://.../posts/${params.id}`)
  const post = await res.json()

  // Pass post data to the page via props
  return { props: { post } }
}

export default Post
```

### Server-side rendering

> SSR

The page HTML is generated on **each request**. If you export an `async` function called `getServerSideProps`, Next.js will pre-render this page on each request using this function.

```js
function Page({ data }) {
  // Render data...
}

// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`https://.../data`)
  const data = await res.json()

  // Pass data to the page via props
  return { props: { data } }
}

export default Page
```

You should use `getServerSideProps` only if you need to render a page whose data must be fetched at request time. It will only be cached if cache-control headers are configured.

- `getServerSideProps` : run on every request

  vs

- `getStaticProps` : run only once on build time

#### Try not to use API route in `getServerSideProps`

You should not use fetch() to call an API route in getServerSideProps. Instead, directly import the logic used inside your API route. You may need to slightly refactor your code for this approach.

```js
// pages/api/user
export default async function handler(req, res) {
  // Using a fetch here but could be any async operation to an external source
  const response = await fetch(/* external API endpoint */)
  const jsonData = await response.json()
  res.status(200).json(jsonData)
}
```

기존에 위와 같이 구성된 API route을

```js
// pages/api/user
export async function getData() {
    const response = await fetch(/* external API endpoint */)
    const jsonData = await response.json()
    return jsonData
}

export default async function handler(req, res) {
    const jsonData = await getData()
    res.status(200).json(jsonData)
}
```

같이 분리하여 구성하고, `getData()` 함수를 `getServerSideProps`에서 호출하는 방식으로 구성하는 것은 가능하다.



## Client-side data fetching

Client-side data fetching is useful when the content of your pages need to update frequently. Unlike the server-side rendering APIs, you can use client-side data fetching at the component level. If done at the page level, the data is fetched at runtime, and the content of the page is updated as the data changes. When used at the component level, the data is fetched at the time of the component mount, and the content of the component is updated as the data changes.

How to do is similar to using React.js.

```js
function Profile() {
  const [data, setData] = useState(null)
  const [isLoading, setLoading] = useState(false)

  useEffect(() => {
    setLoading(true)
    fetch('/api/profile-data')
      .then((res) => res.json())
      .then((data) => {
        setData(data)
        setLoading(false)
      })
  }, [])

  if (isLoading) return <p>Loading...</p>
  if (!data) return <p>No profile data</p>

  return (
    <div>
      <h1>{data.name}</h1>
      <p>{data.bio}</p>
    </div>
  )
}
```

### SWR

The SWR library is highly recommended if you are fetching data on the client-side. It handles caching, revalidation, focus tracking, refetching on intervals, and more.

```js
import useSWR from 'swr'

const fetcher = (...args) => fetch(...args).then((res) => res.json())

function Profile() {
  const { data, error } = useSWR('/api/profile-data', fetcher)

  if (error) return <div>Failed to load</div>
  if (!data) return <div>Loading...</div>

  return (
    <div>
      <h1>{data.name}</h1>
      <p>{data.bio}</p>
    </div>
  )
}
```



## CSS support

### Global styles

To add a stylesheet to your application, import the CSS file within `pages/_app.js`.

```js
// pages/_app.js

import '../styles.css'

// This default export is required in a new `pages/_app.js` file.
export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

These styles (`styles.css`) will apply to all pages and components in your application. Due to the global nature of stylesheets, and to avoid conflicts, you may **only import them inside `pages/_app.js`**.



## Layout

The React model allows us to deconstruct a page into a series of component to reuse between pages.

```js
// components/layout.js

import Navbar from './navbar'
import Footer from './footer'

export default function Layout({ children }) {
  return (
    <>
      <Navbar />
      <main>{children}</main>
      <Footer />
    </>
  )
}
```

```js
// pages/_app.js

import Layout from '../components/layout'

export default function MyApp({ Component, pageProps }) {
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  )
}
```

If you need multiple layouts, you can add a property `getLayout` to your page. This allows you to define the layout on a per-page basis.

```js
// pages/index.js

import Layout from '../components/layout'
import NestedLayout from '../components/nested-layout'

export default function Page() {
  return {
    /** Your content */
  }
}

// Using multiple layouts
Page.getLayout = function getLayout(page) {
  return (
    <Layout>
      <NestedLayout>{page}</NestedLayout>
    </Layout>
  )
}
```

```js
// pages/_app.js

export default function MyApp({ Component, pageProps }) {
  // Use the layout defined at the page level, if available
  const getLayout = Component.getLayout || ((page) => page)

  return getLayout(<Component {...pageProps} />)
}
```

Using `getLayout()`, you can enable state persistence between page transitions because the React component tree is maintained (`getLayout`을 사용하지 않고, component 함수 렌더링 태그에 layout을 작성하면 state가 보존되지 않는다).

### With TypeScript

```typescript
// pages/index.tsx

import type { ReactElement } from 'react'
import Layout from '../components/layout'
import NestedLayout from '../components/nested-layout'
import type { NextPageWithLayout } from './_app'

const Page: NextPageWithLayout = () => {
  return <p>hello world</p>
}

Page.getLayout = function getLayout(page: ReactElement) {
  return (
    <Layout>
      <NestedLayout>{page}</NestedLayout>
    </Layout>
  )
}

export default Page
```

```typescript
// pages/_app.tsx

import type { ReactElement, ReactNode } from 'react'
import type { NextPage } from 'next'
import type { AppProps } from 'next/app'

export type NextPageWithLayout = NextPage & {
  getLayout?: (page: ReactElement) => ReactNode
}

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout
}

export default function MyApp({ Component, pageProps }: AppPropsWithLayout) {
  // Use the layout defined at the page level, if available
  const getLayout = Component.getLayout ?? ((page) => page)

  return getLayout(<Component {...pageProps} />)
}
```

### References

[Persistent Layout Patterns in Next.js](https://adamwathan.me/2019/10/17/persistent-layout-patterns-in-nextjs/)



## Image component and optimization

The Next.js Image component, [`next/image`](https://nextjs.org/docs/api-reference/next/image), is an extension of the HTML `<img>` element.

- Improved performance
- Visual stability : prevent Cumulative Layout Shift automatically
- Faster page loads

```js
import Image from 'next/image'
```

### Local images

To use a local image, `import` your `.jpg`, `.png`, or `.webp` files. Only static `import` is allowed (not `require()`) so it can be analyzed at build time.

If static import is provided, Next.js will automatically determine the `width` and `height` of your image based on the imported file. It's for preventing Cumulative Layout Shift.

```js
import Image from 'next/image'
import profilePic from '../public/me.png'

function Home() {
  return (
    <>
      <h1>My Homepage</h1>
      <Image
        src={profilePic}
        alt="Picture of the author"
        // width={500} automatically provided
        // height={500} automatically provided
        // blurDataURL="data:..." automatically provided
        // placeholder="blur" // Optional blur-up while loading
      />
      <p>Welcome to my homepage!</p>
    </>
  )
}
```

### Remote images

To use a remote image, the `src` property should be a URL string. Because Next.js does not have access to remote files during the build process, you'll need to provide the `width`, `height` and optional `blurDataURL` props manually:

```js
<Image
  src="/me.png"
  alt="Picture of the author"
  width={500}
  height={500}
/>
```



## API routes

A solution to build API with Next.js. Any file inside the folder `pages/api` is mapped to `/api/*` and will be treated as an API endpoint instead of a `page`. They are server-side only bundles and won't increase your client-side bundle size.

```js
export default function handler(req, res) {
  res.status(200).json({ name: 'John Doe' })
}
```

This API route `pages/api/user.js` will return a json response with a status code of 200.

It needs to be exported as default (a.k.a request handler), which then receives the following parameters:

- `req` : An instance of `http.IncomingMessage`(with some middelwares)
- `res` : An instance of `http.ServerResponse`(with some helper functions)

To handle different HTTP methods:

```js
export default function handler(req, res) {
  if (req.method === 'POST') {
    // Process a POST request
  } else {
    // Handle any other HTTP method
  }
}
```

