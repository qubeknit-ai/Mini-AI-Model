# Mini AI Model Trainer Framework

A simple Python-based mini framework that simulates how machine learning models are configured, trained, and evaluated. Inspired by frameworks like PyTorch and scikit-learn, this project demonstrates core Object-Oriented Programming (OOP) concepts.

---

## 🚀 Features

- Multiple model support (Linear Regression, Neural Network)
- Unified training pipeline using a Trainer class
- Config-driven model setup
- Easily extensible architecture
- Pure Python (no external libraries)

---

## 📁 Project Structure

mini_ai_framework/
- model_config.py # Stores model configuration
- base_model.py # Base class for models
- linear_model.py # Linear Regression implementation
- neural_model.py # Neural Network implementation
- data_loader.py # Handles dataset
- trainer.py # Training pipeline
- main.py # Entry point


---

## 🧠 OOP Concepts Implemented

| Concept | Implementation |
|--------|--------------|
| Class Attribute | BaseModel.model_count |
| Instance Attributes | ModelConfig (learning_rate, epochs) |
| Abstraction | BaseModel defines train() and evaluate() |
| Inheritance | Models extend BaseModel |
| Method Overriding | train() and evaluate() |
| super() | Used in child constructors |
| Polymorphism | Trainer works with any model |
| Composition | Model contains ModelConfig |
| Aggregation | Trainer uses DataLoader |
| Magic Method | __repr__ in ModelConfig |

---

## ▶️ How to Run

1. Open terminal in the project folder  
2. Run: python main.py

## Author
- Muhammad Aliyan
- For NAVTTC Project 1