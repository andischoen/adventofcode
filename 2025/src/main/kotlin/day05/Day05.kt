package andi.aoc25.day05

import andi.aoc25.IDay
import andi.aoc25.getTextFromPuzzleInput

class Day05 : IDay{
    override fun solve(part: Int, sample: Boolean): String {
        val filename = if(sample) "input05-sample.txt" else "input05.txt"
        val input = getTextFromPuzzleInput(filename)
        val inputParts = input.split(Regex("\\r\\n\\r\\n"))

        val strRanges = inputParts[0].split(Regex("\\r\\n")).map { r -> r.split("-").map { limit -> limit.toLong() } }
        var ranges = strRanges.map { limits -> limits[0]..limits[1] }

        val ingredients = inputParts[1].split(Regex("\\r\\n")).map { i -> i.toLong() }

        var res:Long = 0
        if(part == 1) {
            res = ingredients.count { i -> ranges.any { r -> i in r } }.toLong()
        } else {
            ranges = ranges.sortedBy { r -> r.first }
            ranges = joinRanges(ranges)
            res = ranges.sumOf { r -> (r.last-r.first+1) }
        }
        return res.toString()
    }

    private fun joinRanges(ranges: List<LongRange>): List<LongRange> {
        val joinedRanges = ArrayList<LongRange>()
        var tempRange = ranges[0]
        var i = 1
        do {
            while (i < ranges.size && ranges[i].first in tempRange) {
                if (ranges[i].last !in tempRange) { // second range overlaps with first so extend the range (otherwise ignore this range)
                    tempRange = tempRange.first..ranges[i].last
                }
                i++
            }
            //so no overlap anymore, this range is complete
            joinedRanges.add(tempRange)
            if(i < ranges.size) tempRange = ranges[i]
            i++
        } while(i < ranges.size)
        return joinedRanges
    }
}