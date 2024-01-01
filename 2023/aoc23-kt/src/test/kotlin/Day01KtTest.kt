import org.junit.jupiter.api.Assertions.*

class Day01KtTest {

    @org.junit.jupiter.api.Test
    fun getValueFromString() {
        assertEquals(29, getValueFromString("two1nine"))
        assertEquals(83, getValueFromString("eightwothree"))
        assertEquals(13, getValueFromString("abcone2threexyz"))
        assertEquals(24, getValueFromString("xtwone3four"))
        assertEquals(42, getValueFromString("4nineeightseven2"))
        assertEquals(14, getValueFromString("zoneight234"))
        assertEquals(76, getValueFromString("7pqrstsixteen"))
        assertEquals(99, getValueFromString("9dlvndqbddghpxc"))
        assertEquals(71, getValueFromString("78blgveightfiveone7bnsfnrmxsmtwonemrb"))
    }
}