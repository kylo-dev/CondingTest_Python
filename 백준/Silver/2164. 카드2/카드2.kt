import java.util.ArrayDeque

fun main() {
    val N = readln().toInt()
    val que = ArrayDeque<Int>().apply { addAll(1..N) }

    while (que.size != 1) {
        que.removeFirst()
        que.add(que.removeFirst())
    }
    println(que.first)
}