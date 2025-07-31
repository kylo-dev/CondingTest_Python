fun main() {
    val N: Int = readln().toInt()

    val arr = mutableListOf<Int>()

    for (i in 0 until N) {
        val input = readln().split(" ")

        when (input[0]) {
            "push" -> arr.add(input[1].toInt())
            "top" -> if (arr.isNotEmpty()) println(arr.last()) else println(-1)
            "pop" -> if (arr.isNotEmpty()) println(arr.removeLast()) else println(-1)
            "size" -> println(arr.size)
            "empty" -> if (arr.isEmpty()) println(1) else println(0)
            else -> null
        }
    }
}