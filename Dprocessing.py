import os 
import pandas as pd  
class Data_Proc:
    def __init__(self, filename):
        self.filename = filename
        self.expected_columns = [ "Участники гражданского оборота", "Тип операции", "Сумма операции", "Вид расчета",
            "Место оплаты", "Терминал оплаты", "Дата оплаты", "Время оплаты", "Результат операции", "Cash-back", "Сумма cash-back"]                 
        self.expected_dtypes = {"Участники гражданского оборота": object, "Тип операции": object, "Сумма операции": float, "Вид расчета": object,
            "Место оплаты": object, "Терминал оплаты": object, "Дата оплаты": object, "Время оплаты": object, "Результат операции": object,
            "Cash-back": object,"Сумма cash-back": float }
        
    def valid_file(self):
        try:
            if not os.path.exists(self.filename):                                                       
                raise FileNotFoundError(f"[Errno 2] No such file or directory: '{self.filename}'")      
            df = pd.read_csv(self.filename) 
            if df.empty:                                                                                
                raise ValueError("Возникла следующая ошибка: Датафрейм пуст")                           
            if list(df.columns) != self.expected_columns:                                               
                print("Названия столбцов не совпадают.")
                print("Ожидаемые:", self.expected_columns)
                print("Фактические:", list(df.columns))
                return
            for column, expected_type in self.expected_dtypes.items():                                  
                actual_type = df[column].dtype                                                          
                if actual_type != expected_type:                                                       
                    print(f"В столбце '{column}' тип данных не соответствует ожидаемому.")
                    print(f"Ожидается: {expected_type.__name__}, Фактически: {actual_type}")
                    return
            print("Чтение датафрейма завершено успешно.")
        except FileNotFoundError as e:
            print(f"Возникла следующая ошибка: {e}")
        except ValueError as e:
            print(e)
     