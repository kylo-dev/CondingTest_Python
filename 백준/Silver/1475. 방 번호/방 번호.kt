import kotlin.math.ceil

fun main() {

    val num = readln().toInt()

    val arr = IntArray(9) { 0 }

    for (n in num.toString()) {
        if (n == '9') {
            arr[6] += 1
        } else {
            arr[n.digitToInt()] += 1
        }
    }
    arr[6] = ceil(arr[6].toDouble() / 2).toInt()

    println(arr.max())
}