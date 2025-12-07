package andi.aoc25.day03

import andi.aoc25.IDay
import andi.aoc25.getLinesFromPuzzleInput

class Day03: IDay {
    

    override fun solve(part: Int, sample: Boolean): String {
        var fileName = "input03.txt"
        if(sample) {
            fileName = "input03-sample.txt"
        }
        val lines = getLinesFromPuzzleInput(fileName)

        var res:Long
        if(part == 1) {
            res = lines.sumOf { bank -> getJoltage(bank) }
        } else {
            res = lines.sumOf { bank -> getJoltageDigits(bank, 12) }
        }

        return res.toString()
    }

    private fun getJoltage(bank: String):Long {
        val firstIndex = getLargestDigitIndex(bank, 0, bank.length-2)
        val joltage = StringBuffer()
        joltage.append(bank[firstIndex])
        val secondIndex = getLargestDigitIndex(bank, firstIndex+1, bank.length-1)
        joltage.append(bank[secondIndex])

        return joltage.toString().toLong()
    }

    private fun getJoltageDigits(bank: String, size: Int):Long {
        var index = -1
        val joltage = StringBuffer()
        for(i in 1.. size) {
            index = getLargestDigitIndex(bank, index+1, bank.length-1-size+i)
            joltage.append(bank[index])
        }
        return joltage.toString().toLong()
    }

    private fun getLargestDigitIndex(bank: String, start: Int, lastIndex: Int): Int {
        var ind = 0
        var v = 0
        for(i in start .. lastIndex) {
            if(v == 9) break
            if(bank[i].digitToInt() > v) {
                ind = i
                v = bank[i].digitToInt()
            }
        }

        return ind
    }
}