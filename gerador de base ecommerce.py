import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurar a semente para resultados consistentes
np.random.seed(42)

# Função para gerar datas
def generate_dates(start_date, end_date):
    return pd.date_range(start=start_date, end=end_date)

# Parâmetros
start_date = "2023-01-01"
end_date = datetime.today().strftime("%Y-%m-%d")  # Data de hoje
num_products = 20
num_customers = 50
average_sales_per_month = 1000

# Gerar datas e calcular total de vendas
dates = generate_dates(start_date, end_date)
total_sales = len(dates) * (average_sales_per_month // 30)

# Lista de estados brasileiros
states = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", 
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", 
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]

# Gerar dados fictícios
data = {
    "Order_ID": [f"ORD{i:05d}" for i in range(1, total_sales + 1)],
    "Order_Date": np.random.choice(dates, size=total_sales),
    "Customer_ID": np.random.choice([f"C{i:03d}" for i in range(1, num_customers + 1)], size=total_sales),
    "Product_ID": np.random.choice([f"P{i:03d}" for i in range(1, num_products + 1)], size=total_sales),
    "Quantity": np.random.randint(1, 5, size=total_sales),
    "Price": np.round(np.random.uniform(10.0, 500.0, size=total_sales), 2),
    "State": np.random.choice(states, size=total_sales),
}

# Criar DataFrame
sales_df = pd.DataFrame(data)

# Exibir um exemplo e salvar como CSV
print(sales_df.head())

# Salvar para uso posterior
file_path = "ecommerce_sales_brazil.csv"
sales_df.to_csv(file_path, index=False)
print(f"Base de dados salva em: {file_path}")
