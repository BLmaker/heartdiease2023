import tensorflow as tf
import pandas as pd



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

    # Create a DataFrame for binary predictions
    binary_predictions_df = pd.DataFrame({'Binary_Predictions': binary_predictions.flatten()})
    
    future_predictions_df = pd.DataFrame({'Binary_Predictions': future_predictions.flatten()})

    # Save the binary predictions to a CSV file
    binary_predictions_df.to_csv(output_csv_file, index=False)
    future_predictions_df.to_csv(output_future_file, index=False)

# Usage with default parameters
predict_and_save_to_csv()
