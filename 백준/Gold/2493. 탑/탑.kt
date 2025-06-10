fun main() {
    val N = readln().toInt()
    val arr = readln().split(" ").map { it.toInt() }
    val answer = IntArray(N)
    val stack = ArrayList<Int>()

    for (i in N - 1 downTo 0) {
        while (stack.isNotEmpty() && arr[i] >= arr[stack.last()]) {
            val idx = stack.removeLast()
            answer[idx] = i + 1
        }
        stack.add(i)
    }

    println(answer.joinToString(" "))
}