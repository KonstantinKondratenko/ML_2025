import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd


def task1():
    X = np.array([69, 74, 68, 70, 72, 67, 66, 70, 76, 68, 72, 79, 74, 67, 66, 71, 74, 75, 75, 76])
    Y = np.array([153, 175, 155, 135, 172, 150, 115, 137, 200, 130, 140, 265, 185, 112, 140, 150, 165, 185, 210, 220])

    def task_A(X):
        mean_X = np.mean(X)  # Выборочное среднее
        median_X = np.median(X)  # Медиана
        mode_X = stats.mode(X)  # Мода (возвращает значение и количество вхождений)
        return mean_X, median_X , mode_X
    
    def task_B(Y):
        variance_Y = np.var(Y, ddof=1)  # ddof=1 для выборочной дисперсии
        return f"Дисперсия Y: {variance_Y:.2f}"

    def task_C(X, mean_X):
        plt.figure(figsize=(10, 6))
        plt.hist(X, bins=8, density=True, alpha=0.7, label='Гистограмма X')
        x_range = np.linspace(X.min(), X.max(), 100)
        pdf = stats.norm.pdf(x_range, mean_X, np.std(X, ddof=1))
        plt.plot(x_range, pdf, 'r-', lw=2, label='Нормальное распределение')
        plt.title('Гистограмма и нормальное распределение для X')
        plt.xlabel('Возраст')
        plt.ylabel('Плотность')
        plt.legend()
        plt.grid(True)
        plt.savefig("./task_C.png")

    def task_G(X, Y):
        plt.figure(figsize=(10, 6))
        plt.scatter(X, Y, alpha=0.7)
        plt.title('Диаграмма рассеяния: Возраст и Вес')
        plt.xlabel('Возраст (X)')
        plt.ylabel('Вес (Y)')
        plt.grid(True)
        plt.savefig("./task_G.png")


    # Run task A
    mean_X, median_X , mode_X = task_A(X)
    print(f"Среднее X: {mean_X:.2f}")
    print(f"Медиана X: {median_X}")
    print(f"Мода X: {mode_X.mode} (встречается {mode_X.count} раз)")

    # Run task B
    print(task_B(Y))

    # Run task C
    task_C(X=X, mean_X=mean_X)

    # Run task G
    task_G(X=X, Y=Y)



def task3():
    mu_a, sigma_a = 4, 1
    mu_b, sigma_b = 8, 2
    
    test_values = [5, 6, 7]
    
    print(f"Распределение Na: N({mu_a}, {sigma_a})")
    print(f"Распределение Nb: N({mu_b}, {sigma_b})")
    print("\nСравнение правдоподобия:")
    
    results = []
    for x in test_values:
        likelihood_a = stats.norm.pdf(x, mu_a, sigma_a)
        likelihood_b = stats.norm.pdf(x, mu_b, sigma_b)
        
        if likelihood_a > likelihood_b:
            winner = "Na"
            advantage = likelihood_a / likelihood_b
        else:
            winner = "Nb"
            advantage = likelihood_b / likelihood_a
        
        results.append({
            'x': x,
            'likelihood_a': likelihood_a,
            'likelihood_b': likelihood_b,
            'winner': winner,
            'advantage': advantage
        })
        
        print(f"x = {x}:")
        print(f"  Правдоподобие Na: {likelihood_a:.4f}")
        print(f"  Правдоподобие Nb: {likelihood_b:.4f}")
        print(f"  Более вероятно: {winner} (в {advantage:.2f} раз) \n")
    
    plt.figure(figsize=(12, 6))
    
    x_range = np.linspace(0, 12, 1000)
    pdf_a = stats.norm.pdf(x_range, mu_a, sigma_a)
    pdf_b = stats.norm.pdf(x_range, mu_b, sigma_b)
    
    plt.plot(x_range, pdf_a, 'b-', linewidth=2, label=f'Na ~ N({mu_a}, {sigma_a})')
    plt.plot(x_range, pdf_b, 'r-', linewidth=2, label=f'Nb ~ N({mu_b}, {sigma_b})')
    
    colors = ['green', 'orange', 'purple']
    for i, x in enumerate(test_values):
        plt.axvline(x=x, color=colors[i], linestyle='--', alpha=0.7, 
                   label=f'x = {x}')
        
        y_a = stats.norm.pdf(x, mu_a, sigma_a)
        y_b = stats.norm.pdf(x, mu_b, sigma_b)
        plt.plot(x, y_a, 'bo', markersize=8)
        plt.plot(x, y_b, 'ro', markersize=8)
    
    plt.title('Сравнение нормальных распределений Na и Nb')
    plt.xlabel('Значение x')
    plt.ylabel('Плотность вероятности')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('task3_compare.png', dpi=300, bbox_inches='tight')
    
    
    for result in results:
        x = result['x']
        winner = result['winner']
        advantage = result['advantage']
        print(f"Для x = {x}: распределение {winner} более вероятно (в {advantage:.2f} раз)")
    
    return results


if __name__ == '__main__':
    print('TASK1:')
    task1()
    print('-'*50)
    print('TASK3:')
    task3()

