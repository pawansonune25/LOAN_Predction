import pickle
import config

model = pickle.load(open(config.MODEL_PATH,'rb'))


def loan_prediction(data):

    result = model.predict(data)
    

    if result[0] == 1:
        return "Loan Approved"

    else:
        return  "Loan Not Approved"
