package andi.aoc25.day04

import andi.aoc25.IDay
import andi.aoc25.getLinesFromPuzzleInput

class Day04: IDay {

    data class Coordinate(val x:Int, val y:Int)
    val N  = Coordinate( 0,-1)
    val NE = Coordinate( 1,-1)
    val E  = Coordinate( 1, 0)
    val SE = Coordinate( 1, 1)
    val S  = Coordinate( 0, 1)
    val SW = Coordinate(-1, 1)
    val W  = Coordinate(-1, 0)
    val NW = Coordinate(-1,-1)
    val directions = listOf<Coordinate>(
        N, NE, E, SE, S, SW, W, NW
    )

    lateinit var map:List<String>

    private fun checkIfMovablePaper(ch: Char, x: Int, y: Int):Boolean {
        if(ch != '@') return false
        else {
            val xLastInd = map[0].length - 1
            val yLastInd = map.size - 1
            var paperCount = 0
            for (offset in directions) {
                val surroundX = x+offset.x
                val surroundY = y+offset.y

                if(surroundX in 0..xLastInd
                   && surroundY in 0 .. yLastInd
                   && map[surroundY][surroundX] == '@')
                    paperCount++
            }
            if(paperCount<4) return true
            return false
        }
    }

    override fun solve(part: Int, sample: Boolean): String {
        val filename:String =
            if(sample) "input04-sample.txt"
            else "input04.txt"

        map = getLinesFromPuzzleInput(filename)
        var counter = 0
        for(y in 0 .. map.size-1) {
            val line = map[y];
            for (x in 0 .. line.length-1 ) {
                counter += if(checkIfMovablePaper(line[x], x, y)) 1 else 0
            }
        }

        return counter.toString();
    }
}