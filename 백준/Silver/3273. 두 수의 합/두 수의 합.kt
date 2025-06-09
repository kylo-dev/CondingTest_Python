fun main() {
    var n = readln().toInt()
    var arr = readln().split(" ").map { it.toInt() }.sorted()
    var k = readln().toInt()

    var (start, end) = 0 to arr.lastIndex
    var answer: Int = 0

    while (start < end) {
        var sum = arr[start] + arr[end]

        if (sum > k) {
            end -= 1
        } else if (sum < k) {
            start += 1
        } else {
            answer += 1
            start += 1
            end -= 1
        }
    }

    println(answer)

}