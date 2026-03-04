from EmotionDetection import emotion_detector

def test_emotion_detection():

    result1 = emotion_detector("I am glad this happened")
    assert result1['dominant_emotion'] == 'joy'

    result2 = emotion_detector("I am really mad about this")
    assert result2['dominant_emotion'] == 'anger'

    result3 = emotion_detector("I feel disgusted just hearing about this")
    assert result3['dominant_emotion'] == 'disgust'

    result4 = emotion_detector("I am so sad about this")
    assert result4['dominant_emotion'] == 'sadness'

    result5 = emotion_detector("I am really afraid that this will happen")
    assert result5['dominant_emotion'] == 'fear'

    print("All tests passed")

test_emotion_detection()

