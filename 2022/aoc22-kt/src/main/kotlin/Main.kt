import java.io.BufferedReader

fun main(args: Array<String>) {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/input.txt")!!.bufferedReader()
    val lines = bufferedReader.readLines()

    var total = 0
    var total2 = 0
    lines.forEach {
        val game = it.split(" ")
        print(it)
        print(" => ")
        val score = getScore(game[0], game[1])
        val score2 = getScore2(game[0], game[1])
        print(score)
        println(" $score2")
        total += score
        total2 += score2
    }

    println("========")
    println(total)
    println(total2)
}

fun getScore(opponent: String, me: String): Int {
    var score = 0

    val oppValue: Int = translateLetterToValue(opponent)
    val meValue: Int = translateLetterToValue(me)
    score += (meValue+1)
    score += getScoreForResult(oppValue, meValue)

    return score
}

fun getScore2(opponent: String, res: String): Int {
    var score = 0

    val oppValue: Int = translateLetterToValue(opponent)
    val meValue: Int = getMeValueForResult(oppValue, res)

    score += (meValue+1)
    score += translateLetterToValue(res) * 3

    return score
}

fun getMeValueForResult(oppValue: Int, res: String): Int {
    return when (res) {
        "X" -> { // lose
            (oppValue + 2).mod(3)
        }
        "Y" -> { // draw
            oppValue
        }
        else -> {
            (oppValue + 1).mod(3)
        }
    }
}

fun getScoreForResult(oppValue: Int, meValue: Int): Int {
    // 0 = rock, 1 = paper, 2 = scissors -> me-opponent -> result
    // -1 = lose
    // 0 = draw
    // 1 = win
    return when ((meValue - oppValue).mod(3)) {
        1 -> 6 // win
        0 -> 3 // draw
        else -> 0 // lose
    }
}

fun translateLetterToValue(me: String): Int {
    return when (me) {
        "X" -> 0 // rock
        "A" -> 0
        "Y" -> 1 // paper
        "B" -> 1
        "Z" -> 2 // scissors
        "C" -> 2
        else -> {
            throw Exception("invalid value")
        }
    }
}
