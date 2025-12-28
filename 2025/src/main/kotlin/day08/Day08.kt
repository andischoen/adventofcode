package andi.aoc25.day08

import andi.aoc25.IDay
import andi.aoc25.getLinesFromPuzzleInput

class Day08: IDay {

    data class JunctionBox(val x:Int, val y:Int, val z:Int)

    private fun getDistance(p1: JunctionBox, p2: JunctionBox): Long {
        return  Math.powExact((p1.x - p2.x).toLong(), 2) +
                Math.powExact((p1.y - p2.y).toLong(), 2) +
                Math.powExact((p2.z - p1.z).toLong(), 2)
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
        val distances = ArrayList<Triple<JunctionBox, JunctionBox, Long>>()
        for(i in points.indices) {
            for(j in i+1 until points.size) {
                distances.add(Triple(points[i], points[j], getDistance(points[i], points[j])))
            }
        }
        distances.sortBy { it.third }

        // now take the first 1000 (in Sample: 10) and connect them
        val count = if(sample) 10 else 1000
        val circuits = ArrayList<HashSet<JunctionBox>>()
        for(i in 0 until count) {
            val conn = distances[i]
            val circuit1 = circuits.firstOrNull() { c -> c.contains(conn.first) }
            val circuit2 = circuits.firstOrNull() { c -> c.contains(conn.second) }
            if (circuit1 == null && circuit2 == null) { //neither junction box is not yet in a circuit
                val circuit = HashSet<JunctionBox>()
                circuits.add(circuit)
                circuit.add(conn.first)
                circuit.add(conn.second)
            } else if (circuit1 != null && circuit2 != null) { //both boxes are in a circuit
                if(circuit1 != circuit2) { //and if it's not the same circuit, merge them
                    circuit1.addAll(circuit2)
                    circuits.remove(circuit2)
                }
            } else { //add the box, that is not yet in the circuit
                val circuit = circuit1 ?: circuit2
                circuit?.add(conn.first)
                circuit?.add(conn.second)
            }

        }
        circuits.sortByDescending { c -> c.size }
        val res = circuits.take(3).map { c -> c.size}.reduce { acc, size -> acc * size }
        return res.toString()
    }
}