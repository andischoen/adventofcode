package org.example

class Day05 : IDay {

    override fun solve() {
        val text = getTextFromPuzzleInput("input05.txt")

        val parts = text.split("\r\n\r\n")
        val rulesLines = parts[0].split("\r\n")
        val pageProductions = parts[1].split("\r\n")

        val rules = prepareRules(rulesLines)
        println(rules)

        var res = 0
        pageProductions.forEach {
            res += checkProduction(it, rules)
        }
        println(res)
    }

    private fun checkProduction(production: String, rules: Map<Int, List<Int>>): Int {
        val pages = production.split(",").map { it.toInt() }
        for (i in pages.indices) {
            val key = pages[i]
            for(j in i+1..<pages.size) {
                if (rules[pages[j]]?.contains(key)!!) {
                    return 0
                }
            }
        }

        return pages[(pages.size)/2]
    }

    private fun prepareRules(rulesLines: List<String>): Map<Int, List<Int>> {
        val rules = rulesLines.map {
            val parts = it.split("|")
            intArrayOf(parts[0].toInt(), parts[1].toInt())
        }.groupBy (keySelector = { it[0] }, valueTransform = { it[1] } )

        return rules
    }

}