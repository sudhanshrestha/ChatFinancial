# Financial Prediction App with LLM Integration

## Project Goals

The primary goal of this project is to develop a financial prediction application that utilizes machine learning models to predict spending and income amounts based on user input. Additionally, the application will integrate a language model to act as a financial advisor, providing insights and guidance on managing finances.

## Current Progress

### Features Implemented

1. **Data Integration and Processing**: Merged multiple datasets containing income and expense records, cleaned and transformed the data.

2. **Model Training**: Implemented various regression models and evaluated their performance using Mean Squared Error (MSE) and R² score.

3. **Hyperparameter Tuning**: Optimized model parameters to improve performance, resulting in lower MSE and improved R² scores.

4. **User Input for Predictions**: Developed a function to gather and validate user input for making predictions.

5. **Model and Scaler Saving**: Saved the trained model and scaler for future predictions.

### Visualization
- Created visualizations for total income and expenses, expenses by category, and a time series of income and expenses to help users understand their financial data better.

### Data Collection
- This application utilizes data collected from the [Money manager & expenses App](https://play.google.com/store/apps/details?id=ru.innim.my_finance) to enhance the quality and quantity of the financial records used for training the models.

## Challenges Faced

1. **Lack of Data**: Insufficient data can lead to overfitting or underfitting in models, affecting prediction accuracy. Strategies for data augmentation or seeking additional datasets may be needed.

2. **Metrics Improvements**: Despite tuning, the model performance metrics (e.g., MSE, R² score) have shown variability, indicating potential issues with model selection or feature engineering.

## Next Steps

1. **Integration of Language Model**: Implement an LLM to provide financial advice based on user queries and interactions.

2. **User Interface Development**: Create a user-friendly application interface for easier interaction with prediction and advisory features.

3. **Testing and Validation**: Conduct thorough testing to ensure prediction accuracy and LLM reliability. Gather user feedback for improvements.

4. **Deployment**: Deploy the application for public use, ensuring security and performance.

5. **Future Enhancements**: 
   - Utilize a comprehensive dataset to improve model training and performance.
   - Explore additional features like budget tracking and integration with banking APIs for real-time financial data.

## Contribution

Contributions to this project are welcome! If you have ideas or features you'd like to see implemented, feel free to open an issue or submit a pull request.
