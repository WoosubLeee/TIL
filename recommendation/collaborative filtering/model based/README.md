# Model-based

## Matrix factorization

Matrix factorization can be seen as breaking down a large matrix into a product of smaller ones. In the case of matrices, a matrix A with dimensions `m x n` can be reduced to a product of two matrices X and Y with dimensions `m x p` and `p x n` respectively.

![Illustration of matrix factorization using the recurring movie example.](https://developers.google.com/machine-learning/recommendation/images/Matrixfactor.svg)

The reduced matrices actually represent the users and items individually. The **m** rows in the first matrix represent the **m** users, and the **p** columns tell you about the features or characteristics of the users. The same goes for the item matrix with **n** items and **p** characteristics.

<img src="https://files.realpython.com/media/dimensionality-reduction.f8686dd52b9c.jpg" alt="A matrix factorized into two matrices using dimensionality reduction" style="zoom:50%;" />

On the example above, the two columns in the user matrix and the two rows in the item matrix are called latent factors and are an indication of hidden characteristics about the users or the items. The number of such factors can be anything from one to hundreds or even thousands. This number is one of the things that need to be optimized during the training of the model.

These latent factors need not be analyzed too much. These are patterns in the data that will play their part automatically whether you decipher their underlying meaning or not.