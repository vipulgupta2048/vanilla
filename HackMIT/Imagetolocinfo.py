from watson_developer_cloud import VisualRecognitionV3
import json


visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='vFTSKJUVMqQs9h4mHY0wwqI9yPjYS6z1tbv_ZkCfV3SX')

with open('flood_people_on_house.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.1',
        owners=["me"]).get_result()
        #classifier_ids=['default']).get_result()

    print(json.dumps(classes, indent=4))

