package andi.aoc25

import andi.aoc25.day02.Day02
import java.io.BufferedReader


fun main() {
    //val day = Day02();
    val day = Day03();

    day.solve(1);
}


fun getLinesFromPuzzleInput(filename: String): List<String> {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/$filename")!!.bufferedReader()
    return bufferedReader.readLines()
}

fun getTextFromPuzzleInput(filename: String): String {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/$filename")!!.bufferedReader()
    return bufferedReader.readText()
}