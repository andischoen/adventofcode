package andi.aoc25

import andi.aoc25.day02.Day02
import andi.aoc25.day03.Day03
import andi.aoc25.day04.Day04
import andi.aoc25.day05.Day05
import java.io.BufferedReader


fun main() {
    val day02 = Day02()
    val day03 = Day03()
    val day04 = Day04()
    val day05 = Day05()

//    println("day 02, part 1 -> " + day02.solve(1))
//    println("day 02, part 2 -> " + day02.solve(2))
//    println("day 03, part 1 -> " + day03.solve(1))
//    println("day 03, part 2 -> " + day03.solve(2, false))
//    println("day 04, part 1 -> " + day04.solve(1, false))
//    println("day 04, part 2 -> " + day04.solve(2, false))
    println("day 05, part 1 -> " + day05.solve(1, false))

}


fun getLinesFromPuzzleInput(filename: String): List<String> {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/$filename")!!.bufferedReader()
    return bufferedReader.readLines()
}

fun getTextFromPuzzleInput(filename: String): String {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/$filename")!!.bufferedReader()
    return bufferedReader.readText()
}