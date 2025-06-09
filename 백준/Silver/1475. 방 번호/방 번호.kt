fun main() {
    var input = readln().toInt()
    var count = IntArray(10) { 0 }

    for (num in input.toString()) {
        val idx = num.digitToInt()

        if (idx == 6 || idx == 9) {
            count[6] += 1
        } else {
            count[idx] += 1
        }
    }
    count[6] = (count[6] + 1) / 2

    println(count.max())
}