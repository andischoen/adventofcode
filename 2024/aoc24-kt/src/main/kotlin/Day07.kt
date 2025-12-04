package org.example

import java.lang.Math.*
import java.math.BigInteger
import kotlin.math.pow

class Day07 : IDay {

    override fun solve() {
        var lines = getLinesFromPuzzleInput("input07.txt")

        var calibrationResult:BigInteger = BigInteger.ZERO
        var calibrationResult2:BigInteger = BigInteger.ZERO

        var lineNum = 0
        lines.forEach {
            var evaluationResult = evaluate(it, lineNum++)
            calibrationResult += evaluationResult
            calibrationResult2 += evaluationResult
            if(evaluationResult == BigInteger.ZERO) {
                calibrationResult2 += evaluateTernary(it, lineNum)
            }
        }

        println("Calibration result = $calibrationResult")
        println("Calibration result2 = $calibrationResult2")
    }

    private fun evaluate(line: String, lineNum: Int): BigInteger {
        val lineParts = line.split(": ")
        val testValue = BigInteger(lineParts[0])
        val values = lineParts[1].split(" ").map { BigInteger(it) }

        // create all combinations of 2 operators, by using binary translation all numbers in
        // in the range - 2^n-1 where n is the number of digits/operators
        val operatorCount = values.size - 1
        val numOfOperatorVariations = 2.0.pow(operatorCount.toDouble()).toInt() - 1
        for(i in 0 .. numOfOperatorVariations) {
            // don't forget to pad so that we have always the same number of digits
            val operators = i.toString(2).padStart(operatorCount, '0')

            var result = values[0]
            for(c in operators.indices) {
                //add or multiply depending on the operator with the next number
                if (operators[c] == '0') result += values[c+1]
                else result *= values[c+1]
            }

            if (result == testValue) {
                println("$lineNum => Operator combi to succeed: $operators")
                return testValue
            }
        }

        return BigInteger.ZERO
    }

    private fun evaluateTernary(line: String, lineNum: Int): BigInteger {
        val lineParts = line.split(": ")
        val testValue = BigInteger(lineParts[0])
        val values = lineParts[1].split(" ").map { BigInteger(it) }

        // create all combinations of 2 operators, by using binary translation all numbers in
        // in the range - 2^n-1 where n is the number of digits/operators
        val operatorCount = values.size - 1
        val numOfOperatorVariations = 3.0.pow(operatorCount.toDouble()).toInt() - 1
        for(i in 0 .. numOfOperatorVariations) {
            // don't forget to pad so that we have always the same number of digits
            val operators = i.toString(3).padStart(operatorCount, '0')

            var result = values[0]
            for(c in operators.indices) {
                //add or multiply depending on the operator with the next number
                if (operators[c] == '0') result += values[c+1]
                else if (operators[c] == '1') {
                    result = BigInteger(result.toString() + values[c+1].toString())
                }
                else result *= values[c+1]
            }

            if (result == testValue) {
                println("$lineNum => Operator combi to succeed: $operators")
                return testValue
            }
        }

        return BigInteger.ZERO
    }
}