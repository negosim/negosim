import unittest
import time
from core.TimeLine import TimeLine


class TestTimeLine(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.timeline = TimeLine(10.0)

    def test_time(self):
        self.assertFalse(TestTimeLine.timeline.is_time_ended())
        print(TestTimeLine.timeline.get_time())
        time.sleep(2)
        print(TestTimeLine.timeline.get_time())
        self.assertFalse(TestTimeLine.timeline.is_time_ended())
        time.sleep(2)
        print(TestTimeLine.timeline.get_time())
        self.assertFalse(TestTimeLine.timeline.is_time_ended())
        time.sleep(2)
        print(TestTimeLine.timeline.get_time())
        self.assertFalse(TestTimeLine.timeline.is_time_ended())
        time.sleep(2)
        print(TestTimeLine.timeline.get_time())
        self.assertFalse(TestTimeLine.timeline.is_time_ended())
        time.sleep(2)
        print(TestTimeLine.timeline.get_time())
        self.assertTrue(TestTimeLine.timeline.is_time_ended())


if __name__ == '__main__':
    unittest.main()
