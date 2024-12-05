package org.example

import java.io.BufferedReader

var i = 0

fun main() {
    val bufferedReader: BufferedReader = object {}.javaClass.getResourceAsStream("/input03.txt")!!.bufferedReader()
    val text = bufferedReader.readText()


    var res = 0
    while(hasMul(text)) {
        res += readMul(text)
    }

    println(res)
}

fun readMul(text: String): Int {
    TODO("Not yet implemented")
}

fun hasMul(text: String): Boolean {
    var li = i
    li = skipUntil(text, li, 'm')
    
}

fun skipUntil(text: String, index: Int, c: Char): Int {
    var li = index
    while(li < text.length && text[li] != c) li++
    return li
}
