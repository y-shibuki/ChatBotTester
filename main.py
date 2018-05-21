class Responder:
    """AIの応答を制御するクラス

    プロパティ:
    name -- Responderオブジェクトの名前
    """
    def __init__(self, name):
        """文字列を受け取り,自分のnameに設定する"""
        self._name = name

    def response(self, text):
        """textを受け取りAIの応答を生成して返す"""
        return '{}ってなに？'.format(text)

    @property
    def name(self):
        """応答オブジェクトの名前"""
        return self._name

class ChatBot:
    """チャットボットのコアクラス

    プロパティ:
    name -- コアの名前
    responder_name -- 現在の応答クラスの名前
    """

    def __init__(self, name):
        """文字列を受け取り、コアインスタンスの名前に設定する
        'What'Responderインスタンスを作成し、保存する
        """

        self._name = name
        self._responder = Responder('What')
    
    def dialogue(self, text):
        """ユーザーからの入力を受け取り、Responderに処理させた結果を返す"""

        return self._responder.response(text)

    @property
    def name(self):
        """チャットボットインスタンスの名前"""
        return self._name
    
    @property
    def responder_name(self):
        """ 保存しているResponderの名前"""
        return self._responder.name
