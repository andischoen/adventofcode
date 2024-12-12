package org.example

import java.io.BufferedReader

fun main() {

    val d = Day05()

    d.solve()

}

fun getTextFromPuzzleInput(filename: String): String {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/$filename")!!.bufferedReader()
    return bufferedReader.readText()
}

fun getLinesFromPuzzleInput(filename: String): List<String> {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/$filename")!!.bufferedReader()
    return bufferedReader.readLines()
}