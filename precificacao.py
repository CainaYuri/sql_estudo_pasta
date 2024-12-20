import numpy as np #maniulação de arrays 
import matplotlib.pyplot as plt # visualizar os dados 
from sklearn.linear_model import LinearRegression #criar modelo de regressão linear 
from sklearn.metrics import mean_absolute_error, r2_score #avaliar o modelo 

#criar conjunto de dados de diamentros e preços de pizzas
x = np.array([6,8,10,14,18]) #diametro em polegadas pizzas
y = np.array([7,9,13,17.5,20]) #preço em reais 



#visualização dos dados em gráfico de disperção 
plt.scatter(x,y)
plt.xlabel('diametro em polegada') #adicionar o rotulo eixo x
plt.xlabel('Preço da pizza em razão de seu diametro') #adicionar o rótulo do eixo y
plt.title('Preço da pizza em relação ao diametro') #adicionar o título do gráfico 
plt.show()

#criar e treinar um modelo de regressão linear com os dados 
model = LinearRegression() #intanciar o modelo
x = x.reshape(-1,1) #transformar o array X em uma matriz de uma coluna 
model.fit(x,y) #treinar o modelo com os dados 

#Avaliar o desempenho do modelo com algumas métricas
y_pred = model.predict(x) #fazer as previsões para os dados de treino 
mse = mean_absolute_error(y, y_pred) #calcular o erro quadrático médio 
r2 = r2_score(y, y_pred) #calcular o coeficiente de determinação 
print(f'{mse:.2f}')
print(f'{r2:.2f}')

#previsão para uma nova pizza 
x_new = np.array([12]) #diametro para nova pizza
y_new = model.predict(x_new.reshape(-1, 1))#fazer a previsão para a nova pizza 

print(f'Uma pizza de: {x_new [0]} polegadas, custa r$: {y_new[0]:.2f}')









