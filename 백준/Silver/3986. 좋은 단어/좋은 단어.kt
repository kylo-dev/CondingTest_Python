import java.util.*

fun main() {
    val N = readln().toInt()
    var answer = 0

    repeat(N) {
        val stack = Stack<Char>()
        val word = readln()

        for (w in word) {
            if (stack.isEmpty()) {
                stack.add(w)
            } else if (stack.isNotEmpty() && stack.last() == w) {
                stack.pop()
            } else {
                stack.add(w)
            }
        }
        if (stack.isEmpty()) {
            answer++
        }
    }

    println(answer)
}