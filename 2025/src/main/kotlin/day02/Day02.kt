package andi.aoc25.day02

import andi.aoc25.IDay
import andi.aoc25.getTextFromPuzzleInput

class Day02: IDay {
    override fun solve(part: Int, sample: Boolean): String {
        val ranges = getTextFromPuzzleInput("input02.txt").split(",")
        val regex:Regex = if(part == 1) Regex("(.+)\\1") else Regex("(.+)\\1+")

        val fakeIds = ArrayList<List<String>>()

        for (range in ranges) {
            val ids : List<String> = expand(range)
            val tempFakeIds = ids.filter { id ->  regex.matches(id)}.toList()
            fakeIds.add(tempFakeIds)
            tempFakeIds.forEach{fakeId -> println(fakeId)}
        }

        val res = fakeIds.flatten().sumOf { fakeId -> fakeId.toLong() };

        return res.toString()
    }

    private fun extracted(id: String) {
        println(id)
    }

    private fun expand(range: String): List<String> {
        val startEnd = range.split("-")

        val start = startEnd[0].toLong()
        val end = startEnd[1].toLong()
        return (start .. end).map { l -> l.toString() }.toList();
    }
}