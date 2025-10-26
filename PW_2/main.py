import numpy as np

def task_1():
    # Исходные данные
    data = np.array([
        [4, 2.9],    # x1
        [2.5, 1],    # x2
        [3.5, 4],    # x3
        [2, 2.1]     # x4
    ])

    def kernel_function(x_i, x_j):
        """
        Вычисляет квадрат евклидова расстояния между двумя точками
        K(x_i, x_j) = ||x_i - x_j||^2 = (x_i1 - x_j1)^2 + (x_i2 - x_j2)^2
        """
        return (x_i[0] - x_j[0])**2 + (x_i[1] - x_j[1])**2

    # Создаем пустую матрицу 4x4
    kernel_matrix = np.zeros((4, 4))

    # Заполняем ядерную матрицу
    for i in range(4):
        for j in range(4):
            kernel_matrix[i, j] = kernel_function(data[i], data[j])

    return data, kernel_matrix


def task_2():
    # Исходные данные
    D = np.array([
        [8, -20],    # X1
        [0, -1],     # X2  
        [10, -19],   # X3
        [10, -20],   # X4
        [2, 0]       # X5
    ])
    
    # 1. Вычисляем среднее мю
    mean = np.mean(D, axis=0)
    
    # 2. Вычисляем ковариационную матрицу сигма
    cov_matrix = np.cov(D, rowvar=False, ddof=0)
    
    # 3. Вычисляем собственные числа для матрицы ковариации
    eigenvalues = np.linalg.eigvals(cov_matrix)
    
    return D, mean, cov_matrix, eigenvalues


def task_3(cov_matrix, eigenvalues):    
    # 1. Вычисляем собственные векторы и собственные числа ковариационной матрицы
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    
    # Сортируем собственные числа и векторы по убыванию (главные компоненты)
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # Первые две главные компоненты
    principal_components = eigenvectors[:, :2]
    
    # 2. Вычисляем остаточную дисперсию для каждой компоненты
    total_variance = np.sum(eigenvalues)
    
    # Доля объясненной дисперсии для каждой компоненты
    explained_variance_ratio = eigenvalues / total_variance
    
    # Остаточная дисперсия после k компонент
    residual_variance_1 = 1 - explained_variance_ratio[0]  # После 1-й компоненты
    residual_variance_2 = 1 - np.sum(explained_variance_ratio[:2])  # После 2-х компонент
    
    return (principal_components, explained_variance_ratio, 
            residual_variance_1, residual_variance_2)

if __name__ == '__main__':
    data, k_matrix = task_1()
    print(f"TASK1: \n Исходные данные: \n {data} \n\n Матрица сходства: \n {k_matrix}\n\n")

    D, mean, cov_matrix, eigenvalues = task_2()
    print(f"TASK2: \n Исходные данные: \n {D} \n\n Среднее мю: \n {mean} \n\n \
Ковариационная матрица: \n {cov_matrix} \n\n Собственные числа матрицы: \n {eigenvalues} \n\n")
    
    principal_components, explained_variance, resid_var_1, resid_var_2 = task_3(cov_matrix=cov_matrix, eigenvalues=eigenvalues)
    print(f"TASK3: \n Первые две главные компоненты: \n {principal_components} \n\n \
Доля объясненной дисперсии для каждой компоненты: \n {explained_variance} \n\n \
Остаточная дисперсия после 1-й компоненты: {resid_var_1:.4f} \n \
Остаточная дисперсия после 2-х компонент: {resid_var_2:.4f}")
