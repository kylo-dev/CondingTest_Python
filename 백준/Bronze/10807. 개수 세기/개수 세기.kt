fun main() {
  var N = readln().toInt()
  var arr = readln().split(" ").map { it.toInt() }
  var find_n = readln().toInt()
  
  println(arr.count { it == find_n})
}