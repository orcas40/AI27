from excel.saveExcel import SaveExcel

def save_excel(driver, data_to_save, name_excel):
    try:
        save_excel = SaveExcel(driver, data_to_save, name_excel)
        save_excel.save_data_excel()
    except Exception as e:
        print(f"Error en excel_service : {e}")