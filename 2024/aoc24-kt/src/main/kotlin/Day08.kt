package org.example

class Day08: IDay {

    var frequencies = mutableMapOf<Char, MutableList<Pair<Int, Int>>>()
    var antinodes = mutableSetOf<Pair<Int,Int>>()

    override fun solve() {
        val lines = getLinesFromPuzzleInput("input08.txt")

        // get a map of all frequencies and their locations
        recordFrequencies(lines)

        println(frequencies)

        //build all combinations of each frequency and place the antinodes
        val xRange = lines[0].indices
        val yRange = lines.indices
        frequencies.values.forEach() { placeAntinodes(it, xRange, yRange) }

        println(antinodes)

        //then simply count the set
        println("Number of antinodes: ${antinodes.size}")
    }

    private fun placeAntinodes(antennas: MutableList<Pair<Int, Int>>, xRange: IntRange, yRange: IntRange) {
        for(i in antennas.indices) {
            for(j in i+1 .. antennas.size-1) {
                val a = antennas[i]
                val b = antennas[j]

                // a -> b
                var deltaX = b.first - a.first
                var deltaY = b.second - a.second
                var x = (b.first + deltaX)
                var y = (b.second + deltaY)

                if(x in xRange && y in yRange) antinodes.add(x to y)

                // b -> a
                deltaX = a.first - b.first
                deltaY = a.second - b.second
                x = (a.first + deltaX)
                y = (a.second + deltaY)

                if(x in xRange && y in yRange) antinodes.add(x to y)
            }
        }
    }

    private fun recordFrequencies(lines: List<String>) {
        for (y in lines.indices) {
            for (x in lines[y].indices) {
                val chr = lines[y][x]
                if (chr != '.') {
                    if (frequencies.containsKey(chr)) {
                        frequencies[chr]?.add(x to y)
                    } else {
                        frequencies[chr] = mutableListOf(x to y)
                    }
                }
            }
        }
    }
}