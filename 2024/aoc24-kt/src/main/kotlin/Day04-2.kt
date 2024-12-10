package org.example

import java.io.BufferedReader



fun main() {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/input04.txt")!!.bufferedReader()
    val lines = bufferedReader.readLines()

    var cnt = 0
    for (y in lines.indices) {
        val line = lines[y]
        for (x in line.indices) {
            val c = line[x]

            if (c == 'A') {
                cnt += countMas(lines, x, y)
            }
        }
    }

    print(cnt)
}

fun countMas(lines: List<String>, x: Int, y: Int): Int {
    var cnt = 0
    if(x in 1..lines[1].length-2) {

    }
    return cnt
}
