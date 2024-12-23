package org.example

class Day06: IDay {
    private var initialGuard = ' '
    private var initialPosY = 0
    private var initialPosX = 0
    private var posY: Int = 0
    private var posX: Int = 0
    private var guard: Char = ' '
    private lateinit var lines: List<CharArray>
    private var directions = hashMapOf(
        '^' to intArrayOf(0,-1),
        '>' to intArrayOf(1,0),
        'v' to intArrayOf(0,1),
        '<' to intArrayOf(-1,0))
    private var path = mutableMapOf<Pair<Int, Int>, Char>()

    override fun solve() {
        lines = getLinesFromPuzzleInput("input06.txt").map { it.toCharArray()}

        determineGuardPosition()

        println("Guard position: $posX / $posY")
        while (moveGuard(true)) {}
        printArea()

        println("the covered path is = ${countArea()}")

        //println(path.map { it.key.contentToString() + ":" + it.value })

        // part 02: find single obstructions to cause a loop
        //      run part 01
        //      build an obstruction on each position of the path (except start)
        //      and check each time if there's a loop
        //      loop check:
        //          remember the path with directions... a map maybe?
        //              Key is the position, value is direction, what about turns? ^>?
        //          if guard is on same position with same direction we have a loop

        var obstructionCnt = 0
        for (p in path.keys) {
            if(loopDetected(p)) {
                obstructionCnt++
            }
        }

        println("Number of obstructions to create a loop: $obstructionCnt")
    }

    private fun loopDetected(p: Pair<Int, Int>): Boolean {
        // reset the guard
        posX = initialPosX
        posY = initialPosY
        guard = initialGuard
        val detectionPath = mutableMapOf<Pair<Int, Int>, Char>()

        var loop = false
        if (p.first == initialPosX && p.second == initialPosY) return false //no obstruction on initial position

        // set the obstruction
        lines[p.second][p.first] = '#'

        var failsafe = 0 // this is ugly but necessary, something's not sound in my loop detection
        while (moveGuard(false)) {
            failsafe++
            if(detectionPath[posX to posY] == guard || failsafe > 12000) {
                loop = true
                break
            }
            detectionPath[posX to posY] = guard
        }

        // reset the obstruction
        lines[p.second][p.first] = '.'
        return loop
    }

    private fun moveGuard(recordPath:Boolean): Boolean {
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
            //and while we are at it, record the path
            if(recordPath) path[posX to posY] = guard
        }

        return true
    }

    private fun determineGuardPosition() {
        for (y in lines.indices)
            for (x in lines[y].indices)
                if (lines[y][x] in listOf('^', 'v', '<', '>')) {
                    posX = x
                    posY = y
                    initialPosX = x
                    initialPosY = y
                    guard = lines[y][x]
                    initialGuard = guard
                    lines[y][x] = '.'
                }
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