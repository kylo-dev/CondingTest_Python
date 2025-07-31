fun main() {
    val n = readln().toInt()
    val arr = readln().split(" ").map { it.toInt() }
    val stack = mutableListOf<Int>()

    val answer = IntArray(n) { 0 }

    for (i in 0 until n) {
        while (stack.isNotEmpty()) {
            if (arr[stack.last()] > arr[i]) {
                answer[i] = stack.last() + 1
                break
            } else {
                stack.removeLast()
            }
        }
        stack.add(i)
    }
    println(answer.joinToString(" "))

}