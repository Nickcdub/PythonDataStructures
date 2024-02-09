from LinkedList import LinkedList
import unittest

class LinkedListTester(unittest.TestCase):
    def test1(self):
        print("Test 1: Testing Append")
        testList = LinkedList()
        self.assertEqual(testList.display(),"[]")
        self.assertEqual(testList.size, 0)
        print("Test Case 1.1: init list success!")

        testList.append(5)
        self.assertEqual(testList.display(),"[5]")
        self.assertEqual(testList.size, 1)
        print("Test Case 1.2: init append success!")

        testList.append("testString")
        self.assertEqual(testList.display(),"[5, testString]")
        self.assertEqual(testList.size, 2)
        print("Test Case 1.2: secondary append success!")

        print("Test 1: Success!\n")
    
    def test2(self):
        print("Test 2: Testing Prepend")
        testList = LinkedList()
        self.assertEqual(testList.display(),"[]")
        self.assertEqual(testList.size, 0)
        print("Test Case 2.1: init list success!")

        testList.prepend(5)
        self.assertEqual(testList.display(),"[5]")
        self.assertEqual(testList.size, 1)
        print("Test Case 2.2: init prepend success!")

        testList.prepend("testString")
        self.assertEqual(testList.display(),"[testString, 5]")
        self.assertEqual(testList.size, 2)
        print("Test Case 2.3: secondary prepend success!")
        print("Test 2: Success!\n")

    def test3(self):
        print("Test 3: Testing Append combined with Prepend")
        testList = LinkedList()
        self.assertEqual(testList.display(),"[]")
        self.assertEqual(testList.size, 0)
        print("Test Case 3.1: init list success!")

        testList.prepend(5)
        self.assertEqual(testList.display(),"[5]")
        self.assertEqual(testList.size, 1)
        print("Test Case 3.2: init prepend success!")


        testList.append("testString")
        self.assertEqual(testList.display(),"[5, testString]")
        self.assertEqual(testList.size, 2)
        print("Test Case 2.3: append following prepend success!")

        print("Success!\n")

    def test4(self):
        print("Test 4: Testing Deletion")
        testList = LinkedList()
        testList.append(5)
        testList.append(True)
        testList.prepend("prepend")
        testList.append("end")
        self.assertEqual(testList.display(),"[prepend, 5, True, end]")
        self.assertEqual(testList.size, 4)
        print("Test Case 4.1: init list success!")

        self.assertEqual(testList.deleteAt(2), True)
        self.assertEqual(testList.display(), "[prepend, 5, end]")
        print("Test Case 4.2: middle delete success!")

        self.assertEqual(testList.deleteAt(0), "prepend")
        self.assertEqual(testList.display(), "[5, end]")
        print("Test Case 4.3: head delete success!")

        self.assertEqual(testList.deleteAt(1), "end")
        self.assertEqual(testList.display(), "[5]")
        print("Test Case 4.4: tail delete success!")

        self.assertEqual(testList.deleteAt(1), None)
        self.assertEqual(testList.display(), "[5]")
        print("Test Case 4.5: out of bounds input handling success!")

        print("Success!\n")

    def test5(self):
        print("Test Case 2.2: Testing Get function")
        testList = LinkedList()
        testList.append(5)
        testList.append(True)
        testList.prepend("prepend")
        testList.append("end")

        self.assertEqual(testList.get(0),"prepend")
        self.assertEqual(testList.get(1),5)
        self.assertEqual(testList.get(2),True)
        self.assertEqual(testList.get(3),"end")
        print("Test Case 5.1: getting all indeces success!")

        self.assertEqual(testList.get(4), None)
        print("Test Case 5.2: out of bounds input handling success!")
        print("Success!\n")



if __name__ == '__main__':
    unittest.main()
