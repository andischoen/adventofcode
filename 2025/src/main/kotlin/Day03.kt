package andi.aoc25

class Day03:IDay {
    override fun solve(part: Int) {
        val lines = getLinesFromPuzzleInput("input03.txt")

        val res = lines.map { bank -> getJoltage(bank) }.sum()

        println(res)
    }

    private fun getJoltage(bank: String):Int {
        val firstIndex = getLargestDigitIndex(bank, 0, bank.length-2)
        val joltage = StringBuffer()
        joltage.append(bank[firstIndex])
        val secondIndex = getLargestDigitIndex(bank, firstIndex+1, bank.length-1)
        joltage.append(bank[secondIndex])

        return joltage.toString().toInt()
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