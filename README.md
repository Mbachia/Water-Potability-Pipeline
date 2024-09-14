# Water Potability Prediction Project

This project focuses on predicting water potability (suitability for human consumption) based on various water quality parameters using a machine learning approach. The dataset consists of measurements such as pH levels, water hardness, dissolved solids, and other key indicators that help determine whether water is safe for drinking.

---

## 1. Business Understanding
The objective is to assess water quality and predict its potability, making it suitable for applications in water treatment planning, environmental monitoring, and ensuring compliance with water quality standards. The project aims to help water treatment plants, environmental agencies, and researchers make informed decisions regarding the safety of water for consumption.

---

## 2. Data Understanding
The dataset includes the following features:
- **pH**: Water's pH level.
- **Hardness**: Mineral content in water.
- **Solids**: Total dissolved solids.
- **Chloramines**: Concentration of chloramines in water.
- **Sulfate**: Sulfate concentration.
- **Conductivity**: Electrical conductivity of the water.
- **Organic Carbon**: Organic carbon content.
- **Trihalomethanes**: Trihalomethanes concentration, indicating disinfection by-products.
- **Turbidity**: Water clarity.
- **Potability**: Target variable indicating potability (1 for potable, 0 for not potable)

## 3. Data Preparation
- **Preprocessing**:
  - Missing values were imputed for features like sulfate and trihalomethanes.

## 4. Modeling
- The project used Random Forest Classifier as the model.
- The evaluation metrics used was Accuracy which was at 68% which has potential for improvement. 
  
## 5. Deployment
The FastAPI service was deployed, offering a user-friendly interface for predicting water potability based on key water quality parameters. DVC was used to track model versions, ensuring smooth updates and consistency across different environments.

---

## Conclusion
This project successfully implemented a water potability prediction model, providing valuable insights for water quality assessment and helping agencies, researchers, and environmental planners make data-driven decisions to ensure water safety.
