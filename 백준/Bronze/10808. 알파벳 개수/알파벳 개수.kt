fun main() {

    var input = readln()

    var arr = IntArray(26) { 0 }

    for (ch in input) {
        arr[ch.code - 97] += 1
    }
    print(arr.joinToString(" "))
}