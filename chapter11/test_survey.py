import unittest

from chapter11.survey import AnonymousSurvey


class TestAnonmyousSurvey(unittest.TestCase):
    """测试AnonymousSurvey类的测试"""

    def setUp(self):
        """创建一个调查对象和一组答案"""
        question = 'What language did you first learn to speal?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', '汉语', 'Spanish']

    def test_store_single_response(self):
        """测试单个答案回妥善的存储"""
        self.my_survey.store_response('English')
        self.assertIn('English', self.my_survey.responses)

    def test_store_three_responses(self):
        """测试单个答案回被妥善的存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main":
    unittest.main()