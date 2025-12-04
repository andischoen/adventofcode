package org.example

class Day09: IDay {
    override fun solve() {
        val disk = getTextFromPuzzleInput("input09.txt")

        var iFront = 0
        var iBack = disk.length-1
        var fileIdFront = 0
        var fileIdBack = (disk.length / 2)
        var filePartsBack = disk[iBack].digitToInt()

        val defragged = mutableListOf<Int>()

        while(iFront < iBack) {
            for(i in 0..<disk[iFront].digitToInt()) {
                defragged.add(fileIdFront)
            }
            fileIdFront++
            iFront++

            var stop = false
            // front index now points to empty space - fill it
            for(i in 0..<disk[iFront].digitToInt()) {
                while(filePartsBack == 0) {
                    fileIdBack--
                    iBack -= 2
                    filePartsBack = disk[iBack].digitToInt()
                    if(iBack < iFront) { // exit through the gift shop... we already had this...
                        stop = true
                    }
                }
                if(!stop) {
                    defragged.add(fileIdBack)
                    filePartsBack--
                }
            }
            // now move to next file
            iFront++
        }

        if(fileIdBack >= fileIdFront) { // that file has not been entered yet...
            while (filePartsBack > 0) {
                defragged.add(fileIdBack)
                filePartsBack--
            }
        }

        //println(defragged)

        val checksum = defragged.mapIndexed { index, value -> (index*value).toLong()}.sum()

        println("The checksum is $checksum")
    }
}