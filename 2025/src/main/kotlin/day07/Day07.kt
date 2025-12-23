package andi.aoc25.day07

import andi.aoc25.IDay
import andi.aoc25.getLinesFromPuzzleInput

class Day07: IDay {

    val debug = true

    override fun solve(part: Int, sample: Boolean): String {
        val filename = if(sample) "input07-sample.txt" else "input07.txt"
        val lines = getLinesFromPuzzleInput(filename)

        var indices = HashSet<Int>()
        var splits = 0
        for(line in lines) {
            if(line.contains("S")) { // first line
                indices.add(line.indexOf('S'))
                if(debug) println(line)
            } else {
                val nextIndices = HashSet<Int>()
                val thisLine = StringBuilder()
                for(i in indices) {
                    if(line[i] == '.') {
                        nextIndices.add(i)
                    } else if(line[i] == '^') {
                        splits++
                        if ((i - 1) >= 0) nextIndices.add(i - 1)
                        if ((i + 1) <= line.lastIndex) nextIndices.add(i + 1)
                    }
                }
                if(debug) {
                    for (i in 0 until lines.size) {
                        if (nextIndices.contains(i)) thisLine.append('|')
                        else if(indices.contains(i)) thisLine.append('^')
                        else thisLine.append('.')
                    }
                    println(thisLine.toString())
                }
                indices = nextIndices
            }
        }

        return splits.toString()
    }
}