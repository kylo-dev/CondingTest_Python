fun main() {
  val K = readln().toInt()
  val arr = mutableListOf<Int>()

  repeat(K) {
    var n = readln().toInt()
    if (n == 0 && !arr.isEmpty()) {
      arr.removeLast()
    } else {
      arr.add(n)
    }
  }
  println(arr.sum())
}