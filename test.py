import unittest
from qlink import messageExist
from qlink import paliStatus


#test palidromes
class testQlink(unittest.TestCase):

    def palidrometest(self):
        # empty string
        assert paliStatus('') is True

        # mirror string
        assert paliStatus('LOOL') is True

        # palidromes with white spaces
        assert paliStatus('euston saw i was not sue') is True

        # palidromes with mixed cases and white spaces
        assert paliStatus('Too hot to hoot') is True

        # palidromes with puntuations and white spaces
        assert paliStatus('Telegram, Margelet!') is True

        # non palidrome word
        assert paliStatus('daniel') is False

        # non palidrome sentence
        assert paliStatus('Qlink loves data!') is False



    def messageExist(self):

        assert messageExist("Sore was I ere I saw Eros.") is True

        assert messageExist("Dont sleep today") is False

        assert messageExist("Nella won't set a test now, Allen.") is True

        assert messageExist("Work starts at 2AM") is False





if __name__ == '__main__':
    unittest.main()