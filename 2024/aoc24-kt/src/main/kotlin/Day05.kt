package org.example

class Day05 {

    fun solve() {
        val text = getTextFromPuzzleInput("input05-test.txt")

        val parts = text.split("\r\n\r\n")
        val rulesLines = parts[0].split("\r\n")
        val pageProductions = parts[1].split("\r\n")

        val rules = prepareRules(rulesLines)
        println(rules)
    }

    private fun prepareRules(rulesLines: List<String>): MutableMap<Int, HashSet<Int>?> {
        val rules = HashMap<Int, HashSet<Int>?>().withDefault { HashSet<Int>() }
        for (rule in rulesLines) {
            val parts = rule.split("|")
            val key = parts[0].toInt()
            val value = parts[1].toInt()

            if(!rules.contains(key)) {
                rules[key] = hashSetOf(value)
            } else {
                rules[key]?.add(value)
            }

        }

        return rules
//        val rules = mutableListOf<IntArray>()
//
//        rulesLines.forEach() {
//            val parts = it.split("|")
//            rules.add(intArrayOf(parts[0].toInt(), parts[1].toInt()))
//        }
//
//        rules.groupBy (keySelector = { it[0] }, valueTransform = { it[1] } )
//
//        return rules
    }

}