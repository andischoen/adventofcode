package andi.aoc25.day05

import andi.aoc25.IDay
import andi.aoc25.getTextFromPuzzleInput

class Day05 : IDay{
    override fun solve(part: Int, sample: Boolean): String {
        val filename = if(sample) "input05-sample.txt" else "input05.txt"
        val input = getTextFromPuzzleInput(filename)
        val inputParts = input.split(Regex("\\r\\n\\r\\n"))

        val strRanges = inputParts[0].split(Regex("\\r\\n")).map { r -> r.split("-").map { limit -> limit.toLong() } }
        val ranges = strRanges.map { limits -> limits[0]..limits[1] }

        val ingredients = inputParts[1].split(Regex("\\r\\n")).map { i -> i.toLong() }

        val res = ingredients.count { i -> ranges.any { r -> i in r } }

        return res.toString()
    }
}