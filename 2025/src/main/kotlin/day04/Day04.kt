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

    lateinit var map:List<CharArray>

    private fun checkIfMovablePaper(ch: Char, x: Int, y: Int):Boolean {
        if(ch != '@') return false
        else {
            val xLastInd = map[0].size - 1
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

        map = getLinesFromPuzzleInput(filename).map { l -> l.toCharArray() }


        var counter = 0
        if(part == 1) {

            counter = countAndRemoveMovablePaper()

        } else {

            var c = 0
            do {
                c = countAndRemoveMovablePaper()
                counter += c
            } while(c>0)

        }

        return counter.toString();
    }

    private fun countAndRemoveMovablePaper(): Int {
        var cnt = 0
        val toBeRemoved = ArrayList<Coordinate>()
        for (y in 0..<map.size) {
            val line = map[y];
            for (x in 0..<line.size) {
                if (checkIfMovablePaper(line[x], x, y)) {
                    cnt++
                    toBeRemoved.add(Coordinate(x, y))
                }
            }
        }

        for (coordinate in toBeRemoved) {
            map[coordinate.y][coordinate.x] = 'x'
        }

        printMap(map)

        return cnt
    }

    private fun printMap(map: List<CharArray>) {
        map.forEach { cA -> println(String(cA)) }
        println()
    }
}