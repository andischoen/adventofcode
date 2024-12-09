package org.example

import java.io.BufferedReader

fun main() {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/input03.txt")!!.bufferedReader()
    var text = bufferedReader.readText()
    //text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    var res = 0

    //part2
    val excludeDontsRegex = Regex("don't\\(\\).*?do\\(\\)", RegexOption.DOT_MATCHES_ALL)
    text = excludeDontsRegex.replace(text, "")
    val removeLastDontRegex = Regex("don't\\(\\).*")
    text = removeLastDontRegex.replace(text, "")
    //part2


    val r = Regex("mul\\((\\d{1,3}),(\\d{1,3})\\)")
    val matchResults = r.findAll(text)
    matchResults.forEach {
        val num1 = it.groups[1]?.value?.toInt()
        val num2 = it.groups[2]?.value?.toInt()

        // println(num1.toString() + ", " + num2)

        res += (num1!! * num2!!)
    }

    println(res)
}

