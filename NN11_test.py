import tensorflow as tf
import pandas as pd
#from svm import svm_fn, nb_fn, knn_fn, rf_fn, dt_fn, lr_fn
#from query import future_row_data, last_row_data
import svm
import sql_functions
import normalization as nz


def predict_and_save_to_csv(
    model_path='model_11_inputs',
    input_csv_file='last_row.csv',
    
    output_csv_file='current_state.csv',
    output_future_file='future_state.csv',
    input_future_file='future_row.csv',
    threshold=0.5
):
    # Load the TensorFlow model
    loaded_model = tf.keras.models.load_model(model_path)

    # Read the new data from the CSV file
    new_data = pd.read_csv(input_csv_file)
    print(f'new data{new_data}')
    
    future_data=pd.read_csv(input_future_file)


    # Assuming new_data is a DataFrame with the same structure as the model input

    # Predict using the loaded model
    predictions = loaded_model.predict(new_data)

    
    future_predictions=loaded_model.predict(future_data)
    
    
    #predictions1 = loaded_model.predict(forecast_data)

    # Convert the predictions to binary values (0 or 1) using a threshold
    binary_predictions = (predictions > threshold).astype(int)
    
    future_predictions = (future_predictions > threshold).astype(int)
    
    print(f'binary{binary_predictions[0][0]}')
    ##### other functions 
    c_judge=[0]*6
    f_judge=[0]*6
    
    '''
    c_judge[0]=svm.svm_fn(query.last_row_data)
    c_judge[1]=svm.nb_fn(query.last_row_data)
    c_judge[2]=svm.dt_fn(query.last_row_data)
    c_judge[3]=svm.rf_fn(query.last_row_data)
    c_judge[4]=svm.lr_fn(query.last_row_data)
    c_judge[5]=svm.knn_fn(query.last_row_data)
    
    f_judge[0]=svm.svm_fn(query.future_row_data)
    f_judge[1]=svm.nb_fn(query.future_row_data)
    f_judge[2]=svm.dt_fn(query.future_row_data)
    f_judge[3]=svm.rf_fn(query.future_row_data)
    f_judge[4]=svm.lr_fn(query.future_row_data)
    f_judge[5]=svm.knn_fn(query.future_row_data)
    '''
    #binary_predictions.flatten()) is ANN result
    #future_predictions.flatten()) is ANN result
    
    print(binary_predictions[0][0])
    
    current1=any(c_judge) or bool(binary_predictions[0][0])
    future1=any(f_judge) or bool(future_predictions[0][0])
    
    #print(f'current1{current1}')
    #current1=any(current1)
    #future1=any(future1)

    #####
    
    

    # Create a DataFrame for binary predictions
    #binary_predictions_df = pd.DataFrame({'Binary_Predictions': binary_predictions.flatten()})
    binary_predictions_df = pd.DataFrame({'Binary_Predictions': [current1]})
    #future_predictions_df = pd.DataFrame({'Binary_Predictions': future_predictions.flatten()})
    future_predictions_df = pd.DataFrame({'Binary_Predictions': [future1]})
    # Save the binary predictions to a CSV file
    binary_predictions_df.to_csv(output_csv_file, index=False)
    future_predictions_df.to_csv(output_future_file, index=False)

def diagnose(new_data):
    

    model_path='model_11_inputs'
    threshold=0.5
    # Load the TensorFlow model
    
    
    loaded_model = tf.keras.models.load_model(model_path)


    # convert list to dataframe
    
    new_data=nz.normalizing(new_data)
    
    new_data=pd.DataFrame(new_data).T

    new_data.columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
           'exang', 'oldpeak', 'slope']
    
    predictions = loaded_model.predict(new_data)

    
    #predictions1 = loaded_model.predict(forecast_data)

    # Convert the predictions to binary values (0 or 1) using a threshold
    binary_predictions = (predictions > threshold).astype(int)
    
    
    
    
    return(binary_predictions)

    

if __name__=='__main__':

    # Usage with default parameters
    juan1=[47,1,4,160,286,0,2,108,1,1.5,2]
    k1=diagnose(juan1)
    