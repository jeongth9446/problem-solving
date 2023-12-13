fun main() {
    val a = readlnOrNull()?.split(" ")
    a?.let {
        println(a[0].toInt() + a[1].toInt())
    }
}