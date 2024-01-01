import java.io.BufferedReader


    fun main(args: Array<String>) {
        val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/input.txt")!!.bufferedReader()
        val lines: List<String> = bufferedReader.readLines()

        var total = 0
        lines.forEach {

            val num = getValueFromString(it)
            total += num
        }

        println(total)
    }

    fun getValueFromString(line: String): Int {

        val map = mutableMapOf<Int, Int>()

        addToMap(line, map, "1", 1)
        addToMap(line, map, "one", 1)
        addToMap(line, map, "2", 2)
        addToMap(line, map, "two", 2)
        addToMap(line, map, "3", 3)
        addToMap(line, map, "three", 3)
        addToMap(line, map, "4", 4)
        addToMap(line, map, "four", 4)
        addToMap(line, map, "5", 5)
        addToMap(line, map, "five", 5)
        addToMap(line, map, "6", 6)
        addToMap(line, map, "six", 6)
        addToMap(line, map, "7", 7)
        addToMap(line, map, "seven", 7)
        addToMap(line, map, "8", 8)
        addToMap(line, map, "eight", 8)
        addToMap(line, map, "9", 9)
        addToMap(line, map, "nine", 9)

        val sortedMap = map.toSortedMap()

        val left:Int = sortedMap[sortedMap.firstKey()]!!
        val right:Int = sortedMap[sortedMap.lastKey()]!!

        return left*10+right
    }

    fun addToMap(line: String, map: MutableMap<Int, Int>, searchFor:String, value:Int) {
        var index: Int = line.indexOf(searchFor)
        if (index != -1) {
            map[index] = value
        }
        index = line.lastIndexOf(searchFor)
        if (index != -1) {
            map[index] = value
        }
    }