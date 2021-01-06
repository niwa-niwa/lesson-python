# 例外処理のpyテストをする場合はpytestをインポートする
import pytest

# テストしたいクラスをインポート
import calc

is_release = True

# メソッドのみ実行する場合、メソッド名の前に「test_」をつける
def test_add_num_and_double():
  cal = calc.Cal()
  assert cal.add_num_and_double(1, 1) == 4


# クラスで実行する場合、クラス名の前に「Test」をつける
class TestCal(object):
  def test_add_num_and_double(self):
    cal = calc.Cal()
    assert cal.add_num_and_double(1, 1) == 4

  #例外処理を実行する場合はpytestをインポートしてWithステートで記述する
  def test_add_num_and_double_raise(self):
    with pytest.raises(ValueError):
      cal = calc.Cal()
      cal.add_num_and_double('1', '1')

  #pytestをスキップさせる
  @pytest.mark.skip(reason='skip!')
  def test_add_num_and(self):
    cal = calc.Cal()
    assert cal.add_num_and_double(1, 1) == 4

  #pytestをif文を使ってスキップさせる
  @pytest.mark.skipif(is_release==True, reason='skip!')
  def test_add_num(self):
    cal = calc.Cal()
    assert cal.add_num_and_double(1, 1) == 4
