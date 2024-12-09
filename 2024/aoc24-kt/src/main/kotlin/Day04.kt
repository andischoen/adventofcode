package org.example

import java.io.BufferedReader

fun main() {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/input.txt")!!.bufferedReader()
    val lines = bufferedReader.readLines()

    print(lines[3])
}