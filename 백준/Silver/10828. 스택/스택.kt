fun main() {
    var N = readln().toInt()
    var arr = mutableListOf<Int>()

    repeat(N) {
        var cmd = readln().split(" ")

        when (cmd[0]) {
            "push" -> arr.add(cmd[1].toString().toInt())
            "pop" -> if (arr.isEmpty()) println(-1) else println(arr.removeLast())
            "top" -> if (arr.isEmpty()) println(-1) else println(arr[arr.lastIndex])
            "size" -> println(arr.size)
            "empty" -> if (arr.isEmpty()) println(1) else println(0)
        }
    }

}