package andi.aoc25.day08

import andi.aoc25.IDay
import andi.aoc25.getLinesFromPuzzleInput
import kotlin.math.pow

class Day08: IDay {

    data class JunctionBox(val x:Int, val y:Int, val z:Int)
    val distances = ArrayList<Triple<JunctionBox, JunctionBox, Long>>()

    private fun getDistance(p1: JunctionBox, p2: JunctionBox): Long {
        return  (p1.x - p2.x).toDouble().pow(2).toLong() +
                (p1.y - p2.y).toDouble().pow(2).toLong() +
                (p2.z - p1.z).toDouble().pow(2).toLong()
    }

    override fun solve(part: Int, sample: Boolean): String {
        // get input in proper data objects
        val filename = if(sample) "input08-sample.txt" else "input08.txt"
        val points = getLinesFromPuzzleInput(filename).map {
            line ->
                val coordinates = line.split(",").map { it.toInt() }
            JunctionBox(coordinates[0], coordinates[1], coordinates[2])
        }

        // caclulate all distances and sort
        for(i in points.indices) {
            for(j in i+1 until points.size) {
                distances.add(Triple(points[i], points[j], getDistance(points[i], points[j])))
            }
        }

        distances.sortBy { it.third }

        // now take the first 1000 (in Sample: 10) and connect them
        val circuits = ArrayList<HashSet<JunctionBox>>()
        var res: Int = 0

        if(part == 1) {
            val count = if (sample) 10 else 1000
            for (i in 0 until count) {
                makeConnection(i, circuits)
            }
            circuits.sortByDescending { c -> c.size }
            res = circuits.take(3).map { c -> c.size }.reduce { acc, size -> acc * size }
            return res.toString()
        } else {
            var ind = 0
            while(circuits.size <= 1) {
                makeConnection(ind, circuits)
                ind++
            }
            while(circuits.size > 1 || circuits[0].size < points.size) {
                makeConnection(ind, circuits)
                ind++
            }
            val res2 = distances[ind-1].first.x.toLong() * distances[ind-1].second.x.toLong()
            return res2.toString()
        }


    }

    private fun makeConnection(
        distInd: Int,
        circuits: ArrayList<HashSet<JunctionBox>>
    ) {
        val conn = distances[distInd]
        val circuit1 = circuits.firstOrNull() { c -> c.contains(conn.first) }
        val circuit2 = circuits.firstOrNull() { c -> c.contains(conn.second) }
        if (circuit1 == null && circuit2 == null) { //neither junction box is not yet in a circuit
            val circuit = HashSet<JunctionBox>()
            circuits.add(circuit)
            circuit.add(conn.first)
            circuit.add(conn.second)
        } else if (circuit1 != null && circuit2 != null) { //both boxes are in a circuit
            if (circuit1 != circuit2) { //and if it's not the same circuit, merge them
                circuit1.addAll(circuit2)
                circuits.remove(circuit2)
            }
        } else { //add the box, that is not yet in the circuit
            val circuit = circuit1 ?: circuit2
            circuit?.add(conn.first)
            circuit?.add(conn.second)
        }
    }
}