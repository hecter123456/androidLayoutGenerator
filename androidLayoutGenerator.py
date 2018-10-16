import unittest

fileName = "activity_main"
width = 1080
height = 1980
tab = "    "
doubleTab = tab + tab
nameList = ["TextView", "ImageButton", "ImageView", "Button"]
endXml = "/>\n\n"

class item:
    def __init__(self, index, id, left, right, top, bottom):
        self.name = nameList[index]
        self.id = id
        self.index = index
        self.pairs = [("Left", left/width,"vertical"),\
                      ("Right", (1-right/width),"vertical"),\
                      ("Top", top/height, "horizontal"),\
                      ("Bottom", (1-bottom/height), "horizontal")]
    def writeGuide(self, name, ratio, orientation):
        return tab + "<android.support.constraint.Guideline\n"\
                   +doubleTab +"android:id=\"@+id/" + self.id + "Guide" + name + "\"\n"\
                   +doubleTab + "android:layout_width=\"wrap_content\"\n"\
                   +doubleTab + "android:layout_height=\"wrap_content\"\n"\
                   +doubleTab + "app:layout_constraintGuide_percent=\"" + "%.3f" %ratio + "\"\n"\
                   +doubleTab + "android:orientation=\"" + orientation + "\""\
                   +endXml
    def itemSwitcher(self,index):
        switcher ={
            0: doubleTab + "android:text=\"@string/" + self.id + "\"\n",
            1: doubleTab + "android:src=\"@drawable/" + self.id + "\"\n"\
               +doubleTab + "android:scaleType=\"fitXY\"\n",
            2: doubleTab + "android:src=\"@drawable/" + self.id + "\"\n"\
               +doubleTab + "android:scaleType=\"fitXY\"\n"
        }
        return switcher.get(index, "")
        
    def writeLayout(self):
        guideXml = ""
        for a,b,c in self.pairs:
            guideXml += self.writeGuide(a, b, c)
        itemXml = tab + "<" + self.name + "\n"\
                 +doubleTab + "android:id=\"@+id/" + self.id + "\"\n"\
                 +doubleTab + "android:layout_width=\"0dp\"\n"\
                 +doubleTab + "android:layout_height=\"0dp\"\n"\
                 +self.itemSwitcher(self.index)\
                 +doubleTab + "app:layout_constraintStart_toStartOf=\"@+id/" + self.id + "GuideLeft\"\n"\
                 +doubleTab + "app:layout_constraintEnd_toStartOf=\"@+id/" + self.id + "GuideRight\"\n"\
                 +doubleTab + "app:layout_constraintTop_toTopOf=\"@+id/" + self.id + "GuideTop\"\n"\
                 +doubleTab + "app:layout_constraintBottom_toTopOf=\"@+id/" + self.id + "GuideBottom\"\n"\
                 +endXml
        return guideXml + itemXml

def main():
    itemList = [item(0, "textView", 200, 300, 400, 500),\
                item(1, "test", 100, 400, 200, 100)]
    writeFile = open(fileName + ".xml", "w")
    start = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"\
+"<android.support.constraint.ConstraintLayout\n"\
+tab+"xmlns:android=\"http://schemas.android.com/apk/res/android\"\n"\
+tab+"xmlns:app=\"http://schemas.android.com/apk/res-auto\"\n"\
+tab+"xmlns:tools=\"http://schemas.android.com/tools\"\n"\
+tab+"android:layout_width=\"match_parent\"\n"\
+tab+"android:layout_height=\"match_parent\">\n\n"
    end = "</android.support.constraint.ConstraintLayout>"
    writeFile.write(start)
    for it in itemList:
        writeFile.write(it.writeLayout())
    writeFile.write(end)

if __name__ == '__main__':
    main()
