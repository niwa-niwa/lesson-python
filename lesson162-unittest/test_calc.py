# ユニットテストのためのライブラリ
import unittest

# テストしたいクラスをインポート
import calc

release_name = 'lessaon'

class CalTest(unittest.TestCase):
  def test_add_num_and_double(self):
    cal = calc.Cal()
    self.assertEqual(cal.add_num_and_double(1, 1), 4)

  # テストをスキップさせる
  @unittest.skip('skiping')
  def test_add_num_and_double_raise(self):
    cal = calc.Cal()
    # 例外処理を実行する場合はwithステートメント
    with self.assertRaises(ValueError):
      cal.add_num_and_double('1','1')

  # If文を使ってテストをスキップさせる
  @unittest.skipIf(release_name=='lesson', 'if-skiping')
  def test_add_num_and_double_2(self):
    cal = calc.Cal()
    self.assertEqual(cal.add_num_and_double(1,1),5)


# unittestをターミナルで実行するための記述
if __name__ == '__main__':
  unittest.main()
