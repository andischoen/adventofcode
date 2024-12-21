package org.example

class Day06: IDay {
    private var posY: Int = 0
    private var posX: Int = 0
    private var guard: Char = ' '
    private lateinit var lines: List<CharArray>
    private var directions = hashMapOf(
        '^' to intArrayOf(0,-1),
        '>' to intArrayOf(1,0),
        'v' to intArrayOf(0,1),
        '<' to intArrayOf(-1,0))

    override fun solve() {
        lines = getLinesFromPuzzleInput("input06.txt").map { it.toCharArray()}

        determineGuardPosition()

        println("Guard position: $posX / $posY")
        while (moveGuard()) {}
        printArea()

        println("the covered path is = ${countArea()}")
    }

    private fun determineGuardPosition() {
        for (y in lines.indices)
            for (x in lines[y].indices)
                if (lines[y][x] in listOf('^', 'v', '<', '>')) {
                    posX = x
                    posY = y
                    guard = lines[y][x]
                    lines[y][x] = '.'
                }
    }

    private fun moveGuard(): Boolean {
        val nextPosX = posX + directions[guard]!![0]
        val nextPosY = posY + directions[guard]!![1]

        lines[posY][posX] = '*'

        if(nextPosY !in lines.indices || nextPosX !in lines[0].indices) {
            // the guard has left the building
            return false
        }

        if (lines[nextPosY][nextPosX] == '#') {
            // change directions!!!
            changeDirection()
        } else {
            // move!
            posX = nextPosX
            posY = nextPosY
        }

        return true
    }

    private fun changeDirection() {
        when(guard) {
            '^' -> guard = '>'
            '>' -> guard = 'v'
            'v' -> guard = '<'
            '<' -> guard = '^'
        }
    }

    private fun printArea() {
        lines.forEach() {
            println(it)
        }
    }

    private fun countArea(): Int {
        val pathCount = lines.sumOf { it.count { c -> c == '*' } }
        return pathCount
    }
}