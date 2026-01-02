package andi.aoc25.day09

import andi.aoc25.IDay
import andi.aoc25.getLinesFromPuzzleInput
import kotlin.math.abs

class Day09: IDay {
    override fun solve(part: Int, sample: Boolean): String {
        val filename = if(sample) "input09-sample.txt" else "input09.txt"
        val initialTiles = getLinesFromPuzzleInput(filename).map{ line ->
            val coords = line.split(",").map{ it.toInt()}
            Pair(coords[0], coords[1])
        }

        var maxArea:Long = 0
        for(i in initialTiles.indices) {
            for(j in i+1..initialTiles.lastIndex) {
                val area = calculateArea(initialTiles[i], initialTiles[j])
                if(maxArea<area) maxArea=area
            }
        }

        return maxArea.toString()
    }

    private fun calculateArea(pointA: Pair<Int, Int>, pointB: Pair<Int, Int>) : Long {
        return abs((pointA.first-pointB.first+1).toLong()*(pointA.second-pointB.second+1).toLong())
    }
}