import PasswordChecker    # The code to test

def test_valid_pswd():
    result = PasswordChecker.pswd_check('Pineapple_1')
    assert result == True

def test_less_than_8_chars():
    result = PasswordChecker.pswd_check('shoe')
    assert result == False

def test_no_capital():
    result = PasswordChecker.pswd_check('appleapple')
    assert result == False, "Where's your capital m8?"

def test_has_no_lowercase():
    result = PasswordChecker.pswd_check('LEMONLEMON')
    assert result == False, "Need some lowers matey"

def test_has_no_numbers():
    result = PasswordChecker.pswd_check('Pineapples')
    assert result == False, "Where's dem numbers?"

def test_has_no_underscores():
    result = PasswordChecker.pswd_check('RobinLovesDonuts')
    assert result == False, "Need me some undy scores"