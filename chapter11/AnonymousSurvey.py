class AnonymousSurvey:
    """收集匿名调查问卷的答案"""
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示问题"""
        print(self.question)

    def store_response(self, mew_response):
        """存储答案"""
        self.responses.append(mew_response)

    def show_results(self):
        """显示所有的答案"""
        print("Survey results:")
        for response in self.responses:
            print('-' + response)
