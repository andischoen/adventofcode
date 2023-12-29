import org.junit.jupiter.api.Assertions.*

class MainKtTest {

    @org.junit.jupiter.api.Test
    fun getScore() {
        assertEquals(8, getScore("A", "Y"))
        assertEquals(1, getScore("B", "X"))
        assertEquals(6, getScore("C", "Z"))
        assertEquals(7, getScore("C", "X"))
    }

    @org.junit.jupiter.api.Test
    fun getScoreForResult() {
        assertEquals(6, getScoreForResult(0, 1))
        assertEquals(3, getScoreForResult(0, 0))
        assertEquals(0, getScoreForResult(0, 2))
    }

    @org.junit.jupiter.api.Test
    fun getScoreForShape() {
        assertEquals(1, translateLetterToValue("X"))
        assertEquals(2, translateLetterToValue("Y"))
        assertEquals(3, translateLetterToValue("Z"))
    }
}