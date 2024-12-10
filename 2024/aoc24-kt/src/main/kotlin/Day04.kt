package org.example

import java.io.BufferedReader

const val xmas = "XMAS"
val dirs: Array<IntArray> = arrayOf(
    intArrayOf(1, 0), //east
    intArrayOf(1, 1), //southeast
    intArrayOf(0, 1), //south
    intArrayOf(-1, 1), //southwest
    intArrayOf(-1, 0), //west
    intArrayOf(-1, -1), //northwest
    intArrayOf(0, -1), //north
    intArrayOf(1, -1)  //northeast
)

fun main() {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/input04.txt")!!.bufferedReader()
    val lines = bufferedReader.readLines()

    var cnt = 0
    for (y in lines.indices) {
        val line = lines[y]
        for (x in line.indices) {
            val c = line[x]

            if (c == 'X') {
                cnt += countXmas(lines, x, y)
            }
        }
    }

    print(cnt)
}

fun countXmas(lines: List<String>, x: Int, y: Int): Int {
    var cnt = 0
    dirs.forEach {
        var found = true
        for (i in 1..3) {
            //calculate the next letter in each direction
            val offsetX = x + (it[0]*i)
            val offsetY = y + (it[1]*i)
            var charOk = (offsetX in lines[0].indices) && (offsetY in lines.indices) && lines[offsetY][offsetX] == xmas[i]
            found = found &&  charOk
        }
        if(found) cnt++
    }
    return cnt
}
