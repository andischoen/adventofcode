package andi.aoc25.day06

import andi.aoc25.IDay
import andi.aoc25.getTextFromPuzzleInput

class Day06: IDay {
    override fun solve(part: Int, sample: Boolean): String {
        val filename = if(sample) "input06-sample.txt" else "input06.txt"

        val lines = getTextFromPuzzleInput(filename).split(Regex("""\r\n""")).map { l -> l.split(Regex("""\s+""")) }

        val results = ArrayList<Long>()
        for(i in 0..<lines[0].size) {
            val operands = lines.dropLast(1).map { l -> l[i].toLong() }
            if(lines.last()[i] == "+")  {
                results.add(operands.sum())
            } else {
                results.add(operands.reduce { acc, op -> acc*op  })
            }
        }

        return results.sum().toString();
    }
}