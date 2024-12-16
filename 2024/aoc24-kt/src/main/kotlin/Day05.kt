package org.example

class Day05 : IDay {

    override fun solve() {
        val text = getTextFromPuzzleInput("input05.txt")

        val parts = text.split("\r\n\r\n")
        val rulesLines = parts[0].split("\r\n")
        val pageProductions = parts[1].split("\r\n")

        val rules = prepareRules(rulesLines)

        var res = 0
        pageProductions.forEach {
            res += checkProduction(it, rules)
        }
        println("part 1 result: $res")

        res = 0
        val wrongProductions = pageProductions.filter { checkProduction(it, rules) == 0 }
        wrongProductions.forEach{
            res += fixProduction(it, rules)
        }

        println("part 2 result: $res")
    }

    private fun fixProduction(production: String, rules: Map<Int, List<Int>>): Int {
        val pages = production.split(",").map { it.toInt() }.toMutableList()
        return fixProduction(pages, rules)
    }

    private fun fixProduction(
        pages: MutableList<Int>,
        rules: Map<Int, List<Int>>
    ): Int {
        for (i in pages.indices) {
            val key = pages[i]
            for (j in i + 1..<pages.size) {
                if (rules[pages[j]]?.contains(key)!!) {
                    swapPlaces(i, j, pages)
                    return fixProduction(pages, rules)
                }
            }
        }

        return pages[(pages.size) / 2]
    }

    private fun swapPlaces(i: Int, j: Int, pages: MutableList<Int>) {
        val temp = pages[i]
        pages[i] = pages[j]
        pages[j] = temp
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