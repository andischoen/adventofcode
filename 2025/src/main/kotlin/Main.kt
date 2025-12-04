package andi.aoc25

import andi.aoc25.day02.Day02
import java.io.BufferedReader


fun main() {
    val day02 = Day02();

    day02.solve();
}


fun getLinesFromPuzzleInput(filename: String): List<String> {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/$filename")!!.bufferedReader()
    return bufferedReader.readLines()
}

fun getTextFromPuzzleInput(filename: String): String {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/$filename")!!.bufferedReader()
    return bufferedReader.readText()
}