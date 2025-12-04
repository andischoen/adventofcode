package andi.aoc25.day02

import andi.aoc25.IDay
import andi.aoc25.getLinesFromPuzzleInput
import andi.aoc25.getTextFromPuzzleInput

class Day02: IDay {
    override fun solve() {
        val ranges = getTextFromPuzzleInput("input02.txt").split(",")

        val regex = Regex("(.+)\\1")

        val fakeIds = ArrayList<List<String>>()

        for (range in ranges) {
            val ids : List<String> = expand(range)
            val tempFakeIds = ids.filter { id ->  regex.matches(id)}.toList()
            fakeIds.add(tempFakeIds)
            tempFakeIds.forEach{fakeId -> println(fakeId)}
        }

        val res = fakeIds.flatten().map { fakeId -> fakeId.toLong() }.sum();

        println("Sum of fake Ids = $res");
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