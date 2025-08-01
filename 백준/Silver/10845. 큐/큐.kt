fun main() {
    val N = readln().toInt()

    val queue = ArrayDeque<Int>()
    
    repeat(N) {
        val input = readln().split(" ")
        
        when (input[0]) {
            "push" -> queue.add(input[1].toInt())
            "pop" -> if (queue.isNotEmpty()) println(queue.removeFirst()) else println(-1)
            "size" -> println(queue.size)
            "empty" -> if (queue.isEmpty()) println(1) else println(0)
            "front" -> if (queue.isNotEmpty()) println(queue.first()) else println(-1)
            "back" -> if (queue.isNotEmpty()) println(queue.last()) else println(-1)
            else -> null
        }
    }
}