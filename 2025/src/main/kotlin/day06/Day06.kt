package andi.aoc25.day06

import andi.aoc25.IDay
import andi.aoc25.getLinesFromPuzzleInput
import andi.aoc25.getTextFromPuzzleInput

class Day06: IDay {
    override fun solve(part: Int, sample: Boolean): String {
        val filename = if(sample) "input06-sample.txt" else "input06.txt"

        val results = ArrayList<Long>()

        if(part == 1) {
            getPart1Results(filename, results)
        } else {
            getPart2Results(filename, results)
        }
        return results.sum().toString();
    }

    private fun getPart2Results(filename: String, results: ArrayList<Long>) {
        val lines = getLinesFromPuzzleInput(filename)

        val rawOperands = lines.dropLast(1)
        val operators = lines.last().split(Regex("""\s+"""))

        var operands = ArrayList<Long>()
        var operatorsIndex = 0
        fun operate() {
            if (operators[operatorsIndex] == "+") {
                results.add(operands.sum())
            } else {
                results.add(operands.reduce { acc, op -> acc * op })
            }
        }

        for (i in 0..rawOperands[0].lastIndex) {
            val operand = rawOperands.map { l -> l[i] }.joinToString("").trim()
            if (operand.isEmpty()) {
                operate()
                operatorsIndex++
                operands = ArrayList<Long>()
            } else {
                operands.add(operand.toLong())
            }
        }
        operate()
    }

    private fun getPart1Results(filename: String, results: ArrayList<Long>) {
        val lines =
            getTextFromPuzzleInput(filename).split(Regex("""\r\n""")).map { l -> l.trim().split(Regex("""\s+""")) }

        for (i in 0..<lines[0].size) {
            val operands = lines.dropLast(1).map { l -> l[i].toLong() }
            if (lines.last()[i] == "+") {
                results.add(operands.sum())
            } else {
                results.add(operands.reduce { acc, op -> acc * op })
            }
        }
    }
}