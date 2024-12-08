package org.example

import java.io.BufferedReader

var i = 0

fun main() {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/input03.txt")!!.bufferedReader()
    val text = bufferedReader.readText()


    var res = 0

    val r = Regex("mul\\((\\d{1,3}),(\\d{1,3})\\)")
    val matchResults = r.findAll(text)
    matchResults.forEach {
        val num1 = it.groups[1]?.value?.toInt()
        val num2 = it.groups[2]?.value?.toInt()

        println(num1.toString() + ", " + num2)

        res += (num1!! * num2!!)
    }

    println(res)
}

