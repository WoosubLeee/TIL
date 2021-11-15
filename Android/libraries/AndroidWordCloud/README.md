# AndroidWordCloud

Word cloud를 생성할 수 있는 라이브러리이다.

<img src="https://cloud.githubusercontent.com/assets/4659608/20027391/5e76fd3c-a324-11e6-99d9-14fae8c85838.png" alt="img" style="zoom: 25%;" />



## Installation

`build.gradle(:app)`에 추가

```kotlin
dependencies {
	compile 'net.alhazmy13.wordcloud:library:0.2.0-beta'
}
```



## Usage

```kotlin
<net.alhazmy13.wordcloud.WordCloudView
       android:id="@+id/wordCloud"
       android:layout_width="match_parent"
       android:layout_height="match_parent" />
```

```kotlin
WordCloudView wordCloud = (WordCloudView) findViewById(R.id.wordCloud);
        wordCloud.setDataSet(list);
        wordCloud.notifyDataSetChanged();
```

### Setting color

There are two option to change the colors, either by passing an array of `int` or by using a predefined colors from `ColorTemplate` class.

```java
wordCloud.setColors(new int[] {Color.BLUE, Color.GRAY, Color.GREEN, Color.CYAN });
//OR
wordCloud.setColors(ColorTemplate.MATERIAL_COLORS);
```



## References

https://github.com/alhazmy13/AndroidWordCloud

