# How to get the type of a variable

You can use one of these methods.

```kotlin
val obj: Double = 5.0

System.out.println(obj.javaClass.name)                 // double
System.out.println(obj.javaClass.kotlin)               // class kotlin.Double
System.out.println(obj.javaClass.kotlin.qualifiedName) // kotlin.Double
```



## References

https://stackoverflow.com/questions/32684739/kotlin-get-type-as-string

