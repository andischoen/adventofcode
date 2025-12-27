package andi.aoc25.day08

import andi.aoc25.IDay
import andi.aoc25.getLinesFromPuzzleInput

class Day08: IDay {
    private fun getDistance(p1: Triple<Int, Int, Int>, p2: Triple<Int, Int, Int>): Long {
        return  Math.powExact((p1.first - p2.first).toLong(), 2) +
                Math.powExact((p1.second - p2.second).toLong(), 2) +
                Math.powExact((p2.third - p1.third).toLong(), 2)
    }

    override fun solve(part: Int, sample: Boolean): String {
        val filename = if(sample) "input08-sample.txt" else "input08.txt"
        val points = getLinesFromPuzzleInput(filename).map {
            line ->
                val coordinates = line.split(",").map { it.toInt() }
            Triple(coordinates[0], coordinates[1], coordinates[2])
        }

        val distances = ArrayList<Triple<Triple<Int, Int, Int>, Triple<Int, Int, Int>, Long>>()
        for(i in points.indices) {
            for(j in i+1 until points.size) {
                distances.add(Triple(points[i], points[j], getDistance(points[i], points[j])))
            }
        }

        distances.sortBy { it.third }

        return ""
    }
}