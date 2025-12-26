package andi.aoc25.day07

import andi.aoc25.IDay
import andi.aoc25.getLinesFromPuzzleInput

class Day07: IDay {

    val debug = true

    val cache = mutableMapOf<Pair<Int, Int>, Long>()
    lateinit var lines:List<String>

    override fun solve(part: Int, sample: Boolean): String {
        val filename = if(sample) "input07-sample.txt" else "input07.txt"
        lines = getLinesFromPuzzleInput(filename)

        if(part == 1) {
            var splits = solvePart1(lines)

            return splits.toString()
        } else {
            val line = 0
            val start = lines[0].indexOf('S')

            val paths = calculatePathsFrom(Pair(line+1, start))
            return paths.toString()
        }
    }

    //fun factorial(n: Int): Int = cache.getOrPut(n) { // <-- this is the fix
    //    when (n) {
    //        0, 1 -> 1
    //        else -> n * factorial(n - 1)
    //    }
    //}
    private fun calculatePathsFrom(p: Pair<Int, Int>):Long {
        if(cache.containsKey(p)) return cache.getValue(p)
        if(p.first > lines.lastIndex) {
            cache[p] = 1
            return 1
        }
        if(lines[p.first][p.second] == '^') {
            val r = calculatePathsFrom(Pair(p.first+1, p.second+1)) + calculatePathsFrom(Pair(p.first+1, p.second-1))
            cache[p] = r
            return r;
        } else {
            val r = calculatePathsFrom(Pair(p.first+1, p.second))
            cache[p] = r
            return r
        }
    }

    private fun solvePart1(lines: List<String>): Int {
        var splits = 0
        var indices = HashSet<Int>()
        for (line in lines) {
            if (line.contains("S")) { // first line
                indices.add(line.indexOf('S'))
                if (debug) println(line)
            } else {
                val nextIndices = HashSet<Int>()
                val thisLine = StringBuilder()
                for (i in indices) {
                    if (line[i] == '.') {
                        nextIndices.add(i)
                    } else if (line[i] == '^') {
                        splits++
                        if ((i - 1) >= 0) nextIndices.add(i - 1)
                        if ((i + 1) <= line.lastIndex) nextIndices.add(i + 1)
                    }
                }
                if (debug) {
                    for (i in 0 until lines.size) {
                        if (nextIndices.contains(i)) thisLine.append('|')
                        else if (indices.contains(i)) thisLine.append('^')
                        else thisLine.append('.')
                    }
                    println(thisLine.toString())
                }
                indices = nextIndices
            }
        }
        return splits
    }
}