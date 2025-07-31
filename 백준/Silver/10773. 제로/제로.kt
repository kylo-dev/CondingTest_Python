fun main() {
    val K = readln().toInt()
    val arr = mutableListOf<Int>()

    for (i in 1..K) {
        val n = readln().toInt()
        if (n == 0) {
            arr.removeLast()
        } else {
            arr.add(n)
        }
    }
    println(arr.sum())
}