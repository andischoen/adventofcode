package org.example

import java.io.BufferedReader
import kotlin.math.absoluteValue

fun main(args: Array<String>) {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/input.txt")!!.bufferedReader()
    val lines = bufferedReader.readLines()

    var cnt = 0
    lines.forEach { line ->
        val numStrs = line.split(" ")

        var isSave: Boolean = true
        var num = numStrs[0].toInt()
        var diff: Int
        val isDecreasing: Boolean = (num > numStrs[1].toInt())
        for (i in 1..<numStrs.size) {
            diff = num - numStrs[i].toInt()
            num = numStrs[i].toInt()
            if (diff.absoluteValue !in 1.. 3) {
                isSave = false
                break
            }
            if(diff > 0 && !isDecreasing || diff < 0 && isDecreasing) {
                isSave = false
                break
            }
        }

        if (isSave) {
            cnt++
        }
    }

    println(cnt)


}