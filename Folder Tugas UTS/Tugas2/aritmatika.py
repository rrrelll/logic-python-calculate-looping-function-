from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

# Class untuk input data
class OperationInput(BaseModel):
    a: int
    b: int
    operator: str

@router.post("/MetodeIfElse")
def calculate_operation(input_data: OperationInput):
    a = input_data.a
    b = input_data.b
    operator = input_data.operator
    
    # logika aritmatika
    if operator == '+':
        c = a + b
        operasi = "Ditambahkan"
    elif operator == '-':
        c = a - b
        operasi = "Dikurangkan"
    elif operator == '*':
        c = a * b
        operasi = "Dikalikan"
    elif operator == '/':
        if b != 0:
            c = a / b
            operasi = "Dibagi"
        else:
            return {"code": 400, "mess": "error", "data": "pembagian dengan nol tidak valid"}
    else:
        return {"code": 400, "mess": "error", "data": "operator tidak valid"}
    
    return {
        "code": 200,
        "message": "success",
        "data": f"{a} {operasi} dengan {b} menghasilkan nilai {c}"
    }


#SWITCH CASE ( Mapping Dictionary)


@router.post("/OperasiAritmatikaMetodeMappingDictionary")
def calculate_operation(data: OperationInput):
    a = data.a
    b = data.b
    operator = data.operator

    operations = {
        '+':a + b,
        '-':a - b,
        '*':a * b,
        '/':a / b if b != 0 else "Error : Pembagian dengan nol tidak valid."
    } 

    result = operations.get(operator,"Error : Operator Tidak Valid.")
    return{
        "a" : a,
        "b" : b,
        "operator" : operator,
        "result" : result

    }



@router.post("/OperasiAritmatikaMetodeSwitchCase")
def calculate_operation(data: OperationInput):
    a = data.a
    b = data.b
    operator = data.operator


    #SWITCH CASE ( Metode Math Case )

    match operator:
        case '+':
            result = a + b
        
        case '-':
            result = a - b
        
        case '*':
            result = a * b
        
        case '/':
            result = a / b if b != 0 else "Error : Pembagian Dengan 0 Tidak Valid."
        
        case _:
            result = " Error : Operator Tidak Valid."    
            
            return {  
            "a" : a,  
            "b" : b,
            "operator" : operator,
            "result" : result
            }



@router.post("/OperasiAritmatikaMetodeTernary")
def calculate_operation(data: OperationInput):
    a = data.a
    b = data.b
    operator = data.operator


    #Metode Ternary
    
    result = (
         a + b if operator == '+' else
         a - b if operator == '-' else
         a * b if operator == '*' else
         (a / b if b != 0 else "Error : Pembagian Dengan 0 Tidak Valid.") 
         if operator == '/' else " Error : Operator Tidak Valid."
    )

    return {
        "a" : a,
        "b" : b,
        "operator" : operator,
        "result" : result
    }