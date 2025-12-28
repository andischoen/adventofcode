package andi.aoc25.day09

import andi.aoc25.IDay
import andi.aoc25.getLinesFromPuzzleInput

class Day09: IDay {
    override fun solve(part: Int, sample: Boolean): String {
        val filename = if(sample) "input09-sample.txt" else "input09.txt"
        val initialTiles = getLinesFromPuzzleInput(filename).map{ line ->
            val coords = line.split(",").map{ it.toInt()}
            Pair(coords[0], coords[1])
        }

        return ""
    }
}