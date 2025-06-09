fun main() {

    var inputs = mutableListOf<Int>()
    var nums = IntArray(10) { 0 }

    repeat(3) {
        inputs.add(readln().toInt())
    }

    var total = inputs.reduce {
            sum, value -> sum * value
    }.toString()

    for (t in total) {
        nums[t.toString().toInt()] += 1
    }

    println(nums.joinToString("\n"))
}