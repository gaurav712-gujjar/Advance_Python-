'''===============================================================
📌 MATRIX (NOTES + SIMPLE DEFINITIONS)
===============================================================

WHAT IS MATRIX?
A matrix is a rectangular table of numbers arranged
in rows and columns.

---------------------------------------------------------------
WHY MATRIX?
---------------------------------------------------------------
1. Stores data in structured (row–column) format.
2. Helps perform fast mathematical calculations.
3. Used in ML, AI, graphics, engineering & scientific computing.
4. Makes solving linear equations easier.
5. Represents transformations (rotation, scaling, movement).

---------------------------------------------------------------
USES OF MATRIX
---------------------------------------------------------------
✔️ Store data (tables, datasets, images)
✔️ Graphics & animations (rotate, scale, move)
✔️ Solve equations in mathematics
✔️ Deep learning & neural network calculations
✔️ Scientific simulations & statistics
✔️ Robotics movement and transformations

===============================================================
📌 MATRIX OPERATIONS (SHORT + IMPORTANT)
===============================================================

# 1️⃣ MATRIX ADDITION
A + B
Add corresponding elements of both matrices.

# 2️⃣ MATRIX SUBTRACTION
A - B
Subtract corresponding elements.

# 3️⃣ SCALAR MULTIPLICATION
kA
Multiply every element by a number ‘k’.

# 4️⃣ MATRIX MULTIPLICATION (DOT PRODUCT)
A × B
Row of A × Column of B
Used heavily in ML & Neural Networks.

# 5️⃣ TRANSPOSE OF MATRIX (Aᵀ)
Rows ↔ Columns
Flip the matrix.

# 6️⃣ DETERMINANT (det(A))
A single value representing scaling factor.

# 7️⃣ INVERSE (A⁻¹)
Matrix that reverses A.
Exists only if determinant ≠ 0.

# 8️⃣ IDENTITY MATRIX (I)
Matrix that keeps values same when multiplied.

# 9️⃣ ZERO MATRIX
All elements are zero.

===============================================================
📌 MATRIX IN MACHINE LEARNING (VERY IMPORTANT)
===============================================================

WHY MATRIX IN MACHINE LEARNING?
Because ML models perform huge mathematical computations,
and matrices make these operations extremely fast.

---------------------------------------------------------------
USES OF MATRIX IN ML
---------------------------------------------------------------
1️⃣ **Store Input Data**
   Dataset = matrix (rows = samples, columns = features)

2️⃣ **Store Weights/Parameters**
   Neural networks & regression models use weight matrices.

3️⃣ **Prediction = Matrix Multiplication**
   Output = Input × Weight
   Core operation in every ML and Deep Learning model.

4️⃣ **Backpropagation**
   Gradients, updates, error calculations → all use matrices.

5️⃣ **Image Processing**
   Images = pixel matrices
   Used in CNNs, object detection, face recognition.

6️⃣ **Feature Transformation**
   PCA, normalization, scaling → matrix operations.

7️⃣ **Statistics**
   Covariance & correlation matrices to study relationships.

===============================================================
📌 QUICK SUMMARY
---------------------------------------------------------------
✔️ Matrix = table of numbers
✔️ Used to store data and perform fast calculations
✔️ Operations = add, subtract, multiply, transpose, inverse
✔️ Machine Learning: everything uses matrices (data, weights, predictions)

==============================================================='''
import numpy as np

a=np.linspace(10,30,3)
print(a)