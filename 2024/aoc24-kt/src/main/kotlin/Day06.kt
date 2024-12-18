package org.example

class Day06: IDay {
    private var posY: Int = 0
    private var posX: Int = 0
    private lateinit var lines: List<String>

    override fun solve() {
        lines = getLinesFromPuzzleInput("input06-test.txt")

        determineGuardPosition(lines)

        print("Guard position: $posX / $posY")
    }

    private fun determineGuardPosition(lines: List<String>) {
        for (y in lines.indices)
            for (x in lines[y].indices)
                if (lines[y][x] in listOf('^', 'v', '<', '>')) {
                    posX = x
                    posY = y
                }
    }
}