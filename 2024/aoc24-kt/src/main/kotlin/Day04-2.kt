package org.example

import java.io.BufferedReader

//northwest, northeast, southwest, southeast =>
// M.M
// .A.
// S.S
// => MMSS
var possibleCrosses = arrayOf("MMSS", "MSMS", "SMSM", "SSMM")


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
    if(x in 1..lines[1].length-2 && y in 1 .. lines.size-2) {
        var cross = StringBuilder()
        cross.append(lines[y-1][x-1])
        cross.append(lines[y-1][x+1])
        cross.append(lines[y+1][x-1])
        cross.append(lines[y+1][x+1])

        if (cross.toString() in possibleCrosses) {
            cnt = 1
        }
    }
    return cnt
}
